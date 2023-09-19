FROM python:3.10

ENV FLASK_APP=app.py
ENV DATABASE_URL=mysql://root:root@db:3306/practica01


WORKDIR /app

COPY . .

RUN pip install flask
RUN pip install jsonify
RUN pip install mysql-connector-python
RUN pip install flask-cors

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]