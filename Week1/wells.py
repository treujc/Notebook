class Wells:
    def __init__(self,wellname,wellnumber):
        self.wellname = wellname
        self.wellnumber = wellnumber

    def getinfo(self):
        string = '{} is wellnumber {}.'.format(self.wellname,self.wellnumber)
        return string

Wells(['EvansWell','MicahsWell','KennysWell'],[1,2,3])

#print(wells.wellnumber[0])
print(EvansWell.getinfo())
