FROM python:2.7
ADD . /code/web
WORKDIR /code/web
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]