class bikeshop:
    def __int__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("total bike",self.stock)
    def rentbike(self,q):

        if q<=0:
            print("Enter the valiad value")
        elif q > self.stock:
            print("Enter the value")
        else:
            self.stock=self.stock-q
            print("total prize",q*100)
            print("total bikes",self.stock)
while True:
    obj=bikeshop()
    uc=int(input('''
    1 Display the stock
    2 Rent bikes
    3 exit
    '''))
    if uc==1:
        obj.displaybike()
    elif uc==2:
        n=int(input("Enter the qut of bikes:--"))
        obj.rentbike(n)
    else :
        break