from flask import Flask, request, jsonify
import requests
import os
import tester
from tester import Scraper
from rq import Queue
from rq.job import Job
from red import conn


# Initialize App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
q = Queue(connection=conn)

# Run Downloader
@app.route('/run')
def run():
    job = q.enqueue(tester.run)
    print(job.get_id())
    return 'OK'

@app.route('/run2')
def run_stack():
    job = q.enqueue(Scraper().getStackOverflow)
    print(job.get_id())
    return 'OK'

@app.route('/run3')
def run_TA():
    job = q.enqueue(Scraper().getGithub)
    print(job.get_id())
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
