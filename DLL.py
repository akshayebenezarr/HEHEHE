class node:
    def __init__(self, data):
        self.data= data
        self.nref= None
        self.pref= None


class dll:
    def __init__(self):
        self.head = None

    def delcur(self):
        n= self.head
        while n.data != "|":
            n = n.nref
        if n.pref is None:
            self.head = n.nref
            return n.nref

        elif n.nref is None:
            n.pref.nref = None
            return n.pref

        else:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        print(n.pref.data)
        return n.pref

    def addval(self, str=""):
        if self.head is None:
            nuno = node(str)
            self.head = nuno

        else:
            nuno = node(str)
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = nuno
            nuno.pref = n

    def printdll(self):
        n = self.head
        if n is not None:
            while n is not None:
                print(n.data, "->", end="")
                n = n.nref

        else:
            print("\n", "DLL is mt")


    def fro(self, data):

        self.delcur()


        l= len(data)
        for i in range(0,l):
            self.addval(data[i])
        self.addval("|")

    def move(self,steps=0, dir=""):
        prev= self.delcur()
        print(prev.data)
        if dir == "left":

            while steps != 1:
                prev = prev.pref
                steps = steps- 1

            nuno = node("|")
            # n = self.head
            prev.nref= nuno
            nuno.pref= prev
            nuno.nref= prev.nref
            prev.nref.pref= nuno

        elif dir == "right":
            prev = prev.nref
            while steps != 0:
                prev = prev.nref
                steps -= 1







    def bac(self, k):
        n = self.head

        while n.data != "|":
            n = n.nref
        tn = n
        n = n.pref
        while k != 0:
            n=n.pref
            k -= 1
        n.nref=tn
        tn.pref=n
ted = dll()
ted.addval("|")
ted.fro("baby")
ted.fro("I'm")
ted.fro("preyin")
ted.fro("on")
ted.fro("you")
ted.fro("tonight")
ted.fro("hehe")
# ted.printdll()

# ted.bac(4)
# ted.printdll()

ted.move(4,"left")
ted.printdll()

