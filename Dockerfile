FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN python -m venv venv
RUN . venv/bin/activate && pip install -r requirements.txt

CMD ["venv/bin/flask", "run", "--host=0.0.0.0"]
