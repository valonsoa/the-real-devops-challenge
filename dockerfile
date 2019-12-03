FROM python:3
 COPY app.py /
 COPY tests /tests
 COPY src /src
 RUN pip install pymongo flask flask_pymongo isodate
 EXPOSE 8080
 CMD ["python", "./app.py"]