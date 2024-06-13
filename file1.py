
class mul():
    def getval(self):
        try:
            self.a=int(input("enter value:"))
        except ValueError:
            print("dont enter alnums or strs")
    def getmul(self):
        for i in range(1,11):
            print("\t{}*{}={}".format(self.a,i,self.a*i))

#main
m=mul()
m.getval()
m.getmul()