from fastapi.testclient import TestClient
from text_generator import app

client = TestClient(app)


def test_description():
    response = client.get("/description")
    assert response.status_code == 200
    assert response.json() == {
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


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_generate():
    passed_text = 'I love women'
    response = client.post('/predict/', json={'text': passed_text})
    assert response.status_code == 200
    assert passed_text in response.json()[0]['generated_text']


def test_team_info():
    response = client.get("/about-team")
    assert response.status_code == 200
    assert response.json() == {
        'name': 'Cobra Kai',
        'members': [
            { 'full_name': 'Danil Makushev', 'role': 'developer', 'img': '/image/Danil.jpg' },
            { 'full_name': 'Evgenia Prasolova', 'role': 'analyst', 'img': '/image/Evgenia.jpg' },
            { 'full_name': 'Semen Bakulin', 'role': 'developer', 'img': '/image/Semen.jpg' },
            { 'full_name': 'Denis Tryapitsyn', 'role': 'project manager', 'img': '/image/Denis.jpg' }
        ]
    }