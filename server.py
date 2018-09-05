# -*- coding: utf-8 -*-
# @Author: xiweibo
# @Date:   2018-09-04 16:13:26
# @Last Modified by:   xiweibo
# @Last Modified time: 2018-09-04 17:27:51
"""
服务端代码
"""
from concurrent import futures
from SimpleXMLRPCServer  import SimpleXMLRPCServer 
from SimpleXMLRPCServer  import SimpleXMLRPCRequestHandler
from SocketServer import ThreadingMixIn

__HOST = 'localhost'
__PORT = 8000

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2') #定义RPC接口的请求地址

class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
	pass

server = ThreadXMLRPCServer((__HOST, __PORT), requestHandler = RequestHandler, allow_none=True)
server.register_introspection_functions() 

# server.register_function(func, 'add') func是服务点定义的函数，add是客户端调用时用的函数
server.register_function(pow)

def adder_function(x, y):
	return x + y
server.register_function(adder_function, 'add')

class MyFuncs:
	def div(self, x, y):
		return x //y


server.register_instance(MyFuncs()) #将类中的方法全部注册到server端

server.serve_forever()