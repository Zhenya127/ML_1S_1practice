FROM python:3.9-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements_api.txt
EXPOSE 8000
CMD ["uvicorn", "text_generator:app"]