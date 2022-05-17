from itertools import tee
import re

def scrap(wrds):
    if isinstance(wrds, str):
        wrds = wrds.split(' ')
    data = set()
    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    for wrd in wrds:
        matches = pattern.search(str(wrd))
        try:
            data.add(matches.group(0))
        except AttributeError:
            pass
    yield from data



def files():
    with open('insert.txt', 'r', encoding='utf-8') as file:
        yield from file


def inserter(lst):
    scraped = scrap(lst)
    display, scraped_list = tee(scraped, 2)
    with open('output.txt', 'w') as file:
        for i in scraped_list:
            file.write(f'{i}\n')
    print('\n-----------------------------------')
    print('Email List:- \n')
    try:
        for _ in range(10):
            print(next(display))
    except StopIteration:
        pass


def mode(mode):
    if mode is 'txt':
        return inserter(lst=files())
    elif mode is 'input':
        return inserter(lst=multi_input())


def multi_input():
    print('''
|----------------------------------------------------------------|
|                                                                |
|     Press << Ctrl + Z >> And Hit Enter To Finish The List!     |
|                                                                |
|----------------------------------------------------------------|\n''')
    print('Enter The Text: \n')
    try:
        while True:
            wrd = input()
            yield wrd
    except EOFError:
        pass
