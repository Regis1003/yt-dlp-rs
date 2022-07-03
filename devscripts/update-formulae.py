#!/usr/bin/env python3

# Allow direct execution
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import json
import re
import urllib.request

# usage: python3 ./devscripts/update-formulae.py <path-to-formulae-rb> <version>
# version can be either 0-aligned (yt-dlp version) or normalized (PyPl version)

filename, version = sys.argv[1:]

normalized_version = '.'.join(str(int(x)) for x in version.split('.'))

pypi_release = json.loads(urllib.request.urlopen(
    'https://pypi.org/pypi/yt-dlp/%s/json' % normalized_version
).read().decode())

tarball_file = next(x for x in pypi_release['urls'] if x['filename'].endswith('.tar.gz'))

sha256sum = tarball_file['digests']['sha256']
url = tarball_file['url']

with open(filename) as r:
    formulae_text = r.read()

formulae_text = re.sub(r'sha256 "[0-9a-f]*?"', 'sha256 "%s"' % sha256sum, formulae_text, count=1)
formulae_text = re.sub(r'url "[^"]*?"', 'url "%s"' % url, formulae_text, count=1)

with open(filename, 'w') as w:
    w.write(formulae_text)