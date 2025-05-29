FROM python:3.12.10-bookworm

WORKDIR /usr/src/graphql_server

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p "graphs"
COPY ./server ./server

WORKDIR /usr/src/graphql_server/server
CMD [ "python", "main.py" ]
