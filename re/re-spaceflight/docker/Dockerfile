from ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

run apt-get -qq update && apt-get install -qq xinetd 

copy spaceflight /
run chmod 755 /spaceflight

run touch /flag && chmod 644 /flag && echo "shctf{Th3-expl0Ration-oF-Spac3-wi11-go-ah3ad}" > /flag
 
run apt-get -qq update && apt-get install -qq xinetd 
 
# apt-get installs
RUN apt-get update -y
run apt-get -y install gcc build-essential cmake git libjson-c-dev libwebsockets-dev git gdb 
run git clone https://github.com/tsl0922/ttyd.git

# build ttyd (tool for hosting web app)
run mkdir /ttyd/build
run cd /ttyd/build/
workdir /ttyd/build
run cmake ..
run make
run make install
 
# expose ttyd (default port 7681)
EXPOSE 7681

# run ttyd at startup
WORKDIR /
CMD ["ttyd", "/spaceflight"]
