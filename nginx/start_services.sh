#!/bin/bash

# Start the Rsyslog service
service rsyslog start

# Start the Nginx service
nginx -g "daemon off;"