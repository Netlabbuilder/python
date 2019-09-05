#!/usr/bin/env python3.6

#This script, running on CentOS - Linux, is to verify the reachability of an IP address using 'subprocess' with 'ping -c2 -W2' command

from flask import Flask, render_template
import subprocess

app = Flask(__name__)

#########
### 1 ###
#########

@app.route('/')
@app.route('/online/')

def index():
	return render_template('reachability_ping_homepage.html')


#########
### 2 ###
#########

@app.route('/online/<ip_address>')

def switch(ip_address):
	ping_result = subprocess.run(['ping', '-c', '2','-W','2', ip_address], encoding='utf-8',stdout=subprocess.PIPE)

	if ping_result.returncode == 0:
		web_output = '<h1> <center> {} is <font color="green"> reachable - up </font> </center> </h1>'.format(ip_address)
	else:
		web_output = '<h1> <center> {} is <font color="red"> unreachable - down </font> </center> </h1>'.format(ip_address)

	return web_output

#########
### 3 ###
#########

app.run()
