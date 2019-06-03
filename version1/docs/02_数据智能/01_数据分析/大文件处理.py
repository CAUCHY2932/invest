# coding:utf-8


file = open('test.txt')
while True:
    line = file.readline()
    if not line:
        break
    print(line, end='')


file = open('test.txt', 'rb')
while True:
    chunk = file.read(10)
    if not chunk:
        break
    print(chunk, end='')
