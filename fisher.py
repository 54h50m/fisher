
__author__ = '54h50m'
__date__ = '2018/7/5 22:16'

from flask import Flask, make_response
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')

@app.route('/book/search/<q><page>')
def search(q,page):
    # q:普通关键字 isbn
    # page

    isbn_or_key = is_isbn_or_key(q)

    pass


def helloo():
    return 'hello, Qiyue'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'], port=81)