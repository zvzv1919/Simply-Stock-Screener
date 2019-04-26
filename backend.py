#print "hello world"
from StringIO import StringIO
# import pycurl
import certifi
import csv
import sys
import datetime
import json
import pymysql
import requests
import mysql.connector
import time
import urllib

# buffer = StringIO()
# c = pycurl.Curl()
#
# #Place the API request here
# c.setopt(c.URL, 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&'
#                 'outputsize=full&apikey=PTF07M1M1UTX6RCF')
# c.setopt(c.CAINFO, certifi.where())
# c.setopt(c.WRITEDATA, buffer)
# c.perform()
# c.close()
#
# #respond from Alpha Vantage in JSON form
# body = buffer.getvalue()
# # Body is a string in some encoding.
# # In Python 2, we can print it without knowing what the encoding is.
# print(body[:10000])
#
# buffer2=StringIO()
# c = pycurl.Curl()
# c.setopt(c.URL, 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&'
#                 'outputsize=full&apikey=PTF07M1M1UTX6RCF')
# c.setopt(c.CAINFO, certifi.where())
# c.setopt(c.WRITEDATA, buffer2)
# c.perform()
# c.close()
#
# body2 = buffer2.getvalue()
# print(body2[:10000])

# buffer3=StringIO()
# # c = pycurl.Curl()
# # c.setopt(c.URL, 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download'
# # )
# # c.setopt(c.CAINFO, certifi.where())
# # c.setopt(c.WRITEDATA, buffer3)
# # c.perform()
# # c.close()
# #
# # body3 = buffer3.getvalue()
# # print(body3[:10000])


# with open('out.csv', 'w') as f:
#     writer = csv.writer(f)
#     reader = csv.reader(data.text.splitlines())
#     for row in reader:
#         print row[0]

# a list holding all company symbols
company_list=[]
now=datetime.datetime.now()
# update the database
def update():
    with open('companylist.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # print row[0]
                company_list.append(row[0])
                line_count += 1
   # print company_list
    # TODO: complete the testing and intraday data filling
    for symbol in company_list:
        request = 'https://api.iextrading.com/1.0/stock/%s/batch?types=chart&range=5y&chartLast=10' % symbol
        # print request
        dataRaw = requests.get(request)
        try:
            data = (json.loads(dataRaw.text))["chart"]
        except ValueError:
            continue
        for item in data:
            try:
                #print symbol, item['date'], item['open'], item['high'], item['low'], item['close']
                vals = [symbol, item['date'], item['open'], item['high'], item['low'], item['close'], item['close'], item['volume'], 0 , 1 ]
                add_stock(vals)
            except KeyError:
                #print ""
                continue



    # use iextest() as an example
    #time.sleep(5)
    # symbol='aapl'
    # request = 'https://api.iextrading.com/1.0/stock/%s/batch?types=chart&range=5y&chartLast=10' % symbol
    # #print request
    # dataRaw = requests.get(request)
    # data=(json.loads(d\ataRaw.text))["chart"]
    # for item in data:
    #     print item
    # return
"""def update():
    with open('companylist.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                #print row[0]
                company_list.append(row[0])
                line_count += 1
    print company_list
    #TODO: complete the testing and intraday data filling
    for symbol in company_list:
        request='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&' \
                'apikey=PTF07M1M1UTX6RCF&datatype=csv' % symbol
        print request
        data=requests.get(request)
        reader = csv.reader(data.text.splitlines())
        for row in reader:
            print row
"""

"""def get_intraday(stock_symbol):
    request = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=1min&' \
              'outputsize=full&apikey=PTF07M1M1UTX6RCF&datatype=csv' % stock_symbol
    data = requests.get(request)
    reader = csv.reader(data.text.splitlines())
    for row in reader:
        print row
"""

def get_live(stock_symbol):
    while True:
        get_realtime(stock_symbol)
        time.sleep(30)

def get_realtime(stock_symbol):
        url = 'https://api.iextrading.com/1.0/stock/%s/price' % stock_symbol
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print "p", data
   
        request = 'https://api.iextrading.com/1.0/stock/%s/batch?types=chart&range=5y&chartLast=1' % stock_symbol
        # print request
        dataRaw = requests.get(request)
        data = (json.loads(dataRaw.text))["chart"]

        for item in data:
                print "o", item['change'], item['changePercent'], item['high'], item['volume'], item['low']
                vals = [stock_symbol, item['date'], item['open'], item['high'], item['low'], item['close'], item['close'], item['volume'], 0 , 1 ]
                conn = mysql.connector.connect(host = '162.221.219.6', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
                cursor = conn.cursor()
                cursor.execute("DELETE from stocks TICKER = %s AND DATE = %s", stock_symbol, item['date'] )
                conn.commit();
                conn.close();
                add_stock(vals)

        sys.stdout.flush()
        
        
# Get stock info (current day)
def get_current(stock_symbol):
    request = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=%s' \
              '&apikey=PTF07M1M1UTX6RCF&datatype=csv' % stock_symbol
    data = requests.get(request)
    return data


# Get stock info (daily price over time)
def get_daily(stock_symbol):
    # api request to retrieve daily price - Xuan
    """data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&'
                    'apikey=PTF07M1M1UTX6RCF&datatype=csv')
    """

    request = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&outputsize=full&' \
              'apikey=PTF07M1M1UTX6RCF&datatype=csv' % stock_symbol
    data = requests.get(request)

    return data

    # update database with price for each day - Brian
    # call add_stock


def add_stock(row):
    conn = mysql.connector.connect(host = '162.221.219.6', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    # print ("writing to db")
    cursor.execute("INSERT INTO stocks(ticker, timestamp, open, high, low, close, adjusted_close, volume, dividend_amount, split_coefficient) VALUES (%s,%s, %s, %s, %s, %s,%s, %s, %s, %s)", [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])
    # print ("wrote to db")
    conn.commit();
    conn.close();
    # return processed_text

def add_stock_fin(row):
    conn = mysql.connector.connect(host = '162.221.219.6', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    # print ("writing to db")
    cursor.execute("INSERT INTO stocks_fin(name, profit, revenue, income, debt, cash) VALUES (%s,%s, %s, %s, %s, %s)", [row[0], row[1], row[2], row[3], row[4], row[5]])
    # print ("wrote to db")
    conn.commit();
    conn.close();
    # return processed_text

def get_stock(ticker):
    conn = mysql.connector.connect(host = '162.221.219.6', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    cursor.execute("SELECT * from stocks WHERE ticker = %s ORDER by timestamp DESC", [ticker])
    data = cursor.fetchall()
    for row in data:
        print (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])

    conn.commit();
    conn.close();
    
def get_historical(ticker):
    conn = mysql.connector.connect(host = '162.221.219.6', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    cursor.execute("SELECT * from stocks WHERE ticker = %s ORDER by timestamp DESC", [ticker])
    data = cursor.fetchall()
    for row in data:
        
        print (row[1]),
        print (row[5])

    conn.commit();
    conn.close();
    
def search_timeframe(start, end, low, high):
    conn = mysql.connector.connect(host = '162.221.219.6', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
    cursor = conn.cursor();
    cursor.execute('SELECT * FROM stocks WHERE %s <= timestamp AND timestamp <= %s AND close >= %s AND close <= %s GROUP BY ticker ', [start,end, low,high])
    data = cursor.fetchall()
    for row in data:
        print (row[0])
    conn.commit();
    conn.close();

# Retrieve current data for single stock, return it to be displayed, and
# update database with historical daily price info
def singlestock(stock_symbol):
    conn = mysql.connector.connect(host = '162.221.219.6', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    # print (stock_symbol)
    cursor.execute("SELECT * FROM Stocks WHERE ticker = %s", [stock_symbol])
    # gets the number of rows affected by the command executed
    data = cursor.fetchall()
    count = 0
    for row in data:
        count += 1
    if count == 0:
        # add the stock to database
        row_count=0
        data = get_daily(stock_symbol)
        reader = csv.reader(data.text.splitlines())
        for row in reader:
            if row_count != 0:
                row = [stock_symbol] + row
                add_stock(row)
            row_count += 1
    #else:
    data = get_current(stock_symbol)
    reader = csv.reader(data.text.splitlines())
    for row in reader:
        print row


    #     print "It Does Not Exist"
    # else:
    #     print "It Does Exist"

    # if data does not already exist in database - Brian
    #get_daily(stock_symbol)
    # get_current(stock_symbol)?
    # print current - Xuan
    # else
    #get_current(stock_symbol)
    # print current data - Xuan


    # if data does not already exist in database - Brian


        # get_current(stock_symbol)?
        # print current - Xuan
    # else
    #     data=get_current(stock_symbol)
    #     reader = csv.reader(data.text.splitlines())
    #     for row in reader:
    #         print row
        # print current data - Xuan


def extractDate(date, component):
    # print date.month
    if component=='YEAR':
        return date.year
    elif component=='MONTH':
        return date.month
    elif component=='DAY':
        return date.day
    else:
        print "invalid component of date"

# Return price points for graph


def graph(stock_symbol,  timeframe):
    max_count=60    # doesn't work for 'all'

    conn = mysql.connector.connect(host='162.221.219.6', user='test', password='cs407test', database='stock_info',
                                   auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    cursor.execute("SELECT * from stocks WHERE ticker = %s ORDER by timestamp DESC", [stock_symbol])
    data = cursor.fetchall() # raw data from database
    # print data
    plot_data=[]    # datapoints to be plotted, formatted as[[date, price]]
    if timeframe=='1 month':
        count=0
        for row in data:
            day=extractDate(row[1], 'DAY')
            month=extractDate(row[1], 'MONTH')
            if day < now.day and month < now.month and now.month > 1 \
                    or day < now.day and month == 12 and now.month == 1 \
                    or month < now.month - 2\
                    or now.month == 1 and month < 12 \
                    or count >= max_count:
                break
            else:
                # plot_data.append([row[1], row[5]])
                print(row[1]),
                print(row[5])
                count +=1
        # print '1 month'
        # take a point every day for 1 month
    elif timeframe=='6 month':
        # print "6 month"
        count = 0
        prevday=-2
        for row in data:
            day=extractDate(row[1], 'DAY')
            month=extractDate(row[1], 'MONTH')
            if day < now.day and month < now.month - 5 and now.month > 6 \
                    or day < now.day and month < now.month + 7 and month > now.month and now.month <=6 \
                    or now.month > 7 and month < now.month - 6 \
                    or now.month == 7 and month == 12 \
                    or now.month <= 6 and month < now.month + 6 and month > now.month\
                    or count >= max_count:
                break
            else:
                if abs(day-prevday)!=1:
                # plot_data.append([row[1], row[5]])
                    print (row[1]),
                    print (row[5])
                    count+=1
                prevday=day
    elif timeframe=='1 year':
        # print '1 year'
        count = 0
        prevday = -2
        for row in data:
            day = extractDate(row[1], 'DAY')
            month = extractDate(row[1], 'MONTH')
            year = extractDate(row[1], 'YEAR')
            if day < now.day and month == now.month and year < now.year \
                    or month < now.month and year < now.year and now.month > 1\
                    or month <= 12 and now.month == 1 and year < now.year\
                    or count >= max_count:
                break
            else:
                if abs(day-prevday)!=1:
                # plot_data.append([row[1], row[5]])
                    print(row[1]),
                    print(row[5])
                    count += 1
                prevday = day
    elif timeframe=='all':
        count = 0
        prevmonth = 0
        for row in data:
            month = extractDate(row[1], 'MONTH')
            if month != prevmonth:
                # plot_data.append([row[1], row[5]])
                print(row[1]),
                print(row[5])
                count += 1
            prevmonth = month
        # print 'all'
    else:
        print 'Invalid timeframe'
    # Take time frame and grab 30 evenly-spaced data points - Xuan
    # Retrieve those data points from database x30 - Brian
    # print 30 data points - Xuan
    # print "testgraph"
    # print plot_data

def parse(query):

    def judge(symbol):
        return True
    tokens=query.split(' ')
    # print(tokens)
    if(tokens[0]=='GAIN'):
        return 'GAIN'
    if(',' in tokens[0]):
        return 'PRICE'
    else:
        return judge

def gain_value(percentage, gt, sdate, edate):
    sdatevals = sdate.split('-')
    if len(sdatevals) == 3:
        # print(sdatevals[0],sdatevals[1],sdatevals[2]);
        if ((len(sdatevals[0]) >= 1 and len(sdatevals[0]) <= 4) and (
                int(sdatevals[1]) >= 1 and int(sdatevals[1]) <= 12) and (
                int(sdatevals[2]) >= 1 and int(sdatevals[2]) <= 31)):
            x = 1
        else:
            print "fail1";
            return
    else:
        if sdate != "sot":
            # print sdate
            return

    edatevals = edate.split('-')
    if len(edatevals) == 3:
        if ((len(edatevals[0]) >= 1 and len(edatevals[0]) <= 4) and (
                int(edatevals[1]) >= 1 and int(edatevals[1]) <= 12) and (
                int(edatevals[2]) >= 1 and int(edatevals[2]) <= 31)):
            x = 1
        else:
            print "fail2";
            return
    else:
        if edate != "present":
            # print edate
            return

    connNew = mysql.connector.connect(host='162.221.219.6', user='test', password='cs407test', database='stock_info',
                                   auth_plugin='mysql_native_password')
    cursorNew = connNew.cursor();
    if (edate == "present"):
        # print ("here")
        cursorNew.execute(
            'SELECT * FROM stocks A INNER JOIN (SELECT max(timestamp) mv, ticker FROM stocks GROUP BY ticker) B on A.ticker= B.ticker and A.timestamp = B.MV;'
        )
    if (edate != "present"):
        cursorNew.execute(
            'SELECT s.ticker, s.timestamp, s.close FROM stocks s AS a RIGHT JOINWHERE s.timestamp = '
            '(SELECT min(st.timestamp) FROM stocks st WHERE s.ticker = st.ticker AND st.timestamp >= %s)', [sdate])
    dataNew = cursorNew.fetchall()
    for row in dataNew:
        print row
    connNew.close()

    # print the rows
    connOld = mysql.connector.connect(host='162.221.219.6', user='test', password='cs407test', database='stock_info',
                                      auth_plugin='mysql_native_password')
    cursorOld = connOld.cursor();
    if (sdate == "sot"):
        cursorOld.execute(
           'SELECT * FROM stocks A INNER JOIN (SELECT min(timestamp) mv, ticker FROM stocks GROUP BY ticker) B on A.ticker= B.ticker and A.timestamp = B.MV;'
        )
    if (sdate != "sot"):
        cursorOld.execute(
            'SELECT s.ticker, s.timestamp, s.close FROM stocks s AS a RIGHT JOINWHERE s.timestamp = '
            '(SELECT min(st.timestamp) FROM stocks st WHERE s.ticker = st.ticker AND st.timestamp >= %s)', [sdate])
           # 'SELECT ticker, min(timestamp), close FROM stocks WHERE timestamp >= %s GROUP BY ticker ORDER BY ticker', [sdate])
    dataOld = cursorOld.fetchall()
    connOld.close()
    # for row in dataOld:
    #     print row
    # for row in dataNew:
    #     print row
    percentageVal = float(percentage)
    for rowNew in dataNew:
        for rowOld in dataOld:
            if rowOld[0]==rowNew[0]:
                priceNew=float(rowNew[2])
                priceOld=float(rowOld[2])
                # print "priceNew:",priceNew
                # print "priceOld:",priceOld, percentage
                #print ((priceNew-priceOld)*100/priceOld)>percentage
                if(priceOld==0):
                    print rowNew[0]
                elif gt and (priceNew-priceOld)*100/priceOld>percentageVal or not gt and (priceNew-priceOld)*100/priceOld<percentageVal:
                    print rowNew[0]


    # for row in dataNew:
    #     print (row[0])
    #    print (row[0], row[1], row[2], row[3], row[4])
    #    s = s + str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]) \
    #        + ' ' + str(row[3]) + ' ' + str(row[4]) + '<br />'

    # disconnect from server


    connOld.close()

# Takes a search query and searches the database - should support "sot" or "YYYY-MM-DD" for sdate and "present" or "YYYY-MM-DD" for edate
def search(query, sdate, edate):

    # Check if the condition is "Gaining value". If so, do parsing here
    condition=parse(query)
    if condition=="GAIN":
        tokens=query.split(' ')
        gain_value(tokens[2], tokens[1]=='>', sdate, edate)
        return
    # TODO:Remove after sprint2
    if condition=="PRICE":
        # do nothing
        print("")
    #TODO:Implement in sprint 3
    else:
        print("Unsupported query")
        return

    #check for date validity
    sdatevals = sdate.split('-')
    if len(sdatevals) == 3:
        #print(sdatevals[0],sdatevals[1],sdatevals[2]);
        if ( (len(sdatevals[0])>= 1 and  len(sdatevals[0]) <= 4) and (int(sdatevals[1])>=1 and int(sdatevals[1]) <= 12) and (int(sdatevals[2]) >=1 and int(sdatevals[2]) <= 31)):
            x = 1
        else :
            print "fail1";
            return
    else:
        if sdate != "sot":
            #print sdate
            return

    edatevals = edate.split('-')
    if len(edatevals) == 3:
        if ( (len(edatevals[0])>= 1 and  len(edatevals[0]) <= 4) and (int(edatevals[1])>=1 and int(edatevals[1]) <= 12) and (int(edatevals[2]) >=1 and int(edatevals[2]) <= 31)):
            x = 1
        else :
            print "fail2";
            return
    else:
        if edate != "present":
            #print edate
            return

    vals = query.split(',')
    low = float(vals[0])
    high = float(vals[1])
    conn = mysql.connector.connect(host = '162.221.219.6', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
    cursor = conn.cursor();
    if (sdate == "sot" and edate == "present") :
        cursor.execute('SELECT ticker, max(timestamp) FROM stocks WHERE %s < close AND close < %s GROUP BY ticker ORDER BY ticker', [low, high])
    if (sdate == "sot" and edate != "present") :
        cursor.execute('SELECT ticker, max(timestamp) FROM stocks WHERE %s < close AND close < %s AND timestamp <= %s GROUP BY ticker ORDER BY ticker', [low, high, edate])
    if (sdate != "sot" and edate == "present") :
        cursor.execute('SELECT ticker, max(timestamp) FROM stocks WHERE %s < close AND close < %s AND timestamp >= %s GROUP BY ticker ORDER BY ticker', [low, high, sdate])
    if (sdate != "sot" and edate != "present") :
        cursor.execute('SELECT ticker, max(timestamp) FROM stocks WHERE %s < close AND close < %s AND timestamp >= %s AND timestamp <= %s GROUP BY ticker ORDER BY ticker', [low, high, sdate, edate])
    data = cursor.fetchall()
    # print the rows

    for row in data:
        print (row[0])
    #    print (row[0], row[1], row[2], row[3], row[4])
    #    s = s + str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]) \
    #        + ' ' + str(row[3]) + ' ' + str(row[4]) + '<br />'

    # disconnect from server

    conn.close()

def iextest():
    prefix='https://api.iextrading.com/1.0'
    with open('IEX_API.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                #print row[0]
                company_list.append(row[0])
                line_count += 1
    #print company_list
    #TODO: complete the testing and intraday data filling
    batchnum=0
    request = prefix + '/stock/market/batch?types=quote&symbols='
    for symbol in company_list:
        if batchnum == 100:
            # Dispatch previous batch request
            print ""
            print request
            data=requests.get(request)
            reader = csv.reader(data.text.splitlines())
            for row in reader:
                print row
            # Reset batchnum and request
            batchnum=0
            request=prefix + '/stock/market/batch?types=quote&symbols='
        if batchnum == 0:
            request = request + symbol
        else:
            request = request + ',' + symbol
        batchnum += 1
    #Dispatch last batch request
    print ""
    print request
    data=requests.get(request)
    reader = csv.reader(data.text.splitlines())
    for row in reader:
        print row
def main():
    #search_timeframe('2008-02-21','2019-02-21','35.00','39.00');
    #search('35.00,39.00','2008-02-21','2019-02-21');
    """prefix='https://api.iextrading.com/1.0'
    request = prefix + '/stock/market/batch?types=quote&symbols=AAPL,UTX'
    print request
    data=requests.get(request)
    reader = csv.reader(data.text.splitlines())
    for row in reader:
        print row
    """
    #test driver
    #singlestock("AAL")
    #print extractDate("1234-56-78", "DAY")
    #graph("AAL", "1 month")

    # print "Current date and time using instance attributes:"
    # print "Current year: %d" % now.year
    # print "Current month: %d" % now.month
    # print "Current day: %d" % now.day
    # print "Current hour: %d" % now.hour
    # print "Current minute: %d" % now.minute
    # print "Current second: %d" % now.second
    # print "Current microsecond: %d" % now.microsecond
    
    #iextest()

    # graph("RAT", "1 month")
    #singlestock("AAL")
    # control statement
    if len(sys.argv) < 3:
        if (len(sys.argv) == 2) and (sys.argv[1] == "update"):
            update()
            return
        else:
            print "format error"
            exit(1)
    if sys.argv[1] == "single":
        singlestock(sys.argv[2])
    elif sys.argv[1] == "historical":
        get_historical(sys.argv[2])
    elif sys.argv[1] == "search":
        if len(sys.argv) < 5:
            print "format error"
            exit(1)
        search(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == "graph":
        if len(sys.argv) < 4:
            print "format error"
            exit(1)
        graph(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "live":
        get_live(sys.argv[2])
    else:
        print "format error"



if __name__ == '__main__':
    main()
# def get_historical_price(time_frame):
#     if(time_frame=='')
#get_current('AAL')
