import os
from cryptography.fernet import Fernet
from pathlib import Path



class File_man():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    
    
    def read_file(file_name):
        #f_check = File_man.check_file(file_name)
        if file_name:
            
            print(f'[filename]: {file_name}')
            with open(file_name, "r") as rf:
                data = rf.readlines()
                rf.close()
                return data
    
                

    
    def write_file(file_name, data, rwm):
        
        text = ""
        for _ in data:
            text += str(_+'\n')
        print(f'TEXT_TO_WRITE: \n {text}')      
        with open(file_name, rwm) as wf:
            wf.write(text)
            wf.close()
    
    def encrypt_file(self):
        pass
    

    def check_file(file_name, user_data):
        path_to_file = file_name
        path = Path(path_to_file)

        if path.is_file():
            
            #user_auth
            #DO A STRING COMPARE TO SEE IF THE PASSWORD MATCHES
            # #####!*!*!*!*!*!
            
            file_data = File_man.read_file(file_name)
            print(f'[file exists] : {file_name}')
            print(f'[FILE_DATA]   : {file_data}')
            return True
        else:
            print(f'[file]: {path_to_file} !does_not_exist!\n \nWELCOME_NEW_PLAYER\n')
            os.system('touch key.key')
            return False

    
    
    
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