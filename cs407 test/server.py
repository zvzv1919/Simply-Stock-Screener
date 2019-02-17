import pymysql
import requests

import simplejson as json
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('template.html')




@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/list-stocks/')
def list_stocks():


	# Open database connection
	conn = pymysql.connect("DESKTOP-38PNH3Q","root","cs407sss","stock_info", 3306 )

	cursor = conn.cursor()

	cursor.execute(""" SELECT * FROM stocks ORDER by Low """)
	# fetch all of the rows from the query
	data = cursor.fetchall ()
	my_list = list()
	print ("Name, Symbol, Low, High, Date")
	# print the rows
	s = "Name	Symbol	Low	High	Date <br />"
	for row in data :
		print (row[0], row[1], row[2], row[3], row[4])
		s = s + str(row[0]) + '		' + str(row[1])  + '	' + str(row[2])  + '	' + str(row[3])  + '	' + str(row[4])  + '<br />'
	

	# disconnect from server
	conn.close()
	
	

	return s
	
@app.route('/add', methods=['POST'])
def add_stock():
	text = request.form['text']
	processed_text = text.upper()
	conn = pymysql.connect("DESKTOP-38PNH3Q","root","cs407sss","stock_info", 3306 )
	cursor = conn.cursor()
	print ("writing to db")
	cursor.execute("INSERT INTO stocks(Name, Symbol, Low, High, Date ) VALUES ('test3',%s, 12.10, 14.22, '2018-11-21')", [processed_text])
	print ("wrote to db")
	conn.commit();
	conn.close();
	return processed_text

@app.route('/search-stocks/', methods=['POST'])
def search_stocks():
	text = request.form['text']
	processed_text = text.upper()
	vals = processed_text.split(',')
	low = float(vals[0]);
	high = float(vals[1]);
	# Open database connection
	conn = pymysql.connect("DESKTOP-38PNH3Q","root","cs407sss","stock_info", 3306 )

	cursor = conn.cursor()

	cursor.execute(" SELECT * FROM stocks WHERE Low > %s AND High < %s  ORDER by Low ", [low,high])
	# fetch all of the rows from the query
	data = cursor.fetchall ()
	my_list = list()
	print ("Name, Symbol, Low, High, Date")
	# print the rows
	s = "Name	Symbol	Low	High	Date <br />"
	for row in data :
		print (row[0], row[1], row[2], row[3], row[4])
		s = s + str(row[0]) + '		' + str(row[1])  + '	' + str(row[2])  + '	' + str(row[3])  + '	' + str(row[4])  + '<br />'
	

	# disconnect from server
	conn.close()
	
	

	return s

if __name__ == '__main__':
  app.debug = True
  app.run(debug=True)