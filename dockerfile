FROM haproxy:alpine

COPY *.sh /
COPY *.py /

USER root
RUN mkdir -p /run/haproxy /var/lib/haproxy && \
    apk add --no-cache py3-pip bash

CMD /bootstrap.sh
