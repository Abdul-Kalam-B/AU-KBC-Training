from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List


class Employee(BaseModel):
    name: str
    age: int
    position: str
    salary: float

class EmployeeInDB(Employee):
    id: str

app = FastAPI()

MONGODB_URL = "mongodb+srv://abdulkalamb23:Mongo123@pymongo.tvmog.mongodb.net/fast?retryWrites=true&w=majority&appName=Pymongo"  # Replace with your MongoDB connection string
client = AsyncIOMotorClient(MONGODB_URL)
db = client["employee_management"] 
collection = db["employees"]  

@app.post("/employees/", response_model=EmployeeInDB)
async def create_employee(employee: Employee):
    employee_dict = employee.dict()
    result = await collection.insert_one(employee_dict)
    employee_dict["id"] = str(result.inserted_id)
    return employee_dict

@app.get("/employees/", response_model=List[EmployeeInDB])
async def read_employees():
    employees = []
    async for employee in collection.find():
        employee["id"] = str(employee["_id"])  
        employees.append(employee)
    return employees

@app.get("/employees/{employee_id}", response_model=EmployeeInDB)
async def read_employee(employee_id: str):
    employee = await collection.find_one({"_id": ObjectId(employee_id)})
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    employee["id"] = str(employee["_id"])
    return employee

@app.put("/employees/{employee_id}", response_model=EmployeeInDB)
async def update_employee(employee_id: str, employee: Employee):
    result = await collection.update_one({"_id": ObjectId(employee_id)}, {"$set": employee.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found or no changes made")
    employee_dict = employee.dict()
    employee_dict["id"] = employee_id
    return employee_dict

@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: str):
    result = await collection.delete_one({"_id": ObjectId(employee_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted"}

@app.get("/")
async def root():
    return {"message": "Welcome to the Employee Management System!"}
