class c1(object):
    def __init__(self,v):
        self.practice=v
    def show(self):
        print(self.practice)
    def getValue(self):
        return self.practice
    def setValue(self,v):
        self.practice=v


inst=c1(100)
print(inst.practice)
inst=c1(200)
print(inst.practice)
inst.practice=300
inst.show()

inst.setValue(300)
print(inst.getValue())
