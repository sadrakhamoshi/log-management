# Log Management Using Nginx & Rsyslog

## Overview
This is a basic HTTP application created using FastAPI and Python. The application is hosted on NGINX, and its logs are forwarded to Rsyslog. Whenever an HTTP response with a 505 status code is detected by Rsyslog, it triggers an email notification to be sent to the user.

## Http Applicatioin
An simple HTTP application is Developed using FastAPI and Uvicorn that is currently running on port 8888. Check out the example folder for more information. To explore the available URLs, you can check out the example folder or visit `localhost/docs` for a complete list. (Note: `localhost/my_page_505` ***always*** returns status code `505`)

### Dockerize the Http APPlication
Write a Dockerfile to run the application on a container. To get more information check out `Dockerfile` for more information. 

## Reversed proxy using Nginx
To run the application on port 80, a `reverse proxy` is required in Nginx. To set this up, you need to create an Nginx configuration file and map all requests that come to **localhost:8888** to **localhost:80**. This can be achieved using the directive in the Nginx configuration. Check out `nginx/nginx.conf` for more information. 

### Dockerize the Nginx
To run nginx service on Docker we had to write a new Dockerfile in frist place. The Dockerfile can be found in `nginx/Dockerfile`. 

## Rsyslog
Rocket-fast syslog is a powerful open-source software used for log processing and management on Unix-like systems. In this example, a python script is configured to send an email notification to the admin user whenever a 505 status code is detected in an nginx log. This is achieved by setting up a tag for nginx logs in rsyslog and running the python script whenever a log with the nginx tag is generated, as detailed in the `nginx/rsyslog_nginx.conf` configuration file. The added script in `/etc/rsyslog.conf` run the python script as soon as nginx logs are generated:

```
module(load="omprog")

template(name="msg" type="list") {
    constant(value="Syslog MSG is: '")
    property(name="msg")
    }

if $programname == "nginx" then {

 action(type="omprog" binary="/usr/local/bin/python3 /manager/alert_manager.py")

}
```

### Dockerize
The Rsyslog is installed on the container of nginx and its configuration is set in `nginx/Dockerfile`.

## Docker-Compose
Finally, a `docker-compose.yml` is created to run two services on different container continuously.

## How to Run

### First you need to install [Docker](https://docs.docker.com/get-docker/) and [Docker-compose](https://docs.docker.com/compose/gettingstarted/).

### Second replace your Sender and Reciver eamils and APP_PASSWORD in `nginx/alert_manager.py`
``` python
sender_email = 'sender@gmail.com'
sender_password = 'APP_PASSWORD'
receiver_email = 'reciver@example.com'
```

### Finally

- Clone the repository

    ```shell script
    $ git clone https://github.com/sadrakhamoshi/log_management.git
    ```
- Run server on your localhost
    
    ```shell script
    $ docker-compose -f docker-compose.dev.yml up -d --build
    ```
