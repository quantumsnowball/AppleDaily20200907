import os
import twint
import pandas as pd


def scrap(keyword='AAPL', start=None, end=None, batch_size=250, tempfile='temp.csv'):
    c = twint.Config()
    c.Search = keyword
    c.Limit = batch_size
    c.Since = start
    c.Until = end
    c.Store_csv = True
    c.Hide_output = True
    c.Output = tempfile

    twint.run.Search(c)

    try:
        data = pd.read_csv(tempfile)
        df = data[['date','time','username','tweet']]
        if os.path.exists(tempfile):
            os.remove(tempfile)
        return df
    except FileNotFoundError:
        print('No search result is returned.')