#print "hello world"
from StringIO import StringIO
import pycurl
import certifi

buffer = StringIO()
c = pycurl.Curl()

#Place the API request here
c.setopt(c.URL, 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&'
                'outputsize=full&apikey=PTF07M1M1UTX6RCF')
c.setopt(c.CAINFO, certifi.where())
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

#respond from Alpha Vantage in JSON form
body = buffer.getvalue()
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
print(body[:10000])

buffer2=StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&'
                'outputsize=full&apikey=PTF07M1M1UTX6RCF')
c.setopt(c.CAINFO, certifi.where())
c.setopt(c.WRITEDATA, buffer2)
c.perform()
c.close()

body2 = buffer2.getvalue()
print(body2[:10000])