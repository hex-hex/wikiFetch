#!/usr/bin/env bash
export WIKI_REPORT_DOWN=~/Downloads/
nohup gunicorn  -k gevent --workers=2 --threads=2 --bind 0.0.0.0:5000 fetchWikiReport:app > ~/fetchWiki.log