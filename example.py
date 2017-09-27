#!/usr/bin/python 
from src import * 


import sys
stack = ArgumentStack("Wrong command")

stack.pushCommand("hello")
stack.pushCommand("world")
stack.assignAction(lambda: print("hello world!"), "say hello to world")
stack.pop()
stack.pushCommand("to")
stack.pushVariable("name")
stack.assignAction(lambda name: print("Hello, %s" % name), "say hello to somebody")
stack.popAll()
stack.pushCommand("help")
stack.assignAction(lambda: print(stack.getHelp()), "Get help")
stack.execute(sys.argv)
