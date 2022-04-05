FROM kalilinux/kali-rolling

run apt-get -qq update && apt-get install -qq xinetd gcc libseccomp-dev

copy pwn-rocket /
run chmod 755 /pwn-rocket

run touch /flag.txt && chmod 644 /flag.txt && echo "shctf{1-sma11-St3p-f0r-mAn-1-Giant-l3ap-f0r-manK1nd}" > /flag.txt

copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

EXPOSE 31337/TCP

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
