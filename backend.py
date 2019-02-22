#print "hello world"
from StringIO import StringIO
# import pycurl
import certifi
import requests
import csv
import sys

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
#
#     for row in reader:
#         print row[0]

# a list holding all company symbols
company_list=[]

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
    reader = csv.reader(data.text.splitlines())
    for row in reader:
        print row

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
        #print row
    # update database with price for each day - Brian
	#call add_stock
	return
	
def add_stock(name , symbol, low, high , date):
	conn = mysql.connector.connect(host = '192.168.1.134', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
	cursor = conn.cursor()
	#print ("writing to db")
	cursor.execute("INSERT INTO stocks(Name, Symbol, Low, High, Date ) VALUES (%s,%s, %s, %s, %s)", [name , symbol, low, high , date])
	#print ("wrote to db")
	conn.commit();
	conn.close();
	return processed_text

def get_stock(ticker):
	conn = mysql.connector.connect(host = '192.168.1.134', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
	cursor = conn.cursor()

	cursor.execute("SELECT * from stocks WHERE ticker = %s ORDER by timestamp DESC", [ticker])
	data = cursor.fetchall() 
	for row in data:
		print (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])

	conn.commit();
	conn.close();

# Retrieve current data for single stock, return it to be displayed, and update database with historical daily price info
def singlestock(stock_symbol):
	conn = mysql.connector.connect(host = '192.168.1.134', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
	cursor = conn.cursor()
	print (stock_symbol)
	cursor.execute("SELECT * FROM Stocks WHERE Symbol = %s",[stock_symbol])
	# gets the number of rows affected by the command executed
	data = cursor.fetchall()
	count = 0
	
	for row in data:
		print (row[0])	
		count = count + 1
	if count == 0:
		print "It does not exist"
	else:
		print "It does exist"
	#
	#print "It Does Not Exist"
	#else:
	#	print "It Does Exist"
	# if data does not already exist in database - Brian
	#get_daily(stock_symbol)
	# get_current(stock_symbol)?
	# print current - Xuan
	# else
	#get_current(stock_symbol)
	# print current data - Xuan
    

# Return price points for graph
def graph(stock_symbol,  timeframe):

    if timeframe=='1 month':
        print '1 month'
        # take a point every day for 1 month
    elif timeframe=='3 month':
        print "6 month"
    elif timeframe=='3 year':
        print '3 year'
    elif timeframe=='all':
        print 'all'
    else:
        print 'error'
    # Take time frame and grab 30 evenly-spaced data points - Xuan
    # Retrieve those data points from database x30 - Brian
    # print 30 data points - Xuan
    print "testgraph"


# Takes a search query and searches the database
def search(query):

    vals = query.split(',')
    low = float(vals[0])
    high = float(vals[1])

    # Open database connection
	
    conn = mysql.connector.connect(host = '192.168.1.134', user = 'test', password ='cs407test', database = 'stock_info',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute(' SELECT * FROM stocks WHERE close > %s AND close < %s  ORDER by close '
                   , [low, high])

    # fetch all of the rows from the query

    data = cursor.fetchall() 
    # print the rows
    s = "Name	Symbol	Low	High	Date <br />"
    for row in data:
		print (row[0])
    #    print (row[0], row[1], row[2], row[3], row[4])
    #    s = s + str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]) \
    #        + ' ' + str(row[3]) + ' ' + str(row[4]) + '<br />'

    # disconnect from server

    conn.close()



			
# control statement



def main():
    #test driver
    get_stock('RAT')
    ##get_daily("AAL")
    #graph("AAL", "1 month")
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
