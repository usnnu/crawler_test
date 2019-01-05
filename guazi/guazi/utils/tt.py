#coding:utf-8

"""
----------------------------------------
    file name:
    description:
    
author:
    date:
    

----------------------------------------
    change:
    
----------------------------------------

"""
import time
import asyncio
import datetime

now = lambda: time.time()
'''
# statement: a coroutine obj
async def do_some_work(x):
    print('waiting:',x)

start = now()
coroutine = do_some_work(2)
print(coroutine)

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('Time cost:',now()-start)

'''
'''
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('word')

#print(asyncio.get_event_loop())

loop_policy = asyncio.get_event_loop_policy()
#l = asyncio.set_event_loop_policy()
print(loop_policy)

loop = asyncio.get_event_loop()
loop.run_until_complete()
#print(asyncio.SelectorEventLoop)

'''

'''
import asyncio

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()

print(datetime)
print(asyncio.wait)

'''

# 简单使用

import asyncio
import time

async def get_html(url):
    print("start get url.")
    await asyncio.sleep(2)
    print('end get url')

def simple_test1():
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_html('http://www.baidu.com'))
    print(time.time() - start_time)


def simple_test2():
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html('http://www.baidu.com') for i in range(10)]
    print(tasks[1])
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)
    print(tasks[1])





if __name__ == '__main__':
    simple_test2()

