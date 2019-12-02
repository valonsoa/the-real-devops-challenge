FROM python:3
 ADD app.py /
 ADD tests /tests
 ADD src /src
 RUN pip install pymongo flask flask_pymongo isodate
 EXPOSE 8080
 CMD ["python", "./app.py"]