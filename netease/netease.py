import requests
import pandas as pd
import io

headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/56.0.2924.87 Safari/537.36',
    }

EXCHANGE_TYPES = {
    '上交所': 0,
    '深交所': 1
}

def historical_prices(code, start='', end='', fields='TCLOSE;LCLOSE;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'):
    code = str(code)
    first_code = '1' if code[0] in ('0', '2', '3') else '0'
    url = 'http://quotes.money.163.com/service/chddata.html'
    data = {
        'code': first_code + str(code),
        'start': str(start),
        'end': str(end),
        'fields': str(fields),
    }
    r = requests.get(url, params=data, headers=headers)
    r.encoding='gb2312'
    df = pd.read_csv(io.StringIO(r.text), index_col=0, parse_dates=['日期'])
    df['股票代码'].replace(regex=True, to_replace=r'\'', value=r'', inplace=True)
    return df

def zycwzb(code):
    url = 'http://quotes.money.163.com/service/zycwzb_' + str(code) + '.html'
    data = {
        'type': 'report'
    }
    r = requests.post(url, data=data, headers=headers)
    df=pd.read_csv(io.StringIO(r.text))
    t=df.drop(df.columns[-1], axis=1).T
    csv_buffer=io.StringIO()
    t.to_csv(csv_buffer)
    csv_buffer.seek(0)
    df2=pd.read_csv(csv_buffer, header=1, parse_dates=['报告日期'], index_col=0)
    df2['每股净资产(元)'].replace(to_replace='--', value=0, inplace=True)
    return df2