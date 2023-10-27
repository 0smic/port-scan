from socket import *
import time
import argparse
import sys

parser = argparse.ArgumentParser(description="Scan all the open port of specific ip")

parser.add_argument( # Argument to collect ip address to scan
    "-ip",
    nargs=1,
    help="Ip of the device that you need to scan the open port"
)
parser.add_argument( # Argument to collect the web_name to scan
    "-web",
    nargs=1,
    help="Full name of the web to scan open port"
)

args = parser.parse_args()


start_time = time.time()

class Scan_PORT:
    def __init__(self,target):
        self.target = target
        self.socket = socket(AF_INET, SOCK_STREAM)

    def ip_scan(self):
        for i in range(1, 6000): #create loop to check the port is open or not
            conn = self.socket.connect_ex((self.target, i))
            if (conn == 0):
                print(f"port {i}: OPEN")
            self.socket.close()
        print("Process finished")


if args.ip:
    target = args.ip[0]

elif args.web:
    web_name = args.web[0]
    try:
        target = gethostbyname(web_name) #get the ip addr of the web
    except gaierror: #check error if couldn't find the ip addr of the web
        print(f"Error: Could not resolve hostname '{web_name}' to an IP address.")
        sys.exit(1)
else:
    print("You to specifiy the ip address")
    sys.exit(1)

scan_port = Scan_PORT(target)
scan_port.ip_scan()
