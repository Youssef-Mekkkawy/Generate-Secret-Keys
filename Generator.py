import string
import random
""" 

    # Simple Script For Generate Secret Keys & Password #

"""
class Generator:

    def __init__(self) -> None:
        self.String = [string.ascii_letters, string.digits]
        self.Data = ''.join(self.String)
        
    def Shuffling(self, Data:str = None, No_of_Shuffling:int = 30):

        if Data == None:
            Data = self.Data

        new = list(Data)
        for i in range(No_of_Shuffling):
            random.shuffle(new)
        return new
    
    def Secret_Key(self, Length:int = 28, Number_of_Each_Separated:list = [8,4,4,12], Separated:str = None, Out_Put_ID_Only:bool = False):
        # Strings Letters Number 
        Sum_Number_in_List = sum(Number_of_Each_Separated)
        Number_of_item_in_list = len(Number_of_Each_Separated)
        Count_Of_Separated = len(Separated)
        Collect_ID = []
        # Check sum is equal 
        if Sum_Number_in_List != Length:
            return f"Please Some of {Length} Must Be Same {Number_of_Each_Separated} -> len is {Sum_Number_in_List}"

        DATA = Generator.Shuffling(self, self.Data)
        random.shuffle(DATA)

        for i in range(0,Number_of_item_in_list):
            # Choose Randome Char From Data.
            Random_Chara = random.sample(DATA, Number_of_Each_Separated[i])
            random.shuffle(Random_Chara)
            Separated_ID = ''.join(Random_Chara)
            Collect_ID.append(Separated_ID)

        # Add Separated Symple.
        if Separated != None:
            ID = Separated.join(Collect_ID)
            Size = len(ID)
            Size_Without_Spreated = Size - ((Number_of_item_in_list - 1) * Count_Of_Separated)
        else:
            ID = ''.join(Collect_ID)
            Size = len(ID)
            Size_Without_Spreated = Size
            

        if Out_Put_ID_Only == True:
            return ID
        else:
            return ID, f"Size: {Size}", f"Size Without Sptreated: {Size_Without_Spreated}"

    def Password(self, Length:int = 28, Special_Chara:str = None):
        if Special_Chara == None:
            Data = [self.Data, '!@#$%&*']
        else:
            Data = [self.Data, '!@#$%&*', Special_Chara]

        Generator.Shuffling(self, Data, 15)
        Data = ''.join(Data)
        Random_Chara = random.sample(Data, Length)
        password = ''.join(Random_Chara)
        return password
