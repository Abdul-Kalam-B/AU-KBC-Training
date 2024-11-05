from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import easyocr
from io import BytesIO
from PIL import Image

app = FastAPI()

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):

    image_data = await file.read()
    image = Image.open(BytesIO(image_data))
    
 
    result = reader.readtext(image)

    extracted_text = " ".join([text for _, text, _ in result])
    
    return JSONResponse(content={"extracted_text": extracted_text})
