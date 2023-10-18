from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from model.config import Config
import uvicorn
from model.schema.symptom import SymptomScheme
from utils import predict

app = FastAPI()
config = Config.load()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["POST"],  
    allow_headers=[
        "Content-Type",  
        "Authorization"],  
)


@app.post("/symptoscan/")
def say_hello(request: Request, symptom: SymptomScheme):
    prediction = predict(config, symptom.dict())
    print(prediction)
    return {
        "disease":prediction[0],
        "confidence":prediction[1]
    }


if __name__=="__main__":
    uvicorn.run("main:app",host='0.0.0.0',port=4557,reload=True,workers=3)