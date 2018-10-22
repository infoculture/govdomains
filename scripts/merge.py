#!/usr/bin/env python
import sys, os

def merge_federal():
	out = open('../federal/full.txt', 'w')
	f = open('../federal/roots.txt')
	for l in f:
		out.write(l)
	f.close
	for name in os.listdir('../federal/lists'):
		f = open('../federal/lists/' + name)
		for l in f:
			out.write(l)
		f.close
	out.close()


def merge_regional():
	fullout = open('../regional/full.txt', 'w')
	dirs = os.listdir('../regional')
	for d in dirs:
		if not os.path.isdir('../regional/%s' % (d)): continue
		out = open('../regional/%s/full.txt' % (d), 'w')
		f = open('../regional/%s/roots.txt' % (d))
		for l in f:
			out.write(l.strip() + '\n')
			fullout.write(l.strip() + '\n')
		f.close
		try:
			lists = os.listdir('../regional/%s/lists' % (d))
		except FileNotFoundError:
			lists = []
		for name in lists:
			f = open('../regional/%s/lists/' % (d) + name)
			for l in f:
				out.write(l.strip() + '\n')
				fullout.write(l.strip() + '\n')
			f.close
		out.close()

	pass

def merge_all():
	os.system('cat ../federal/full.txt ../regional/full.txt > ../full.txt')
	pass


def run():
	merge_federal()
	merge_regional()
	merge_all()

if __name__ == "__main__":
	run()