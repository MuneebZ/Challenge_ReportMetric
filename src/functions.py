import datetime
import json
import numpy as np
import pandas as pd
from dataclasses import dataclass

from data_cleaning import df_cleaning

df = df_cleaning()


@dataclass
class ReportMetric:
    """_summary_

    Returns:
        _type_: _description_
    """

    df: pd.DataFrame
    startdate: datetime.datetime

    #
    def items_sold(self):
        df_sold_that_day = self.df[['date_parsed', 'quantity']]
        df_sold_that_day_groupby = df_sold_that_day.groupby(
            by='date_parsed').sum()
        itmes = df_sold_that_day_groupby[df_sold_that_day_groupby.index.isin(
            [self.startdate])]['quantity'].values[0]
        return itmes

    #
    def costumer_total(self):
        df_customer = self.df[['date_parsed', 'customer_id']]
        df_customer_groupby = df_customer.groupby(by='date_parsed').nunique()
        customers = df_customer_groupby[df_customer_groupby.index.isin(
            [self.startdate])]['customer_id'].values[0]
        return customers

    #
    def discount_rate(self):
        df_discount_rate_that_day = self.df[['date_parsed', 'discount_rate']]
        df_discount_rate_that_day_groupby = df_discount_rate_that_day.groupby(
            by='date_parsed').mean()
        discount_rate_avg = \
            df_discount_rate_that_day_groupby[df_discount_rate_that_day_groupby.index.isin([self.startdate])][
                'discount_rate'].values[0]
        return discount_rate_avg

    #
    def order_total_avg(self):
        df_orderAvg_that_day = self.df[['date_parsed', 'total_amount']]
        df_orderAvg_that_day_groupby = df_orderAvg_that_day.groupby(
            by='date_parsed').mean()
        order_total_avg = df_orderAvg_that_day_groupby[df_orderAvg_that_day_groupby.index.isin([self.startdate])][
            'total_amount'].values[0]
        return order_total_avg

    #
    def discount_total(self):
        df_disc_total_that_day = self.df[['date_parsed', 'discounted_amount']]
        df_disc_total_that_day_groupby = df_disc_total_that_day.groupby(
            by='date_parsed').sum()
        total_discount_amount = \
            df_disc_total_that_day_groupby[df_disc_total_that_day_groupby.index.isin(
                [self.startdate])]['discounted_amount'].values[0]
        return total_discount_amount

    #
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
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)