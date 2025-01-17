FROM python:3.9

COPY . /flask-app/

WORKDIR /flask-app

RUN pip install -r requirements.txt

CMD [ "bash" ]

# CMD [ "python", "app.py"]