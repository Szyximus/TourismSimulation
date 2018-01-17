FROM python:3.6-alpine
COPY requirements.txt /tmp/
RUN pip install numpy
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/
ENTRYPOINT ["./tmp/launch.sh"]