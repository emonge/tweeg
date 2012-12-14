#!/usr/bin/env python

# Tweeg v0.0.1 -- Un primitivo, feo y sucio script en Python que utiliza
# la informacion de Rhythmbox y la envia a Twitter en forma de tweet
#
# Copyright (c) 2012 Enrique Monge - emonge AT debian.org.sv
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation version 2 of the License.
# 
# On Debian GNU/Linux systems, the complete text of the GNU General Public
# License, version 2 can be found in `/usr/share/common-licenses/GPL-2'.

import os, sys
import twitter

consumer_key='SUPROPIACONSUMERKEY'
consumer_secret='SUPROPIACONSUMERSECRET'
access_token_key='SUTOKEN'
access_token_secret='SUTOKENSECRET'
api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)
checkcommand = 'ps aux | grep rhythmbox | wc -l'
command = 'rhythmbox-client --no-start --no-present --print-playing-format "%tt / %ta"'
prefix = "#NowPlaying > "

check=os.popen(checkcommand)
for checknum in check.readlines():
	checkind = checknum.strip("\n")

if int(checkind) > 2:
	f=os.popen(command)
	for song in f.readlines():
		 if len(sys.argv)==2:
			 comment = sys.argv[1]
			 separator = " | "
			 tweet = prefix+song+separator+comment
			 tweet = tweet.strip("\n")
		 else:
			 tweet = prefix+song
			 tweet = tweet.strip("\n")		 
		 if len(tweet) > 140:
			 ltweet = str(len(tweet))
			 print "This tweet exceeds the allowable lenght: "+ltweet+ " characters. Let's tweet again!"
		 else:
			 status = api.PostUpdate(tweet)
			 print tweet
else:
	print "Rhythmbox is not running!"
