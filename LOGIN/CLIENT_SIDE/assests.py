
class assests():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def image_pro(self, List, Num):
    
        #Assests Listed In Catagories
        #RUNES:
        self.All_Giz = 'assests/Rune_All_giz.png'
        self.Har_Gool = 'assests/Rune_Har_gool.png'
        self.Yah_Rah = 'assests/Rune_Yah_rah.png'
        self.Runes = [self.All_Giz, self.Har_Gool, self.Yah_Rah]

        #Fruitless_Trees
        self.FTree_1 = 'assests/FTree_1.png'
        self.FTree_2 = 'assests/FTree_2.png'
        self.FTree_3 = 'assests/FTree_3.png'
        self.FTree_Complete = 'assests/FTree_Complete.png'
        self.FTree_Joker = 'assests/FTree_Joker.png'
        self.FTrees = [self.FTree_1, self.FTree_2, self.FTree_3]