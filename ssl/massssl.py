#!/usr/bin/env python
# -*- coding utf8 -*-
import sys
import os
import json
#from xmlr import xmliter

def run(filename):
	f = open(filename, 'r')
	for l in f:
		parts = l.split(',')
		domain = parts[0].strip()
		if len(l) > 0 and l[0] != '#':
			if os.path.exists('results\\%s.xml' % domain): 
				continue
			os.system('sslscan --show-certificate --http --xml=results\\%s.xml %s' % (domain, domain))

if __name__ == '__main__':
	run(sys.argv[1])