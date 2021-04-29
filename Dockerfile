from python:3.8-alpine

# Add scripts to the running container
ENV PATH="/scripts:${PATH}"

# Copy requirements.txt to the Docker image
COPY ./requirements.txt /requirements.txt

# Required Alpine packages to install uWSGI
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

RUN pip install -r /requirements.txt

# Remove the temporary files
RUN apk del .tmp

RUN mkdir /app
COPY ./app /app
WORKDIR /app

COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]

