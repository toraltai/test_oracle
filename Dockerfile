FROM python:3 
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 
WORKDIR /code 
EXPOSE 8000
COPY req.txt /code/ 
RUN pip install -r req.txt 
COPY . /code/
