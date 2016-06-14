#!/usr/bin/env python
#import mapreduce.py
import random
import socket
import sys
import pickle
        

class Worker:

	def __init__(self):
		self.Map_Input={}
		self.Mapper_Output={}
		self.Merged_data_values={}
		self.Reducer_output={}
		
	def Initialize(self,number):
		for i in range(0,number):
			self.Map_Input.update({random.randint(1,2),1})
		
	#def Map(self,map_input):
	
	
	#def Reduce(self,reduce_input):

		
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
port = 10000
try:
	host = socket.gethostname()
except s.gaierror:
    #could not resolve
    print ('Hostname could not be resolved. Exiting...')
    sys.exit()	

# connection to hostname on the port.
s.connect(('127.0.0.1', 5000))    	
#Receiving Message from Master 
Master_message = s.recv(4096)	
print ('Message from Master Received')

#Checking Master's Messages

if Master_message=='Run_Init':
	# Stage Iniatialize : Reading tags within the range of the worker                      
	Initialize(self,10)
	#Sending message "Init OK"
	message= 'Init_OK'
	try :
		#Set the whole string
		s.sendall(message)
	except socket.error:
		#Send failed
		print ('Sending Message Init_OK failed')
		sys.exit()
		
elif Master_message=='Run_Map':
	# Stage Map : 
	#self.Mapper_Output=Map(self,Map_Input)
	#Sending message "Map OK"
	message= 'Map_OK'
	try :
		#Set the whole string
		s.sendall(message)
	except socket.error:
		#Send failed
		print ('Sending Message Map_OK failed')
		sys.exit()
		
elif Master_message=='Run_Shuffle':
	try :
		#Serialize data
		dict0=pickle.dumps(self.Mapper_Output)
		s.sendall(dict0)
	except socket.error:
		#Send failed
		print ('Sending Mapper_Output failed')
		sys.exit()
	#Sending message "Shuffle OK"
	message= 'Shuffle_OK'
	try :
		#Set the whole string
		s.sendall(message)
	except socket.error:
		#Send failed
		print ('Sending Message Shuffle_OK failed')
		sys.exit()
		
elif Master_message=='Run_PrepareReduceInput':
	try:
		dict2=pickle.loads(s.recv(4096))
	except socket.error:
		print ('Reiveiving Data failed')
	self.Merged_data_values=dict2
	
	#Sending message "PrepareReduce OK"
	message= 'PrepareReduce_OK'
	try :
		#Set the whole string
		s.sendall(message)
	except socket.error:
		#Send failed
		print ('Sending Message PrepareReduce_OK failed')
		sys.exit()
		
elif Master_message=='Run_Reduce':
	self.Reducer_output=Reduce(self,Merged_data_values)
	try :
		#Serialize data
		dict3=pickle.dumps(self.Reducer_output)
		s.sendall(dict3)
	except socket.error:
		#Send failed
		print ('Sending Reducer_output failed')
		sys.exit()
	#Sending message "Reduce OK"
	message= 'Reduce_OK'
	try :
		#Set the whole string
		s.sendall(message)
	except socket.error:
		#Send failed
		print ('Sending Message Reduce OK failed')
		sys.exit()
else:
	print ('Not valible message')
    
s.close()






