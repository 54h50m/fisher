# _*_ coding: utf-8 _*_
__author__ = '54h50m'
__date__ = '2018/7/9 21:40'

    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些‘_’
def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('_', '')
    if '_' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key
