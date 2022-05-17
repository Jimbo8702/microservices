FROM python:3.10 
ENV PYTHONUNBUFFERED 1
WORKDIR /app-flask
COPY requirements.txt /app-flask/requirements.txt
RUN pip install -r requirements.txt
COPY . /app-flask

CMD python main.py







