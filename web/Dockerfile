FROM python:latest

LABEL maintainer="Takahide Nogayama <nogayama@jp.ibm.com>"

# Install pip packages
RUN pip install Flask


WORKDIR /app

COPY app /app
CMD [ "python", "/app/app.py" ]
