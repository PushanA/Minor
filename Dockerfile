FROM python:3.7
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
#Open port 5000
EXPOSE 5000
ENV NAME OpentoAll
CMD ["python", "app.py"]
