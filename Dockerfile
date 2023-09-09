FROM python:3.8-slim

WORKDIR /DangerousPickle

RUN touch /tmp/flag.txt

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ../PycharmProjects/DangerousPickle .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]