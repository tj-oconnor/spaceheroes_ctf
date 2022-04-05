# declare distro and timezone
FROM ubuntu:20.04
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install software for restricted user
RUN apt-get update 
RUN apt-get install -y openssh-server 

# add a restricted user 
RUN useradd -rm -d /home/hawking -s /bin/rbash hawking
RUN echo 'hawking:stephenhawkingisprettycooleh' | chpasswd
RUN echo 'shctf{1nf0rm4ti0n_c4nn0t_b3_d3str0y3d}' >> /home/hawking/flag.txt
RUN mkdir /home/hawking/.ssh
RUN echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDKItoETdZP9Oa7egogP76VsiEQQ1kPb5F8e63DlLqh1PDXQti4cksYCzaGMWWDfUic2vNaMDyYrXVopOxa0bo505T42Kfu9Sz3Xx5xrZojOhOOcvxPmiGTMe/Ng6fUFFnogh5N+CYA3qXceyIzEfgANU+lfGgK0kkDXyqEIEa/4pwOiztKov8QaDtRKbPFIQYMUTy8W4lhlkRnKALfLheEN6vC1StYMlsQ4qnZXJ5do/bL+OQCbesbmCkR3gdYiGwKs2XtmSP1QKP8Ff8OBuERiRJM8oOVnplcg+iQPvUWy6iX9htCwtMFOqijt+pL09tYEM4wQyB9GOw5hWzavfsDWGwfDx2zPorW+iCz7M7D8uL6OFkYDDY/+KHsD5AspTaH9AIUu3IjHij3IVh/A2JdTglynwuG0qQZPiCCotc8lT8NKn8Woroyfb8XPySIICC0g/L/hHCTXH0jd92j8CsbR2YdDd76vGLj1ThEe8hx/F3HEocDc3v02CE6sHBZMfCODxux5a0CEejm2+TsuM1c7kYrusivXV+OzNpaTioAR1n8UxIfMm3TNK3sLmT/1ooyuLLjCRLYB6/zoy1KIAIVIxN3y/9JZn94kKS5Q8AGTMrG4L3yt4bcRCf6Zf/Asv17WmJYY3DP7RKVHF/dYg06SFgbm/2kTYOYLXnNxo2hwQ==' >> /home/hawking/.ssh/authorized_keys

# enable ssh server for access
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]