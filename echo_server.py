#!/usr/bin/env python 

import socket
import sys
import pickle

map_output={}
reduced_output={}

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 5000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
print ('waiting for a connection\n')
connection, client_address = sock.accept()

while True:
    data = connection.recv(4096)
    data=data.decode()
    print ('received "%s"' % data)
    if data=='Ready':
        print ('Sending Start Init Command\n')
        message1='Run_Init'
        connection.send(message1.encode())
    elif data=='Init_OK':
        print ('Init OK, sending run map command\n')
        message2='Run_Map'
        connection.sendall(message2.encode())
    elif data=='Map_OK':
        print ('Map OK, sending run shuffle command\n')
        message3='Run_Shuffle'
        #stelnei to mhnma 
        connection.sendall(message3.encode())
        #dexetai ta dedomena
        try:
            map_output=pickle.loads(connection.recv(4096))
            print('map output received')
            print(map_output,'\n')
        except socket.error:
            print ('Reiveiving Data failed')
    elif data=='Shuffle_OK':
        print ('Shuffle OK, sending run reduce command\n')
        message4='Run_PrepareReduceInput'
        #stelnei to mhnuma
        connection.sendall(message4.encode())
        #stelnei dedomena
        try:
            connection.sendall(pickle.dumps(map_output))
            print('merged data sent')
        except socket.error:
            #Send failed
            print ('Sending Message Shuffle_OK failed')
            sys.exit()
    elif data=='PrepareReduce_OK':
        print ('PrepareReduce OK, sending run Reduce command\n')
        message5='Run_Reduce'
        connection.sendall(message5.encode())
        #dexetai dedomena
        try:
            reduced_output=pickle.loads(connection.recv(4096))
            print('reduced output received')
        except socket.error:
            print ('Reiveiving Data failed')      
    elif data=='Reduce_OK':
        print ('Reduced Data:')
        print(reduced_output,'\n')
        break
    else:
        print ('no more data from' %client_address)
        break

connection.close()
