FROM alpine:latest

RUN \
  apk add --update python && \
  rm -rf /var/cache/apk/*

ADD . ./
EXPOSE 3000/udp
ENTRYPOINT ["python", "udp_server.py"]
