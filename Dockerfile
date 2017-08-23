FROM python:alpine

MAINTAINER rmrbest@gmail.com

WORKDIR /src

COPY src /src/
COPY requirements.txt /src
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/src/server.py"]