from chat_lib import Communication
from sys import argv
import threading

class thread_recv_msg(threading.Thread):
	def __init__(self,my_port):
		threading.Thread.__init__(self)
		self.my_port = my_port
		self.my_communication = Communication(None,9491,None)
	def run(self):
		while True:
			msg_packet = self.my_communication.recv()
			''' send the recieved packet to the main_loop_obj '''
			'''main_loop_obj.msg_recieved(msg_packet)'''
			print msg_packet

class group_chat():
	def __init__(self,group_id):
		if group_id == None:
			# TODO generate self.group_id
			pass
			
		else:
			self.group_id = group_id
		# TODO create UI
		pass
		
	def add( tupple_ip ):
		# TODO send "GRP ADD self.group_id" to all IPs in tupple_ip
		pass
		
	def send(self,msg):
		# TODO send "MSG self.group_id ___" to self.ip
		pass

class private_chat():
	def __init__(self,ip):
		self.ip = ip
		# TODO create UI
		pass
		
	def send(self,msg):
		# TODO send "MSG PVT ___" to self.ip
		pass

class public_chat():
	def __init__(self):
		# TODO create UI
		pass
		
	def send(self,msg):
		# TODO send "MSG PUB ___" to all IPs in main_loop_obj.online_dict
		pass


class Connection:
	ip=''
	my_port = 0
	send_port = 0
	name=''
	def send_msg(self,msg):
		my_communication.send(msg)
	def recv_msg(self):
		thread_recv = thread_recv_msg(self.my_port)
		thread_recv.start()	


class main_loop():
	''' A dict for storing {'ip': 'name' }'''
	online_dict = {}
	
	''' object for public chat '''
	public_chat_obj = None
	
	''' A dict for storing {'ip': private_chat object} for connected IPs '''
	private_chat_obj_dict = {}
	
	''' A dict for storing {'group_id': group_chat object} for groups '''
	group_chat_obj_dict = {}
	
	def __init__(self,name):
		# TODO create UI
	
		''' Start the thread for recieving messages '''
		thread_recv_msg(9491).start()
		
		# TODO send "RESPOND NAME" to all IP ports on network

	def msg_recieved(self,msg_packet):
		# TODO implement all message recieved protocols
		self.label_string.set(msg_packet[1]+":"+my_connection.name+": 			"+msg_packet[0])
		pass

my_connection = Connection()
if len(argv)!=5:
	print "Usage: python app.py <ip> <port to listen> <port to send> <handle>"
	exit(0)
my_connection.ip = argv[1]
my_connection.my_port = int(argv[2])
my_connection.send_port = int(argv[3])
my_connection.name=argv[4]
my_communication = Communication(my_connection.ip,my_connection.my_port,my_connection.send_port,my_connection.name)

my_connection.send_msg("hello")

my_connection.recv_msg()
		

