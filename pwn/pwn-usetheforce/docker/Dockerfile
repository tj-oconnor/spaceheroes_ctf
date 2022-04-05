FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y gcc socat

# Add in our starting bash script
WORKDIR /
RUN useradd -m luke
COPY start.sh /start.sh
RUN chmod 755 /start.sh

# Add user, flag, and permissions on flag
COPY flag.txt /home/luke/flag.txt
RUN chown root:root /home/luke/flag.txt
RUN chmod 644 /home/luke/flag.txt


# Copy files and make executable
COPY force/. /home/luke
RUN chmod +x /home/luke/force

RUN rm -f /bin/sed
# Expose port (DONT FORGET TO MAP) and run
#WORKDIR /
EXPOSE 9000
CMD ["./start.sh"]
