from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from utils.predict import load_model_and_predict
from utils.predict import load_model_and_predict

import uvicorn

app = FastAPI()

@app.get("/")
def greet():
    return "Brain Tumor MRI Image Classification Predictor"

@app.post("/predict")
async def predict(file: UploadFile = File(...), model_type: str = "custom"):
    if file.content_type not in ["image/jpeg", "image/png"]:
        return JSONResponse(status_code=400, content={"error": "Invalid file type"})
    
    result = await load_model_and_predict(file, model_type)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)