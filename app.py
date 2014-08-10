from sys import argv
from Tkinter import Frame, Tk, Frame, BOTH, Entry, Button, RIGHT, StringVar
from ttk import Label, Scale, Style
from chat_lib import Communication
import threading

class thread_recv_msg(threading.Thread):
	def __init__(self,my_port):
		threading.Thread.__init__(self)
		self.my_port = my_port
	def run(self):
		global my_communication
		while True:
			msg_packet = my_communication.recv()
			app.msg_recieved(msg_packet)
		
class Connection:
	ip=''
	my_port = 0
	send_port = 0
	def send_msg(self,msg):
		my_communication.send(msg)
	def recv_msg(self):
		thread_recv = thread_recv_msg(self.my_port)
		thread_recv.start()		

class ak():


	
	
	def send_msg(self):
		global my_connection
		while True:

			message=raw_input()
			my_connection.send_msg(message)
		
	def msg_recieved(self,msg_packet):
		print msg_packet[1]+": "+msg_packet[0]
		

if len(argv)!=4:
	print "Usage: python app.py <ip> <port to listen> <port to send>"
	exit(0)

my_communication = Communication(argv[1],int(argv[2]),int(argv[3]))

my_connection = Connection()
my_connection.recv_msg()
my_connection.ip = argv[1]
my_connection.my_port = int(argv[2])
my_connection.send_port = int(argv[3])
        

app = ak()
app.send_msg()

