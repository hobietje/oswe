FROM python:3.9.1-buster AS python 

RUN apt-get update -y && apt-get install -y libmpc-dev

WORKDIR /workdir

COPY /app/requirements.txt /workdir
RUN pip3 install -r requirements.txt

COPY /app /workdir

ENTRYPOINT [ "python3" ]
CMD ["/workdir/change-rs256-to-hs256.py"]