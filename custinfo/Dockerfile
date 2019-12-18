FROM python:latest

LABEL maintainer="Takahide Nogayama <nogayama@jp.ibm.com>"

# Install pip packages
RUN pip install Flask

EXPOSE 5000
WORKDIR /app

COPY app /app
CMD [ "python", "/app/app.py" ]
