from fastapi import FastAPI
from transformers import pipeline, set_seed
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_302_FOUND

set_seed(42)


class Item(BaseModel):
    text: str


app = FastAPI()
generator = pipeline('text-generation', model='gpt2')


@app.get("/")
def root():
    return RedirectResponse(url="/client/index.html",
                            status_code=HTTP_302_FOUND)


@app.get("/description/")
def description():
    message = {
        'header': 'This project is built around gpt2 model',
        'body': [
            {'type': 'text_field',
             'text': 'gpt2 is text generator model'},
            {'type': 'text_field',
             'text': 'This model was loaded from Hugging face hub'},
            {'type': 'text_field',
             'text': 'To test model use method `predict`'},
            {'type': 'text_field',
             'text': '`predict` requires body with single keyword(=text)'},
            {'type': 'text_field',
             'text': '`predict` returns generated text by gpt2 model'}
        ]
    }
    return message


@app.post("/predict/")
def predict(item: Item):
    return generator(item.text, max_length=40, num_return_sequences=1)


@app.get('/about-team')
async def team_info():
    return {
        'name': 'Cobra Kai',
        'members': [
            { 'full_name': 'Danil Makushev', 'role': 'main developer' },
            { 'full_name': 'Evgenia Prasolova', 'role': 'analyst' },
            { 'full_name': 'Semen Bakulin', 'role': 'secondary developer' },
            { 'full_name': 'Denis Tryapitsyn', 'role': 'project manager' }
        ]
    }


app.mount("/client",
          StaticFiles(directory="text_generator_client"),
          name="client")
