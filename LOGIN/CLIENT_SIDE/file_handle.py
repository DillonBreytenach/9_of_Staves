import os
from cryptography.fernet import Fernet
from pathlib import Path

#CONNECTION__
import socket
import tqdm















class transmit():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.SEPARATOR = "<SEPARATOR>"
        self.BUFFER_SIZE = 4096 # send 4096 bytes each time s
     

        #CONNECT TO SOCKET
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print(e)
        self.host = '127.0.0.1'
        self.port = 8081
        
        try:
            self.sock.connect((self.host, self.port))
            print("[CONNECTED]")
        except Exception as e:
            print(e)
        try:
            self.sock.bind((self.host, self.port))
            print("BOUND")
        except Exception as e:
            print("SOCKET NOT BOUND : ",str(e))
            

        try:
            self.sock.listen(5)
            self.sock.setblocking(False)
        except Exception as e:
            print(e)    


        #def send_msg(self, filename):
         #   while True:
          #      self.sock.send(str(filename))
            
            #self.filesize = os.path.getsize(self.file_name)
            #progress = tqdm.tqdm(range(self.filesize), f"Sending {self.filename}", unit="B", unit_scale=True, unit_divisor=1024)
            #
            #try:
            #    #file_To_send
            #    
            #    self.sock.send(f"{self.filename}<SEPARATOR>{self.filesize}".encode())
            #    with open(self.filename, "rb") as f:
            #        while True:
            #            # read the bytes from the file
            #            bytes_read = f.read(self.BUFFER_SIZE)
            #            if not bytes_read:
            #                # file transmitting is done
            #                break
            #            # we use sendall to assure transimission in 
            #            # busy networks
            #            self.sock.sendall(bytes_read)
            #            # update the progress bar
            #            progress.update(len(bytes_read))
            #    # close the socket
            #    self.sock.close()
            
            #except Exception as e:
            #    print(e)
            #return str(self.get_msg())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


class File_man():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    
    
    
    def read_file():

        file = open("login.txt", "r")
        data = file.readlines()
        file.close()
        return data
    
    def write_file(self, text):       
        file = open("login.txt", "w")
        file.write(text)
        file.close()
    
    def encrypt_file(self):
        pass
    

    def check_file():
        path_to_file = 'login.txt'
        path = Path(path_to_file)

        if path.is_file():
            print(f'file exists')
        else:
            print(f'file: {path_to_file} does not exist')
            os.system('touch key.key')
            return path

    
    
    
    def load_key(self):   
        """
        Loads the key from the current directory named `key.key`
        """
        return open("login.txt", "rb").read()


    def write_key():
        """
        Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)    




"""
    def main(self):
        opt = input("OPTIONS: \n--READ_FILE\n--WRITE_TO_FILE\n--WRITE_KEY\n--LOAD_KEY\n\n-->")
        if "READ".upper() in opt.upper():
            F_m.read_file()
        if "WRITE_TO_FILE".upper() in opt.upper():
            text = input("TEXT TO WRITE: \n---> ")
            self.write_file(text)
        if "WRITE_KEY".upper() in opt.upper():
            self.write_key()
        if "LOAD".upper() in opt.upper() or "LOAD_FILE".upper() in opt.upper():
            print("LOAD_KEY:", self.load_key())
        if "EXIT".upper() in opt.upper():
            exit()
        else:
            self.main()

    
    
if __name__=="__main__":
    F_m = File_man()
    F_m.main()
#    F_m.Make_file()
#    F_m.write_file()
#    F_m.read_file()

"""