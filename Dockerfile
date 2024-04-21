FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN flask sqlitebp init-db

CMD [ "python3", "-m" , "flask", "run",  "--host=0.0.0.0"]