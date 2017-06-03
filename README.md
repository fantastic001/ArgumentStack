ArgumentStack is an Python library for easy parsing and making useful and powerful command-line apps. 

This library is initially aimed to be used in [Mako CLI wrapper](https://github.com/fantastic001/Mako).

Example:
	
	#!/usr/bin/python 
	from ArgumentStack import * 
	
	import sys
	stack = ArgumentStack()
	
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
