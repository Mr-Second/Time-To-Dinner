#!/usr/bin/env python3
# -*- coding: utf-8 -*
import json, pickle
try:
	with open('test.json', 'r', encoding='UTF-8') as f:
		json.load(f)
	with open('ResTable.pickle', 'rb') as f:
		p = pickle.load(f)
		print(len(p))
except Exception as e:
	raise e
	print(e)