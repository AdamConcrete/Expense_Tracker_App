import sqlite3 as db
from datetime import datetime

def init():
	'''
	initialize a new database to store the expenditures
	'''
	conn = db.connect("expense_tracker.db")
	cur = conn.cursor()
	sql = '''
	create table if not exists expenses (
		amount number,
		category string,
		message string,
		date string
		)
	'''
	cur.execute(sql)
	conn.commit()

def log(amount, category, message=""):
	'''
	logs the expenses in the database.
	'''
	date = str(datetime.now())
	conn = db.connect("expense_tracker.db")
	cur = conn.cursor()
	sql = '''
	INSERT INTO expenses VALUES(
		 {},
		'{}',
		'{}',
		'{}'
		)
	'''.format(amount,category,message,date)
	cur.execute(sql)
	conn.commit()


def view(category=None):
	'''
	Returns a list of all or selected expenses. Category can be specified.
	'''
	conn = db.connect("expense_tracker.db")
	cur = conn.cursor()
	if category:
		sql = '''
		select * from expenses  where category = '{}'
		'''.format(category)
		sql2 = '''
		select sum(amount) from expenses where category = '{}'
		'''.format(category)
	else:
		sql = '''
		select * from expenses
		'''.format(category)
		sql2 = '''
		select sum(amount) from expenses
		'''.format(category)

	cur.execute(sql)
	results = cur.fetchall()
	cur.execute(sql2)
	total_amount = cur.fetchone()[0]

	return total_amount, results


#print (view())
