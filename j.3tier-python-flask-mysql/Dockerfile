FROM python:3.10-slim
LABEL Maintainer="Kapil a devops engineer from india"
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
