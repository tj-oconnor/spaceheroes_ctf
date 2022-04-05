FROM kalilinux/kali-rolling

run apt-get -qq update && apt-get install -qq xinetd gcc 

copy satisfy /
run chmod 755 /satisfy

run touch /flag.txt && chmod 644 /flag.txt && echo "shctf{Whos-Th3-k1ng-of-Ur-Sat3ll1te-Castl3}" > /flag.txt

copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

EXPOSE 31337/TCP

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
