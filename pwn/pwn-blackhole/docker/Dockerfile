FROM kalilinux/kali-rolling

run apt-get -qq update && apt-get install -qq xinetd gcc libseccomp-dev

copy blackhole /
run chmod 755 /blackhole

run touch /flag.txt && chmod 644 /flag.txt && echo "shctf{1-hAs-4-$1ngul4riTy-coNtain3d-w1thin-a-r3g1on-oF-sp4c3}" > /flag.txt

copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

EXPOSE 31337/TCP

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
