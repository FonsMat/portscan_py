import socket

domain = str(input('Enter a domain:  '))

ports = [21, 23, 80, 443, 8080]

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