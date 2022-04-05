FROM kalilinux/kali-rolling

run apt-get -qq update && apt-get install -qq xinetd python3 

copy RahoolsChallenge.py /
run chmod 755 /RahoolsChallenge.py

copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

expose 31337

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
