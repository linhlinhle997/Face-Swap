from __future__ import unicode_literals
import youtube_dl
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--url", required=True, help='Input url video')
args = parser.parse_args()

def down() :
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		url = args.url
		ydl.download([url])
down()

