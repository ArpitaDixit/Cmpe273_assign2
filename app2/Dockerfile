FROM python:2.7
MAINTAINER Anshul Agrawal "anshul.dec7@gmail.com"
ADD . /code/web
WORKDIR /code/web
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]