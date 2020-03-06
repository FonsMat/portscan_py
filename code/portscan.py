import socket 
#network socket is an end point of a communication flow between processes through a computer network.

domain = str(input('Enter a domain:  '))

#the program will only check these ports:
ports = [21, 23, 80, 443, 8080] #you can change if you want

for port in ports:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        code = client.connect_ex((domain, port))
    except:
        print('Enter a valid domain')
    else:
        if code == 0:
            print(port, 'OPEN')
        else:
            print(port, 'CLOSED')
