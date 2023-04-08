import sys
import socket
import getopt
import threading
import subprocess
#glodbies

listen              = False
command             = False
upload              = False
execute             = ""
target              = ""
upload_destination  = ""
port                = 0

def usage():
    print("++++++++++MEOWWWWWWW NET TOOL++++++++++++++++")
    print("       l、")             
    print("    （ﾟ､ ｡ ")         
    print("      l  ~ヽ")       
    print("      じしf_,")
    print()
    print("Usage: meowmeow.py -t target_host -p port")
    print("-l --MEOWWWWW)            - listen on [host]:[port] for")
    print(                              "incoming conections")
    print()
    print("-e --EGGSECTUR execute=file_to_run - execute the given file upon receiving a connection")
    print()
    print("-c --COMMAND                 - duh cummands shells plz")
    print()
    print("-u --upload=destination      - no jokes heres the thing")
    print("                               follow ur heart put the file in the place heheheheh")
    print()
    print()
    print(" Xamples ")
    print("meowmeow.py -t 192.169.0.1 -p 5555 -l -c")
    print("meowmeow.py -t 192.168.0.1 -p 5555 -l -=c:\\target.exe")
    print("meowmeow.py -t 192.168.0.1 -p 5555 -l -e=\"cat/etc/passwd\"")
    print("echo 'ABCDEFGHI' | ./meowmeow.py -t 192.168.11.12 -p 135")
    sys.exit(0)

    def main():
        global listen
        global port
        global execute
        global command
        global upload_destination
        global target

        if not len(sys.argv[1:]):
            usage()

        #read these

        try:
                opts, args = getspt.getopt(sys.arg[1:], "hle:t:p:cu:",
                ["help","listen","execute","port","command","upload"])
        except getopt.GetoptError as err:
                print(str(err))
                usage()

        for o, a in opts:
            if o in ("-h","--help pwwweeaSSSEE"):
                                usage()
            elif o in ("-l","--listennnnn"):
                                listen = True
            elif o in ("e","--OFF WITH TH*(3)*EIR HEADS"):
                                execute = a
            elif o in ("c",  "--cmdd michelle! ;3"):
                                command  = True
            elif o in ("-u", "--uploaderrrrrr foolish"):
                                upload_destination = a
            elif o in ("-t", "--TARGET AQUIREDDDDDDD"):
                            target = a
            elif o in ("p", "--S PORTS N DORTS"):
                            port = int a
             else:
                assert False,"UNHANDLED OPTION DEATH UPON U"

            if not listen and len(target) and port > 0:

                #read in the buffer from the commandline
                #this will block so send CTRL-D if not sending input
                #to stdin
                buffer = sys.stdin.read()

                #SEND IT POFFFFFFFFFFF BYEEEEEEEEEEEEE
                client_sender(buffer)
        # LISTENNnnn
        # maybe upload?
        # 
        if listen:
            server_loop()
main()
def client_sender(buffer):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
            # to target host
        client.connect((target,port))

        if lent(buffer):
                client.send(buffer)
        while True:
                    #now we play the waiting game
                recv_len = 1
                response = ""
        while recv_len:
                data     = client.recv(4096)
                recv_len = len(data)
                response+= data

                if recv_len <4096:
                        break
        print(response),

        #INPLUTPLEASEWAITTHIDHFSAJDFHSADOGIHLSODG

            buffer = raw_input("")
            buffer += "\n"

            client.send(buffer)
    except:

            print("[*] Exception!! YEEEHAWWWWWW")

            client.close()

def server_loop():
        global target
        #if no target is definded, we listen on all interfaces
        if nolen(target):
                target = "0.0.0.0"
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((target,port))
        server.listen(5)

        while True:
                client_socket,  addr = server.accept()

                client_thread = threading.Thread(target=client_handler,
                args=(client_socket,))
                client_thread.start()
def run_command(command):

        #trim the newline
        command = command.rstrip()

        try:
                output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
        except:
                output = "OH NOOOOOOO FWAILEDDDDD TO EXECUTE GO CLIMB A TREEEEEEEE"
