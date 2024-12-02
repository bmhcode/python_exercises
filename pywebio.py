# import openai
from pywebio import start_server
from pywebio.input import *
from pywebio.output import * # put_text, put_table
from pywebio.session import *
from pywebio.pin import *

put_text('BMH')

start_server(put_text, port = 5500, debug=True)

input('Press any key ...')