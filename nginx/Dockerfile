FROM python:3.8-slim-buster

# Install Nginx and Rsyslog
RUN apt-get update && \
    apt-get install -y nginx nano rsyslog


# config nginx
# RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/

EXPOSE 80

# alert_manager the files
RUN mkdir /manager
COPY alert_manager.py /manager/

# add permisson to execution
RUN chmod ugo+rwx /manager/alert_manager.py

# Copy config nginx_rsyslog to rsyslog.d/
COPY rsyslog_nginx.conf /etc/rsyslog.d/

# Edit /etc/rsyslog.conf
RUN sed -i '/imklog/s/^/#/' /etc/rsyslog.conf
RUN sed -i '1i $ModLoad imfile' /etc/rsyslog.conf
COPY tmp.txt .
RUN echo "$(cat tmp.txt)" >> /etc/rsyslog.conf 

# RUN service rsyslog restart
COPY start_services.sh .

# Start services
CMD ["./start_services.sh"]