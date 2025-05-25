FROM alpine:latest

RUN apk update && apk add --no-cache python3 py3-pip iputils grep

WORKDIR /app

COPY 03_practice.py .

CMD [ "python3" , "03_practice.py" ]