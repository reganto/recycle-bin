FROM nginx:latest

COPY ./run.sh /run.sh
COPY ./default.conf /etc/nginx/conf.d

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x run.sh


VOLUME [ "/vol/static" ]

CMD [ "./run.sh" ]