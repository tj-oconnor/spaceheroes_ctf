FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install Flask

WORKDIR /root
EXPOSE 5000
ADD app.py /root
ADD flag.txt /root
COPY /static /root/static
COPY /templates /root/templates
ADD /serve.sh /root
ENTRYPOINT "/root/serve.sh"
