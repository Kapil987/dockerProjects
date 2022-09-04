# alpine avoided as useradd, groupadd etc command were not there
FROM tomcat:8.0
LABEL maintainer="Kapil"

# uid and gid are used here to  match host user , to avoid mismatch incase of volume mount, 
# ARG can be given at building you image using --> 
# sudo docker build -t user_tom --build-arg USER_ID=$(id -u ${USER}) --build-arg GROUP_ID=$(id -u ${GROUP_ID}) --build-arg USER_NAME=$(id -nu ${USER_ID}) .
ARG USER_ID
ARG GROUP_ID
ARG USER_NAME

RUN rm -rf /usr/local/tomcat/webapps/*
# if the below mkdir command is ran the ownership is granted to root unless you chown it and then if tempfs is created on the same,
# then you will get permission denied error as root has the ownership, 
# workaround for this problem is to use uid in tmpfs  --tmpfs=/usr/local/tomcat/logs:uid=1000:1000 at runtime
# mkdir -p /usr/local/tomcat/logs 

# you may plan to use exec in place of noexec to provide execution permission in the tempfs
# docker run --read-only -d --rm --name test_tom -p 8081:8080 --tmpfs /usr/local/tomcat/logs:uid=1000,gid=1000,rw,noexec,nosuid,nodev,size=4m user_tom


COPY ./demo.war /usr/local/tomcat/webapps/
COPY ./index.html /usr/local/tomcat/webapps/ROOT/

# Not a good practice but you can comment/uncomment giving root password to check/demonstrate --security-opt no-new-privileges option working
# if you pick a uid+gid combination that doesn’t exist in the base image, the runtime user will only have access to files that everyone has access to

# RUN echo "root:root" | chpasswd &&\ 
RUN groupadd -g ${GROUP_ID} ${USER_NAME} &&\
useradd -l -u ${USER_ID} ${USER_NAME} -g ${GROUP_ID} &&\
chsh --shell /usr/sbin/nologin root
RUN chown --changes --silent --no-dereference --recursive ${USER_ID}:${GROUP_ID} /usr/local/tomcat/webapps \
/usr/local/tomcat/logs \
/usr/local/tomcat/work

# at this point even though USER is created but this will still create folder with root ownership
# mkdir -p /usr/local/tomcat/testing

# optional you may choose this at runtime, even with --read-only USER is able to write into this folder
# if the below is commented and --read-only flag is used then it the dir becomes read only (no modification allowed)
# VOLUME /usr/local/tomcat/webapps 

# default user will used for login
USER ${USER_NAME}

# optional may be specified at run time
EXPOSE 8080
