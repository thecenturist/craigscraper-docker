FROM alpine:3.14
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
WORKDIR /app
COPY main.py requirements.txt usa_urls.txt ./
RUN mkdir output
RUN pip3 install -r requirements.txt
CMD python main.py
