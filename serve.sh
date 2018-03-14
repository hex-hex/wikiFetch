#!/usr/bin/env bash
nohup gunicorn  -k gevent --workers=2 --threads=2 --bind 0.0.0.0:5000 fetchWikiReport:app > ~/fetchWiki.log