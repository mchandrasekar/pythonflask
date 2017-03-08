#!/bin/bash

currenttime=$(date +%s)
time=$(curl -s http://192.168.99.100:5000/random)
if [ $currenttime -ge $time ]; then 
	echo "greater" 
elif [ $currenttime -le $time ]; then
	echo "lesser"
elif [ $currenttime -eq $time ]; then
	echo "equal"
fi
