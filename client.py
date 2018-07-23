#!/usr/bin/python3
'''
AUTHOR: ED-209-Mk7
DATE: 07/10/2018
PURPOSE:  Take a Client model from a class last year and some style and encryption.
STATUS:  Much Coffee and motivation.
USAGE: client.py [Server IP] [Server Port]
CAUTION: If you run this as SUDO / ROOT that is the level of access the client will have.
'''

import socket, sys, os, re, time, subprocess

print('\nClient Initializing...\nPUNCH IT CHEWIE\n') #Later make Random Welcome

def argsCheck():# A check if the user is giving a CLI arg
    global SERVER, PORT #Set up global var PORT
    if len(sys.argv) != 3: #If anything other than 2 arguments is given...
        print('\nUSAGE: '+sys.argv[0]+' [Server IP] [Server Port]\n')
        sys.exit(1)
    else:
        SERVER = sys.argv[1]
        PORT = sys.argv[2]
        if SERVER.count('.') == 3:
            try:
                socket.inet_aton(SERVER)
                print('[+] Valid IP Given for Server Address...')
            except:
                print('[-] IP is detected as invalid. Exiting.\n')
                sys.exit(1)
        else:
            print('[-] IP does not appear valid. Exiting...\n')
            sys.exit(1)
        if PORT.isdigit() and 1 <= int(PORT) <= 65535: #Args are good, but is it valid?
            print('[+] Valid Port Number Given...')
            PORT = int(sys.argv[2])
        else:
            print('\n[!] Valid Server Address and Port are required.\n')
            sys.exit(1)

USER = os.getlogin()
print('[i] Local user detected as:',USER)

def connectUp():
    global SERVER, PORT, RUSER
    SERgjfjhVER = socket.socket()
    try:
        SERVER.connect((SERVER,PORT))
    except Exception as err:
        print('[-] An error occured while trying to connect to '+SERVER+':'+PORT)
        print(str(err)+'\n')
        sys.exit(1)
    print('[+] Connected to',SERVER+':'+str(PORT))
    print('[!] Be Advised: Though it shows',USER,'is connected,\n     you are in fact running as the user who initiated the server.')
    #now reach out and retrieve whoami


'''def linkOps():
    while True:
        cmd_input = raw_input('['+USER+)
'''

argsCheck()
connectUp()
sys.exit(0)


'''
TCP_IP = '127.0.0.1'
TCP_PORT = 8090 #Reserve a port
BUFFER_SIZE = 1024
MESSAGE_TO_SERVER = "Hello, World!"

try:
    #Create an AF_INET (IPv4), STREAM socket (TCP)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('Error occurred while creating socket. Error code: ')
    print((err)) #print output of the error.
    sys.exit();
#try connecting
try:
    tcp_socket.connect((TCP_IP, TCP_PORT))
except Exception as err:
    print('An error occured while trying to connect to '+str(TCP_IP)+':'+str(TCP_PORT))
    print(str(err)+'\n')
try :
    #Sending message
    tcp_socket.send(MESSAGE_TO_SERVER.encode())
except socket.error as err:
    print('Error occurred while sending data to server.')
    print(str(err))#print the output of the error.
    sys.exit()

print('Message to the server send successfully')
'''
