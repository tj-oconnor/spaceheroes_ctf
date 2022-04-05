FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y gcc socat

# Add in our starting bash script
WORKDIR /
RUN useradd -m ctf
COPY start.sh /start.sh
RUN chmod 755 /start.sh

# Add user, flag, and permissions on flag
COPY flag.txt /home/ctf/flag.txt
RUN chown root:root /home/ctf/flag.txt
RUN chmod 644 /home/ctf/flag.txt


# Copy files and make executable
COPY ./guardians /home/ctf
RUN chmod +x /home/ctf/guardians

# Expose port (DONT FORGET TO MAP) and run
EXPOSE 9000
CMD ["./start.sh"]
