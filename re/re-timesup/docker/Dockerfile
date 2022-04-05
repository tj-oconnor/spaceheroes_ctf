FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN apt-get update -y && apt-get -y install xinetd socat --fix-missing

# unset the library path so you can force loading
RUN unset LD_LIBRARY_PATH

copy timesup /
run chmod 755 /timesup

run touch /flag.txt && chmod 644 /flag.txt && echo "shctf{b3yond_the_c0rridor_of_R_space_t1me}" > /flag.txt

EXPOSE 12345/tcp

CMD socat TCP-LISTEN:12345,reuseaddr,fork EXEC:"/timesup"



