FROM golang:1.18

WORKDIR /demo_app

RUN apt-get update

COPY ./app ./app

CMD cd app/main && go test -bench=. -benchtime=10000x -benchmem -host server