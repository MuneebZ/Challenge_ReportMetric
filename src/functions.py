import datetime
import json
from dataclasses import dataclass
import numpy as np
import pandas as pd


from data_cleaning import df_cleaning

df = df_cleaning()


@dataclass
class ReportMetric:
    """
    A class with methods that will return the desired report metrics.
    A description of each metric is found above each method in a comment.
    
    df: The cleaned DataFrame from data_cleaning.py -> pd.DataFrame
    startdate: The date the user inputs at the endpoint -> datetime.datetime

    """

    df: pd.DataFrame
    startdate: datetime.datetime

    # The total number of items sold on that day.
    def items_sold(self):
        df_sold_that_day = self.df[['date_parsed', 'quantity']]
        df_sold_that_day_groupby = df_sold_that_day.groupby(
            by='date_parsed').sum()
        itmes = df_sold_that_day_groupby[df_sold_that_day_groupby.index.isin(
            [self.startdate])]['quantity'].values[0]
        return itmes

    # The total number of customers that made an order that day.
    def costumer_total(self):
        df_customer = self.df[['date_parsed', 'customer_id']]
        df_customer_groupby = df_customer.groupby(by='date_parsed').nunique()
        customers = df_customer_groupby[df_customer_groupby.index.isin(
            [self.startdate])]['customer_id'].values[0]
        return customers

    # The average discount rate applied to the items sold that day.
    def discount_rate(self):
        df_discount_rate_that_day = self.df[['date_parsed', 'discount_rate']]
        df_discount_rate_that_day_groupby = df_discount_rate_that_day.groupby(
            by='date_parsed').mean()
        discount_rate_avg = \
            df_discount_rate_that_day_groupby[df_discount_rate_that_day_groupby.index.isin([self.startdate])][
                'discount_rate'].values[0]
        return discount_rate_avg

    # The average order total for that day
    def order_total_avg(self):
        df_orderAvg_that_day = self.df[['date_parsed', 'total_amount']]
        df_orderAvg_that_day_groupby = df_orderAvg_that_day.groupby(
            by='date_parsed').mean()
        order_total_avg = df_orderAvg_that_day_groupby[df_orderAvg_that_day_groupby.index.isin([self.startdate])][
            'total_amount'].values[0]
        return order_total_avg

    # The total amount of discount given that day.
    def discount_total(self):
        df_disc_total_that_day = self.df[['date_parsed', 'discounted_amount']]
        df_disc_total_that_day_groupby = df_disc_total_that_day.groupby(
            by='date_parsed').sum()
        total_discount_amount = \
            df_disc_total_that_day_groupby[df_disc_total_that_day_groupby.index.isin(
                [self.startdate])]['discounted_amount'].values[0]
        return total_discount_amount

    # The total amount of commissions generated that day.
    def comm_total(self):
        df_total_com = self.df[['total_amount', 'rate', 'date_parsed']]
        df_total_com['total_com'] = self.df['total_amount'] * self.df['rate']
        df_total_com_groupby = df_total_com.groupby(
            by='date_parsed').agg({'total_com': ['sum']})
        commissions_total = df_total_com_groupby[df_total_com_groupby.index.isin([self.startdate])][
            'total_com'].values[0]
        return commissions_total

    #
    def comm_avg(self):
        df_total_avg = self.df[['total_amount',
                                'rate', 'date_parsed', 'order_id']]
        df_total_avg['total_avg'] = self.df['total_amount'] * self.df['rate']
        df_total_avg_groupby = df_total_avg.groupby(
            by=['date_parsed']).agg({'total_avg': ['mean']})
        commissions_order_average = df_total_avg_groupby[df_total_avg_groupby.index.isin([self.startdate])][
            'total_avg'].values[0]
        return commissions_order_average

    #
    def comm_total_prom(self):
        df_com_prom = self.df[['total_amount',
                               'rate', 'date_parsed', 'promotion_id']]
        df_com_prom['total_com_prom'] = self.df['total_amount'] * \
            self.df['rate']
        df_com_prom_groupby = df_com_prom.groupby(by=['date_parsed', 'promotion_id'], as_index=False).agg(
            {'total_com_prom': ['sum']})
        df2 = df_com_prom_groupby[df_com_prom_groupby['date_parsed']
                                  == self.startdate][df_com_prom_groupby.columns[1:]]
        commissions_promotion_average = dict(
            zip(df2[df2.columns[0]], df2[df2.columns[1]]))
        return commissions_promotion_average

    # def __post_init__(self):
    #     self.description = f"{self.df} at {self.startdate}"


class NpEncoder(json.JSONEncoder):
    """
    Defining our own enconder class to be used within the json.dumps function in app.py.
    This solves the TypeError problem: "Object of type '{type}' is not JSON serializable" 
    """

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)
