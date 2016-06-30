#!/usr/bin/env python
#import mapreduce.py
import random
import socket
import sys
import pickle
        

#class Worker:


Map_Input={}
Mapper_Output={}
Merged_data_values={}
Reducer_output={}

		
def Initialize():
        output={}
        gender=['man#','woman#']
        for i in range(1,11):
                g=random.choice(gender)
                output.update({random.randint(500000,600000):g.replace('#','%s'%i)})
        return output
		
def Map(map_input):
        output={}
        gender=['man#','woman#']
        for i in range(len(map_input)):
                g='woman%s'%i
                if g in map_input.values():
                        output.update({gender[1].replace('#','%s'%i):1})
                else:
                        output.update({gender[0].replace('#','%s'%i):1})
        return output
	
	
def Reduce(reduce_input):
        output={}
        gender=['man','woman']
        m=0
        f=0
        for i in range(len(reduce_input)):
                g='woman%s'%i
               # print(g)
                if g in reduce_input.keys():
                        f=f+1
                        #print('woman found')
                else:
                        m=m+1
                        #print('man found')
        output.update({gender[0]:m})
        output.update({gender[1]:f})
        return output

		
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
#Sending Ready message to server
message='Ready'
s.send(message.encode())
print('Message "%s" send\n' %message)
while 1:
        #Receiving Message from Master 
        Master_message = s.recv(4096)
        Master_message=Master_message.decode()
        print ('Message from Master Received')

        #Checking Master's Messages

        if Master_message=='Run_Init':
        	# Stage Iniatialize : Reading tags within the range of the worker                      
                Map_Input.update(Initialize())
                #Sending message "Init OK"
                message= 'Init_OK'
                print(Map_Input)
                try :
                        #Set the whole string
                	s.sendall(message.encode())
                	print('1.sent init ok\n')
                except socket.error:
                        #Send failed
                        print ('Sending Message Init_OK failed')
                        sys.exit()	
        elif Master_message=='Run_Map':
                # Stage Map : Keeping only male/female values extracting EPC values
                Mapper_Output.update(Map(Map_Input))
                print(Mapper_Output)
                #Sending message "Map OK"
                message= 'Map_OK'
                try :
                        #Set the whole string
                        s.sendall(message.encode())
                        print('2.sent map ok\n')
                except socket.error:
                        #Send failed
                        print ('Sending Message Map_OK failed')
                        sys.exit()	
        elif Master_message=='Run_Shuffle':
                try :
                        #Serialize data
                        s.sendall(pickle.dumps(Mapper_Output))
                        print('3.sent dictionary Mapper output\n')
                except socket.error:
                        #Send failed
                        print ('Sending Mapper_Output failed')
                        sys.exit()
                #Sending message "Shuffle OK"
                message= 'Shuffle_OK'
                print('4.sent shuffle ok\n')
                try :
                        #Set the whole string
                        s.sendall(message.encode())
                except socket.error:
                        #Send failed
                        print ('Sending Message Shuffle_OK failed')
                        sys.exit()
		
        elif Master_message=='Run_PrepareReduceInput':
                try:
                        Merged_data_values=pickle.loads(s.recv(4096))
                        print('5.Received merged data\n')
                        print(Merged_data_values)
                except socket.error:
                        print ('Reiveiving Data failed')
                #Sending message "PrepareReduce OK"
                message= 'PrepareReduce_OK'
                try :
                        #Set the whole string
                        s.sendall(message.encode())
                        print('6.sent prepare reduce ok\n')
                except socket.error:
                        #Send failed
                        print ('Sending Message PrepareReduce_OK failed')
                        sys.exit()
		
        elif Master_message=='Run_Reduce':
                Reducer_output=Reduce(Merged_data_values)
                try :
                        #Serialize data
                        s.sendall(pickle.dumps(Reducer_output))
                        print('7.reduced input sent\n')
                except socket.error:
                        #Send failed
                        print ('Sending Reducer_output failed')
                        sys.exit()
                #Sending message "Reduce OK"
                message= 'Reduce_OK'
                try :
                        #Set the whole string
                        s.sendall(message.encode())
                        print('8.sent reduce ok\n')
                        break
                except socket.error:
                        #Send failed
                        print ('Sending Message Reduce OK failed')
                        sys.exit()
        else:
                print ('Not valible message')
                break
    
s.close()






