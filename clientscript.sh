#!/bin/bash

currenttime=$(date +%s)
time=$(curl -s http://127.0.0.1:5000/)
if [ $currenttime -ge $time ]; then 
	echo "greater" 
fi
