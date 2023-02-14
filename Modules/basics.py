# Modules - is file that containce refference to another file to build this module

# Import can be done: from Example.sales import calc_shipping, calc_tax or: import example.sales

from example.sales import calc_shipping
from example import sales

sales.calc_shipping()
