#! coding: utf-8
from twisted.internet.defer import Deferred
def got_poem(res):
    print ('Your poem is served:')
    print res
def poem_failed(err):
    print err.__class__
    print err
    print ('No poetry for you.')
def aa(a, b):
    print("aaa")
    print(a)
    print(b)
d = Deferred()
# add a callback/errback pair to the chain
d.addCallback(got_poem) # 第一个执行时第一个参数固定为 callback传入的参数
d.addCallback(aa, "hhhh")  # 第二个执行时第一个参数固定为 None
# fire the chain with an error result
d.callback("abc")  # abc传入 got_poem
