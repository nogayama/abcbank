# -*- coding: utf-8 -*-

# =================================================================
# Licensed Materials - Property of IBM
#
# (c) Copyright IBM Corp. 2019, 2019 All Rights Reserved
#
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
# =================================================================

FROM python:3.7.4

LABEL maintainer="Takahide Nogayama <nogayama@jp.ibm.com>"

# Install pip packages
RUN pip install Flask

EXPOSE 5000
WORKDIR /app

COPY app /app
CMD [ "python", "/app/app.py" ]
