ARG BUILD_FROM
FROM $BUILD_FROM

# Add env
ENV LANG C.UTF-8

# Setup base
RUN apk add --no-cache jq python py-pip
RUN pip install paho-mqtt

# Copy data
COPY run.sh /
COPY ownserver.py /bin 

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
