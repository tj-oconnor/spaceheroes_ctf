#!/bin/bash
unzip chall.zip
cd img
tar --create --file=a.tar master0-3.qcow2  master0-4.qcow2
strings a.tar | grep "shctf{"
cd ..
rm -rf img

