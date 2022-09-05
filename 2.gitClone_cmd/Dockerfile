FROM amazonlinux
RUN yum install update httpd git -y && \
    mkdir /root/.ssh

# For ease place private key in current dir
#COPY ./httpd.conf /etc/httpd/conf/
COPY ./id_rsa /root/.ssh/id_rsa
RUN chmod -R 700 /root/.ssh && \
    chown -R root:root /root/.ssh && \
    chmod 600 /root/.ssh/id_rsa && \
# ssh-keysacn is used to avoid prompt to add host in known_hosts file
    ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts && \
    git clone git@bitbucket.org:kapilhsr/html-web-app.git /var/www/html/
CMD ["/usr/sbin/httpd","-D", "FOREGROUND"]


# FROM amazonlinux
# RUN yum install update httpd git -y && \
#     mkdir /root/.ssh
# ARG ssh_prv_key
# RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
#     chmod -R 700 /root/.ssh && \
#     chown -R root:root /root/.ssh && \
#     chmod 600 /root/.ssh/id_rsa && \
#     ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts && \
#     git clone git@bitbucket.org:kapilhsr/html-web-app.git /var/www/html/ 
# CMD ["/usr/sbin/httpd","-D", "FOREGROUND"]

## More Info
## docker build -t apache --build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa)" --squash .
## --squash is experimental
## sed -i 's/#ServerName www.example.com:80/ServerName 127.0.0.1:80/' /usr/local/apache2/conf/httpd.conf
