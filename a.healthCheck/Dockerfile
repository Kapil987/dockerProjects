FROM httpd
LABEL Kapil Kapil
RUN apt-get update && apt-get install wget curl; wget https://raw.githubusercontent.com/Kapil987/min_proj/master/src/main/webapp/index.jsp -O /usr/local/apache2/htdocs/index.html
HEALTHCHECK --interval=5s --timeout=20s --retries=2 CMD curl --fail http://localhost:80 || exit 1