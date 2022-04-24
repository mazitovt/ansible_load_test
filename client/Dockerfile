FROM golang:1.18

WORKDIR /demo_app

COPY ./app ./app

RUN apt-get update
RUN cd app && chmod +x ./rip

# TODO: -host should be server name or ip

# CMD cd app/main && go test -bench=. -benchtime=1000x -benchmem -host server
# CMD cd app && go test -bench=. -benchtime=1000x -benchmem -host server
# CMD cd app && chmod +x ./rip