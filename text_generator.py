from fastapi import FastAPI
from transformers import pipeline, set_seed
from pydantic import BaseModel

set_seed(42)
class Item(BaseModel):
    text: str

app = FastAPI()
generator = pipeline('text-generation', model='gpt2')

@app.get("/")
def root():
    return {"message": "API application for text generator"}

@app.post("/predict/")
def predict(item: Item):
    return generator(item.text, max_length=40, num_return_sequences=3)