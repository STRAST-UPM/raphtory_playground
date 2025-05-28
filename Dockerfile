FROM python:3.12.10-bookworm

WORKDIR /usr/src/raphtory_playground

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p "app"
COPY ./app/* ./app
RUN mkdir -p "graphs"
COPY ./graphs/* ./graphs

CMD [ "python", "./main.py" ]
