FROM kalilinux/kali-rolling

run apt-get -qq update && apt-get install -qq xinetd 

copy launch_code /
run chmod 755 /launch_code

run touch /flag.txt && chmod 644 /flag.txt && echo "shctf{Every-cUb1c-1nch-0f-spAce-is-a-m1racl3}" > /flag.txt

copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

EXPOSE 31337/TCP

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]
