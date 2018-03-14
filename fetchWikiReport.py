import datetime

import requests
from flask import Flask, render_template, request

app = Flask(__name__)


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fetchReport', methods=['POST', ])
def fetch_report():
    url = "http://i.luckypaying.com/bill/getBillDownUrl"
    headers = {
        'Cookie': request.form['cookie']
    }

    begin_time = datetime.datetime.strptime(request.form['begin'], '%Y-%m-%d')
    end_time = datetime.datetime.strptime(request.form['end'], '%Y-%m-%d')

    for date in date_range(begin_time, end_time):
        date_string = "{}-{:0>2d}-{:0>2d}".format(date.year, date.month, date.day)
        querystring = {"billDate": date_string, "tradeType": "PAY"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        with open("./down/{}.xls".format(date_string), "wb") as code:
            code.write(response.content)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
