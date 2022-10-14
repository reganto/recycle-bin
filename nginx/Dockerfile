FROM nginx:latest

COPY ./run.sh /run.sh
COPY ./default.conf /etc/nginx/conf.d

RUN mkdir -p /home/app/web/static && \
    chmod 755 /home/app/web/static && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x run.sh


VOLUME [ "/home/app/web/static" ]

CMD [ "./run.sh" ]