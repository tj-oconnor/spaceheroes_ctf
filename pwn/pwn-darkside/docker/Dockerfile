FROM kalilinux/kali-rolling

run apt-get -qq update && apt-get install -qq xinetd gcc libseccomp-dev

copy darkside /
run chmod 755 /darkside

copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

EXPOSE 31337/TCP

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
