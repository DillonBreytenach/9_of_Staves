import threading
import time


class ListiCal():
    def __init__(self, **kwargs):
        super().__init__()
        self.group_list = []
        self.group = []
        self.client_list = []

    def run_to(self, obj_):
        ##GET UPDATES
        ##SEND UPDATES TO ALL MEMBERS OF GROUP
        print("OBJ_Q: ", obj_)


    def read_list(self, obj):
        self.RL = threading.Event()
        print("OBJ IN QUESTION:: ", obj)
        obj_q = []
        if obj:
            print("READING..")
   
            try:
                print("READING....")
                for i in self.group_list:
                    obj_q = i
                    print("READ_GROUP: ", i)
                    for j in i:
                        #print("CONNECTION: ", j)
                        if obj == j:
                            print("FOUND OBJ")
                            #obj_q = i
                            self.run_to(obj_q)
            except Exception as e:
                print(f'READ_LIST_ERR:: {str(e)}')
                pass


    def parent_list(self, client):
        self.E = threading.Event()

        varify = self.read_list(client)
        if varify == "EMPTY":
            print("FUCK")

        num = len(self.client_list)
        if num % 2:
            print("EVEN VAL")
            self.group_list.append(self.group)
            print("GROUP LIST", str(self.group_list))


        if len(self.client_list) >= 1:
            self.group.append(client)
            print(f'group::   {self.group}')


        if len(self.group) < 2:
            print('WAITING...')

            self.E.wait()

        elif len(self.group) == 2:
            self.group = []


    def check_list(self, data):
        for _ in self.client_list:
            if data in _:
                print(f'FOUND {str(_)}')
                return True
                



    def main(self):
        conn = "CONN"
        client = []
        while True:
            data = input("ADD_CLIENT \n  >> ")
            if "Q" in data.upper():
                break

            if data:
                client = [conn, data]


                #CHECK LIST IF CLIENT EXISTS
                if len(self.client_list) < 1:
                    print("STARTING")
                
                if self.check_list(data) == True:
                    self.read_list(client)
                    
                else:
                    self.client_list.append(client)
                    grouping = threading.Thread(target=self.parent_list, args=(client,))
                    grouping.daemon = True
                    grouping.start()







LC = ListiCal()
LC.main()
        