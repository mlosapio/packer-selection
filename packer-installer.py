#!/usr/bin/python
""" Basic file to pull down latest packer and save to /tmp/ """

import urllib
import lxml.html
import zipfile
import os

URL = 'https://releases.hashicorp.com/packer/'
BASE_PATH = 'packer'

def get_latest():
	""" Return the latest release """
	releases = []
	connection = urllib.urlopen(URL)
	dom = lxml.html.fromstring(connection.read())
	for line in dom.xpath('//a/@href'):
		if BASE_PATH in line:
			# Ignore release candidates
			if 'rc' not in line:
				releases.append(line.split("/")[2])
	releases.sort(key=lambda s: map(int, s.split('.')))
	return releases[-1]

def download_file(release):
	""" Takes the release and downloads the latest """
	print "Downloading file"
	packer_tgz = urllib.URLopener()
	packer_tgz.retrieve(URL + release + '/packer_' + release + '_linux_amd64.zip', "/tmp/packer.zip")

def extract_and_copy():
	""" Takes /tmp/packer.zip and puts the binary in /usr/local/bin """
	filehandle = open('/tmp/packer.zip', 'rb')
	zip = zipfile.ZipFile(filehandle)
	for name in zip.namelist():
		print "Extracting %s" % name
		outpath = "/usr/local/bin/"
		zip.extract(name, outpath)
		os.chmod(outpath + name, 555)
	filehandle.close()

def main():
	release = get_latest()
        print "latest release returned as %s" % release
	download_file(release)
	extract_and_copy()

if __name__ == "__main__":
	main()
