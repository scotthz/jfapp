import os
import socket
import sys
from flask import Flask

app = Flask(__name__)
host_ip = 'undefined IP'
host_name = 'undefined hostname'

@app.route("/")
def root():
    return "<h1 style='color:blue'>Hello from {} ({}, {})</h1>".format(os.uname().nodename, host_name, host_ip)

def get_host():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip, host_name
    except:
        print("Unable to get Hostname and IP")

if __name__ == '__main__':
    host_ip, host_name = get_host()
    print(host_name, file=sys.stderr)
    app.run(host=host_ip, port='5000')
