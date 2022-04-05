#!/bin/bash

while [ true ]; do
	su -l luke -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'./force',pty,echo=0,raw,iexten=0 2> /dev/null"
done;
