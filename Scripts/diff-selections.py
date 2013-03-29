#!/usr/bin/python

import sys, os, os.path, subprocess

sugarPath = os.environ['EDITOR_SUGAR_PATH']

# Ensure that we have ksdiff available
if not os.path.exists('/usr/local/bin/ksdiff'):
	indexFile = open(os.path.join(sugarPath, 'Contents/Resources/help/index.html'), 'r')
	sys.stdout.write(indexFile.read())
else:
	# Grab our files, and toss them over to ksdiff
	selections = sys.stdin.read().splitlines()
	command = '/usr/local/bin/ksdiff'
	for path in selections:
		# To avoid complicated shell script escaping, we just use single quotes
		command += " '" + path.replace("'", "'\\''") + "'"
	status = subprocess.call(command, shell=True)
