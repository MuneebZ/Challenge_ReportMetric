from flask import Flask, render_template, request
import datetime
import json
import numpy as np
import pandas as pd
from functions import ReportMetric, NpEncoder

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def result():
    json_string = schema_output()

    return render_template('form.html', entry=json_string)


def schema_output():
    startdate = date_formatting()
    df = pd.read_csv('out.csv')

    commission_avg_per_order, commission_total, commission_total_per_prom, \
        customers, discount_rate_avg, discount_total, \
        items, order_total_avg = metric_values(df, startdate)

    json_output = \
        {
            'customers': customers,
            'total_discount_amount': round(discount_total, 2),
            'items': items,
            "order_total_avg": round(order_total_avg, 2),
            # round(discount_rate_avg, 2),
            "discount_rate_avg": round(discount_rate_avg, 2),
            "commissions": {
                "promotions": {
                    "1": round(commission_total_per_prom.get(1, np.NaN), 2),
                    "2": round(commission_total_per_prom.get(2, np.NaN), 2),
                    "3": round(commission_total_per_prom.get(3, np.NaN), 2),
                    "4": round(commission_total_per_prom.get(4, np.NaN), 2),
                    "5": round(commission_total_per_prom.get(5, np.NaN), 2),
                },
                "total": round(commission_total[0], 2),
                "order_average": round(commission_avg_per_order[0], 2),
            }
        }
    json_string = json.dumps(
        json_output, allow_nan=True, indent=4, cls=NpEncoder)
    return json_string


def metric_values(df, startdate):
    report_metric = ReportMetric(df=df, startdate=startdate)

    items = report_metric.items_sold()
    customers = report_metric.costumer_total()
    discount_rate_avg = report_metric.discount_rate()
    order_total_avg = report_metric.order_total_avg()
    discount_total = report_metric.discount_total()
    commission_total = report_metric.comm_total()
    commission_avg_per_order = report_metric.comm_avg()
    commission_total_per_prom = report_metric.comm_total_prom()
    
    return commission_avg_per_order, commission_total, \
    commission_total_per_prom, customers, discount_rate_avg, \
    discount_total, items, order_total_avg


def date_formatting():
    startdate = datetime.datetime.strptime(
        request.form["var_3"],
        '%Y-%m-%d')
    startdate = startdate.strftime('%Y-%m-%d')
    return startdate


if __name__ == '__main__':
    app.run(debug=True)
