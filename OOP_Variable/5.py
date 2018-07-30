class Cal(object):
    def __init__(self,v1,v2):
        if isinstance(v1,int):
            self.v1=v1
        if isinstance(v2,int):
            self.v2=v2

    def add(self):
        return self.v1+self.v2
    def sub(self):
        return self.v1-self.v2
    def div(self):
        return self.v1/self.v2
    def mul(self):
        return self.v1*self.v2
    def setV(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def getV(self):
        return self.v1,self.v2

Prac=Cal(100,200)
print(Prac.add(),Prac.sub(),Prac.div(),Prac.mul())

Prac.setV(200,300)
print(Prac.add(),Prac.sub(),Prac.div(),Prac.mul())
