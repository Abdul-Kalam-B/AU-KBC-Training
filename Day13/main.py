from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

students = {}

class Student(BaseModel):
    id:int
    name:str
    age:int
    grade:str 

#Get all     

@app.get("/students",response_model=List[Student])
async def get_student():
    return list(students.values())

#Get specific student

@app.get("/students/{student_id}",response_model=Student)
async def get_student(student_id:int):
    student = students.get(student_id)
    if not student:
        raise HTTPException(status_code=404,detail="Student not found")
    return student

#Add a new student

@app.post("/students/",response_model=Student)
async def create_student(student: Student):
    if student.id in students:
        raise HTTPException(status_code=400,detail="Student ID already exists")
    students[student.id] = student
    return student

#update student details

@app.put("/students/{student_id}",response_model=Student)
async def update_student(student_id:int , updated_student:Student):
    if student_id not in students:
        raise HTTPException(status_code=404 , detail="Student not found")
    if student_id != updated_student.id:
        raise HTTPException(status_code=400, detail="Student ID mismatch")
    
    students[student_id] = updated_student
    return updated_student

#Remove a student by ID 

@app.delete("/students/{student_id}")
async def delete_student(student_id:int):
    if student_id not in students:
        raise HTTPException(status_code=404,detail="Student not found")
    del students[student_id]
    return {"message": f"Student with ID {student_id} has been deleted"}






