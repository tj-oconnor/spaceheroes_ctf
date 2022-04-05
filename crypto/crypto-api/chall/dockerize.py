import os
import sys


def main():
    name = sys.argv[1]
    with open("serve.sh", "w") as f:
        f.write(f"""#! /bin/sh
cd /root; python3 app.py""")
    os.system("chmod +x serve.sh")
    os.system(f"touch {name}")
    with open("Dockerfile", "w") as f:
        f.write(f"""FROM ubuntu:20.04
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
""")
    os.system(
        f"""sudo docker build -t {name} . ;sudo docker login -u '{"frootsalad@spaceheroes.ctfd.io"}' ; sudo docker tag {name} registry.ctfd.io/spaceheroes/{name}; sudo docker push registry.ctfd.io/spaceheroes/{name}""")

main()
