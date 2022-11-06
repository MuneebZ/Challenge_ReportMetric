import pandas as pd


def df_cleaning():
    """
    1. Transforming the .csv files from data directory into pandas (pd) DataFrames (df).
    2. Turn date objects into datetime objects
    3. Left join respective dfs using correct columns from left to right column
    4. Return final, cleaned df

    Returns:
        df: The cleaned DataFrame from function df_cleaning() -> pd.DataFrame
    """

    # Load datasets
    order = pd.read_csv('data/orders.csv')
    orderLine = pd.read_csv('data/order_lines.csv')
    # product = pd.read_csv('data/products.csv')        not used during the cleaning process
    promotion = pd.read_csv('data/promotions.csv')
    productProm = pd.read_csv('data/product_promotions.csv')
    vendorCom = pd.read_csv('data/commissions.csv')

    # Transform dates into datetime objects
    order['date_parsed'] = pd.to_datetime(
        order['created_at'], infer_datetime_format=True)
    order['date_parsed'] = pd.to_datetime(
        order['date_parsed'].dt.date, infer_datetime_format=True)
    vendorCom['date_parsed'] = pd.to_datetime(
        vendorCom['date'], infer_datetime_format=True)
    productProm['date_parsed'] = pd.to_datetime(
        productProm['date'], infer_datetime_format=True)

    # Left join tables using pd.merge onto respective columns
    df = pd.merge(left=orderLine, right=order, how="left",
                  left_on='order_id', right_on='id')
    df = pd.merge(left=df, right=vendorCom, how="left", left_on=['date_parsed', 'vendor_id'],
                  right_on=['date_parsed', 'vendor_id'], )
    df = pd.merge(left=df, right=productProm, how="left", left_on=['date_parsed', 'product_id'],
                  right_on=['date_parsed', 'product_id'], )
    df = pd.merge(left=df, right=promotion, how="left",
                  left_on=['promotion_id'], right_on=['id'], )

    return df


df = df_cleaning()
df = df.drop(['created_at', 'date_x', 'date_y', 'id_y'],
             axis=1)  # drop repeated columns

# Save df onto a .csv file labeled 'out.csv'
df.to_csv('data/out.csv', index=False)
