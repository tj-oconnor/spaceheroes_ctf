FROM kalilinux/kali-rolling

run apt-get -qq update && apt-get install -qq xinetd gcc libseccomp-dev && apt-get -y install dpkg && apt-get -qq update && dpkg --add-architecture i386 && apt-get -qq update
run apt-get install -qq libc6:i386 libstdc++6:i386 libncurses5:i386 zlib1g:i386
copy leet /
run chmod 755 /leet

run touch /flag.txt && chmod 644 /flag.txt && echo "shctf{Y00_175_70NY_574RK}" > /flag.txt

copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

EXPOSE 1337/TCP

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
