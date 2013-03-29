#!/usr/bin/python

import sys, os, os.path, subprocess, tempfile

sugarPath = os.environ['EDITOR_SUGAR_PATH']

# Ensure that we have ksdiff available
if not os.path.exists('/usr/local/bin/ksdiff'):
	indexFile = open(os.path.join(sugarPath, 'Contents/Resources/help/index.html'), 'r')
	sys.stdout.write(indexFile.read())
else:
	# Grab our clipboard contents
	p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
	retcode = p.wait()
	clipboard = p.stdout.read()
	# Write our clipboard contents to a temporary file
	file = tempfile.NamedTemporaryFile()
	file.write(clipboard)
	# Grab our file, and toss it and the temp file over to ksdiff
	selection = sys.stdin.read()
	# To avoid complicated shell script escaping, we just use single quotes
	command = "/usr/local/bin/ksdiff '" + selection.replace("'", "'\\''") + "' '" + file.name.replace("'", "'\\''") + "'"
	status = subprocess.call(command, shell=True)
	file.close()
