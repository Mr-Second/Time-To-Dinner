#!/usr/bin/env python3
# -*- coding: utf-8 -*
import json
try:
	with open('gomaji.json', 'r', encoding='UTF-8') as f:
	    json.load(f)
except Exception as e:
	raise e
	print(e)