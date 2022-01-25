#!/usr/bin/env python3

import operator
import re

logFilePath = 'lb.log'
# Credit to ticky's regex repo and geoffcallendar's comment:  https://gist.github.com/ticky/3909462
regex = "(MSIE|Trident|(?!Gecko.+)Firefox|(?!AppleWebKit.+Chrome.+)Safari(?!.+Edge)|(?!AppleWebKit.+)Chrome(?!.+Edge)|(?!AppleWebKit.+Chrome.+Safari.+)Edge|AppleWebKit(?!.+Chrome|.+Safari)|Gecko(?!.+Firefox))(?: |\/)([\d\.apre]+)"
matchList = []

def main():
	file = open(logFilePath)
	lines = file.readlines()
	# count = 0
	for line in lines:
		for match in re.finditer(regex, line, re.S):
			matchText = match.group()
			matchList.append(matchText)
	# Initialize dictionary to store frequency of browsers/versions
	browserCount = {}
	for browserVersion in matchList:
		if browserVersion in browserCount:
			browserCount[browserVersion] += 1
		else:
			browserCount[browserVersion] = 1
	sortedBrowserCount = sorted(browserCount.items(), key=operator.itemgetter(1), reverse=True)
	# printing the elements frequencies
	print("==========================\nBrowser/Version: Frequency\n==========================")
	for key, value in sortedBrowserCount:
		print(f"{key}: {value}")
  
main()