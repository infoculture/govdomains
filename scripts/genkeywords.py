#!/usr/bin/env python


f = open('../full.txt', 'r')
uniq = []
for l in f:
    parts = l.split('.')
    for p in parts[:-1]:
        if p not in uniq:
            uniq.append(p)
            print(p)
