class playcontinue:
    def __init__(self,occupied_list):
        self.occupied_list=occupied_list
        self.playcontinue=False
        for i in range(5):
            for j in range(5):
                if self.occupied_list=='*':
                    self.playcontinue=True
                    break
    def __str__(self):
        return self.playcontinue
    def __repr__(self):
        return self.__str__()

                    