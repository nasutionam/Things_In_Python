import socket

hostname = input("Input hostname : ")
ipaddr = socket.gethostbyname(hostname)
print("IP Address = %s" % ipaddr)