#!/usr/bin/python 
# -*- coding: utf-8 -*- 
import fileinput 
import math 

def comb(n, r):
  return math.factorial(n) / (math.factorial(n - r) * math.factorial(r))
# メイン処理 
for line in fileinput.input():
  line = line.replace('\n', '')
  line = line.replace('\r', '')
  s = line.split(",")
  runner = int(s[0])
  hook = int(s[1])
  if runner > 3 and runner > hook:
    print(comb(hook - 1, runner - hook))
  else:
    print(0)