#!/usr/bin/env python

import urllib, re

links = open('links.txt', 'r').readlines()

count = len(links)
line = 0

database = open('data.txt', 'w')

while line < count:

	url = links[line]
	www = urllib.urlopen(url) 
	www_tekst = www.read()

	html = '<span class="number">.</span>.............:<br />\d\d:\d\d<br />.............:<br />\d\d:\d\d</td>|<span class="number">..</span>.............:<br />\d\d:\d\d<br />.............:<br />\d\d:\d\d</td>'
	text = re.findall(html, www_tekst)

	numbers = []
	sunrises = []
	sunsets = []

	
	time = '\d\d:\d\d'
	i = 0
	for marker in text:
		i = i + 1
		times = re.findall(time, marker)
		numbers.append(i)
		sunrises.append(times[0])
		sunsets.append(times[1])

	counter = 0
	while counter < i:
		database.write(str(numbers[counter]) + ' ' + sunrises[counter] + ' ' + sunsets[counter] + '\n')
		counter = counter + 1

	line = line + 1

database.close()

