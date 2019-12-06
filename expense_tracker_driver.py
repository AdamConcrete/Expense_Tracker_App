usage = '''
Expense Tracker CLI.
Usage:
  python expense_tracker_driver.py init
  python expense_tracker_driver.py view [<view_category>]
  python expense_tracker_driver.py <amount> <category> [<message>]
'''

from docopt import docopt
from expense_tracker import *
from tabulate import tabulate

args = docopt(usage)

if args['init']:
    init()
    print("User Profile Created")

if args['view']:
    category = args['<view_category>']
    amount, results = view(category)
    print("Total expense: ", amount)
    print(tabulate(results))

if args['<amount>']:
    try:
        amount = float(args['<amount>'])
        log(amount, args['<category>'], args['<message>'])
    except:
        print(usage)