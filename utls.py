from itertools import tee


def scrap(wrds):
    s = set()
    for wrd in wrds:
        splited_wrd = wrd.split(' ')
        for i in range(len(splited_wrd)):
            wrds_indexed = splited_wrd[i]
            if ('@' in wrds_indexed and '.' in wrds_indexed) and (len(wrds_indexed) > 7):
                s.add(wrds_indexed)
    yield from s


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
