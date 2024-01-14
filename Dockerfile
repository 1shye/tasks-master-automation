FROM python:3.8-slim

WORKDIR /task_master

COPY . /task_master

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["pytest --html=/opt/report.html"]
