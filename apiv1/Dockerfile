FROM python:latest

LABEL maintainer="Takahide Nogayama <nogayama@jp.ibm.com>"

# Install pip packages
RUN pip install Flask
RUN apt-get update && apt-get install vim -y

WORKDIR /app
EXPOSE 8080

COPY app /app
CMD [ "python", "/app/app.py" ]
