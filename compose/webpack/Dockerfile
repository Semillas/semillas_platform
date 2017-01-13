# docker.webpack

FROM ubuntu:latest

WORKDIR /app
COPY . /app

RUN apt-get update
RUN apt-get install curl -y
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install nodejs -y
RUN npm install webpack -g
RUN npm install
CMD webpack --config webpack.config.js --watch --watch-poll
