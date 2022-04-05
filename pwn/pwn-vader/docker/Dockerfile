FROM kalilinux/kali-rolling

run apt-get -qq update && apt-get install -qq xinetd gcc

copy vader /
run chmod 755 /vader

run touch /flag.txt && chmod 644 /flag.txt && echo "shctf{th3r3-1s-n0-try}" > /flag.txt
run touch /sith.txt && chmod 644 /sith.txt && echo "shctf{W1th0ut-str1f3-ur-v1ctory-has-no-m3an1ng}" > /sith.txt
 
copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

EXPOSE 31337/TCP

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
