#!/usr/bin/python3
'''
AUTHOR: ED-209-Mk7
DATE: 07/10/2018
PURPOSE:  Take a Server model from a class last year and some style and encryption.
STATUS:  Much Coffee and motivation.
USAGE: server.py [Listening Port]
CAUTION: If you run this as SUDO / ROOT that is the level of access the client will have.
'''
import socket #Imported sockets module for networking
import os # To interact with OS
import sys # Clean exits and OS interaction
import subprocess

def argsCheck():# A check if the user is giving a CLI arg
    global PORT #Set up global var PORT
    if len(sys.argv) != 2: #If anything other than 1 argument is given...
        print('\nUSAGE: '+sys.argv[0]+' [TCP Listening port]\n')
        sys.exit(1)
    else:
        PORT = sys.argv[1]
        if PORT.isdigit() and 1 <= int(PORT) <= 65535: #Args are good, but is it valid?
            print('\n[+] Valid Port Number Given...')
            PORT = int(sys.argv[1])
        else:
            print('\n[!] Port number given was invalid.\n')
            sys.exit(1)

#define some vars globally that will be used in future functions
HOST = '127.0.0.1'
BUFFER_SIZE = 1024 #Normally use 1024, to get fast response from the server use small size
SERVER = socket.socket()

def socketStart():
    global SERVER, PORT
    try:
        print('[i] Attempting to bind to TCP Port:',str(PORT))
        SERVER.bind((HOST,PORT))
    except socket.error as err:
        print('An error occurred while attempting to bind a socket:')
        print(str(err)) #Print the actual error code
        sys.exit(1) # Exit as an error(1)
    print('[+] Success. Bound to TCP Port:',str(PORT),'\n')
    try:
        SERVER.listen(5) #Listen for up to 5 attepts
        # The first process is the netstat cmd
        netstatcmd = subprocess.Popen(['netstat','-antp'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        # Second is the grep process where its stdin is set to the netstatcmd output
        grepcmd = subprocess.Popen(['grep',str(PORT)], stdin=netstatcmd.stdout, stdout=subprocess.PIPE)
        # Close the Pipe
        netstatcmd.stdout.close()
        # Decode the output and strip the whitespace and other non print chars
        output = grepcmd.communicate()[0].decode().rstrip()
        print(output) # Print the output
        grepcmd.stdout.close() # Close this Pipe as well
    except error as err:
        print('[!] An error occurred while attempting to listen on TCP Port:',str(PORT))
        print(str(err))
        sys.exit(1)


def runServer():
    global SERVER, PORT
    while True:
        print('\n[+] Listening on TCP Port:',str(PORT))
        client, addr = SERVER.accept() #Accept incoming connections
        print('client:',str(client))
        print('addr:',str(addr))
        clientIP = addr[0]  #Client IP is the first object from received client data
        print('[+] Connection Accepted from:',str(clientIP))
        while True: #infinite loop to start after an incoming connection is accepted
            cmd = client.recv(1024) # Commands send by client
            if cmd: #Check for input from client
                # Execute the command and retain the stdout (the first obj of the tuple[0])
                clientCMD = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE).communicate()[0]
                client.sendall(clientCMD) #send output back to the client
            else:
                print('[+] Connection appears to have closed. Closing socket.')
                client.close() #Close the client
                break


def main():
    argsCheck()
    socketStart()
    runServer()
    sys.exit(0)

if __name__ == "__main__":
    main()
else:
    print('Imported...')
    main()








'''
try:
   #Create an AF_INET (IPv4), STREAM socket (TCP)
   tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
   print('Error occurred while creating socket.')
   print(str(err)+'\n')
   sys.exit()

try:
    tcp_socket.bind((TCP_IP, TCP_PORT))
    # Listen for incoming connections  (max queued connections: 2)
    tcp_socket.listen(2)
    print('Listening..')
except socket.error as err:
    print('An error occurred while attempting to bind a socket:')
    print(str(err))
    sys.exit()

#keep server alive
while True:
   connection, address = tcp_socket.accept()#open a socket and accept a connection
   print('Client connected: ',address)
   data = connection.recv(BUFFER_SIZE).decode()
   print("Message from client:", data)
   #connection.sendall("Thanks for connecting")  #Echo the message from client
'''
