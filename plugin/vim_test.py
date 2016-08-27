import vim
import time
import threading

def update_buffer():
	vim.current.buffer.append("Hello world")
	vim.current.buffer.append("Hello world")
	vim.current.buffer.append("Hello world")
	vim.current.buffer.append("Hello world")

class MyThread (threading.Thread): 
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		for _ in range(10):
			vim.current.buffer.append("Hello world")
			time.sleep(1)
			vim.command('redraw')

def sleep_print():
	thd = MyThread()
	thd.start()
