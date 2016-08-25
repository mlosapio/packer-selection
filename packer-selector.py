#!/usr/bin/python

import urllib
import lxml.html

URL = 'https://releases.hashicorp.com/packer/'


def get_latest():
	""" Return the latest release """
	releases = []
	connection = urllib.urlopen('URL')
	dom = lxml.html.fromstring(connection.read())
	for line in dom.xpath('//a/@href'):
		releases.append(line.split("/")[2])
	releases.sort()
	return releases[0]

def main():
	release = get_latest()
	print release

if __name__ == "__main__":
	main()

