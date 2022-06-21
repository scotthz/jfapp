FROM python:3

WORKDIR /

RUN pip install flask jinja2

COPY ./server.py /server.py

ENTRYPOINT [ "python3" ]

CMD [ "server.py" ]

