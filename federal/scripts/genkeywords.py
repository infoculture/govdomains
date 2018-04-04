#!/usr/bin/env python
import sys, os



f = open('../federal.txt', 'r')
uniq = []
for l in f:
    parts = l.split('.')
    for p in parts[:-1]:
        if p not in uniq:
            uniq.append(p)
            print(p)