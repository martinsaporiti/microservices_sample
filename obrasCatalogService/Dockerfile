FROM python:3

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./usr/src/app

# ENTRYPOINT [ "python" ]

CMD [ "python", "./usr/src/app/app.py" ]
