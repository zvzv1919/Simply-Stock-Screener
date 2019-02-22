#print "hello world"
from StringIO import StringIO
# import pycurl
import certifi
import csv
import sys
import datetime
import pymysql
import requests
import mysql.connector

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

# Get stock info (current day)
def get_current(stock_symbol):
    request = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=%s' \
              '&apikey=PTF07M1M1UTX6RCF&datatype=csv' % stock_symbol
    data = requests.get(request)
    return data

# Get stock info (daily price over time)
def get_daily(stock_symbol):
    #api request to retrieve daily price - Xuan
    """data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&'
                    'apikey=PTF07M1M1UTX6RCF&datatype=csv')
    """

    request = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&outputsize=full&' \
              'apikey=PTF07M1M1UTX6RCF&datatype=csv' % stock_symbol
    data = requests.get(request)
    reader = csv.reader(data.text.splitlines())
    for row in reader:
        print row
    return data
    # update database with price for each day - Brian
	#call add_stock
	
def add_stock(name , symbol, low, high , date):
	conn = mysql.connector.connect(host = 'DESKTOP-38PNH3Q', user = 'root', password ='cs407sss', database = 'stock_info',auth_plugin='mysql_native_password')
	cursor = conn.cursor()
	#print ("writing to db")
	cursor.execute("INSERT INTO stocks(Name, Symbol, Low, High, Date ) VALUES (%s,%s, %s, %s, %s)", [name , symbol, low, high , date])
	#print ("wrote to db")
	conn.commit();
	conn.close();
	#return processed_text



# Retrieve current data for single stock, return it to be displayed, and update database with historical daily price info
def singlestock(stock_symbol):
    # if data does not already exist in database - Brian
        data=get_daily(stock_symbol)
        reader = csv.reader(data.text.splitlines())
        for row in reader:
            print row

        # get_current(stock_symbol)?
        # print current - Xuan
    # else
        data=get_current(stock_symbol)
        reader = csv.reader(data.text.splitlines())
        for row in reader:
            print row
        # print current data - Xuan
    
def extractDate(date, component):
    if component=='YEAR':
        return int(date[0:4])
    elif component=='MONTH':
        return int(date[5:7])
    elif component=='DAY':
        return int(date[8:10])
    else:
        print "invalid component of date"

# Return price points for graph
def graph(stock_symbol,  timeframe):
    max_count=60    #doesn't work for 'all'

    #TODO:GET data from sql
    data=[] #raw data from database
    plot_data=[]    #datapoints to be plotted, formatted as[[date, price]]
    if timeframe=='1 month':
        count=0
        for row in data:
            day=extractDate(row[0], 'DAY')
            month=extractDate(row[0], 'MONTH')
            if day < now.day and month < now.month and now.month > 1 \
                    or day < now.day and month == 12 and now.month == 1 \
                    or month < now.month - 2\
                    or now.month == 1 and month < 12 \
                    or count >= max_count:
                break
            else:
                plot_data.add(row[0], row[4])
                count +=1
        # print '1 month'
        # take a point every day for 1 month
    elif timeframe=='6 month':
        # print "6 month"
        count = 0
        prevday=-2
        for row in data:
            day=extractDate(row[0], 'DAY')
            month=extractDate(row[0], 'MONTH')
            if day < now.day and month < now.month - 5 and now.month > 6 \
                    or day < now.day and month < now.month + 7 and month > now.month and now.month <=6 \
                    or now.month > 7 and month < now.month - 6 \
                    or now.month == 7 and month == 12 \
                    or now.month <= 6 and month < now.month + 6 and month > now.month\
                    or count >= max_count or abs(day-prevday)==1:
                break
            else:
                plot_data.add(row[0], row[4])
                count+=1
                prevday=day
    elif timeframe=='1 year':
        # print '1 year'
        count = 0
        prevday = -2
        for row in data:
            day = extractDate(row[0], 'DAY')
            month = extractDate(row[0], 'MONTH')
            year = extractDate(row[0], 'YEAR')
            if day < now.day and month == now.month and year < now.year \
                    or month < now.month and year < now.year and now.month > 1\
                    or month <= 12 and now.month == 1 and year < now.year\
                    or count >= max_count or abs(day - prevday) == 1:
                break
            else:
                plot_data.add(row[0], row[4])
                count += 1
                prevday = day
    elif timeframe=='all':
        count = 0
        prevmonth = 0
        for row in data:
            month = extractDate(row[0], 'MONTH')
            if month == prevmonth:
                break
            else:
                plot_data.add(row[0], row[4])
                count += 1
                prevmonth = month
        # print 'all'
    else:
        print 'Invalid timeframe'
    # Take time frame and grab 30 evenly-spaced data points - Xuan
    # Retrieve those data points from database x30 - Brian
    # print 30 data points - Xuan
    # print "testgraph"
    print plot_data


# Takes a search query and searches the database
def search(query):

    vals = query.split(',')
    low = float(vals[0])
    high = float(vals[1])

    # Open database connection
	
    conn = mysql.connector.connect(host = '162.221.219.6', user = 'test', password ='cs407test',
                           database = 'stock_info',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute(' SELECT * FROM stocks WHERE Low > %s AND High < %s  ORDER by Low '
                   , [low, high])

    # fetch all of the rows from the query

    data = cursor.fetchall()
    my_list = list()
    print ('Name, Symbol, Low, High, Date')

    # print the rows

    s = "Name	Symbol	Low	High	Date <br />"
    for row in data:
        print (row[0], row[1], row[2], row[3], row[4])
        s = s + str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]) \
            + ' ' + str(row[3]) + ' ' + str(row[4]) + '<br />'

    # disconnect from server

    conn.close()

def main():
    #test driver
    #singlestock("AAL")
    #print extractDate("1234-56-78", "DAY")
    graph("AAL", "1 month")
    search("1,4")
    # print "Current date and time using instance attributes:"
    # print "Current year: %d" % now.year
    # print "Current month: %d" % now.month
    # print "Current day: %d" % now.day
    # print "Current hour: %d" % now.hour
    # print "Current minute: %d" % now.minute
    # print "Current second: %d" % now.second
    # print "Current microsecond: %d" % now.microsecond
    # control statement
    if len(sys.argv) < 3:
        print "format error"
        exit(1)
    if sys.argv[1] == "single":
        singlestock(sys.argv[2])
    elif sys.argv[1] == "search":
        search(sys.argv[2])
    elif sys.argv[1] == "graph":
        if len(sys.argv) < 4:
            print "format error"
            exit(1)
        graph(sys.argv[2], sys.argv[3])
    else:
        print "format error"
        exit(1)


if __name__ == '__main__':
    main()
# def get_historical_price(time_frame):
#     if(time_frame=='')
#get_current('AAL')
