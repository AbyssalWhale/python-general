# Modules - is file that containce refference to another file to build this module

# Import can be done:
# Abosult import: from example.shopping import sales - the use sales
# Relative import: from ..Modules import basics
# Another used: from Example.sales import calc_shipping, calc_tax or: import example.sales

from example.shopping.sales import calc_shipping
from example.shopping import sales
