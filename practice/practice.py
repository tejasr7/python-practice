# Problem Solving with Algorithms and Data Structures
# Chapter 1

def gcd(m, n):
       while m % n != 0:
          old_m = m
          old_n = n
          m = old_n
          n = old_m % old_n
       return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self, other_fraction):
        new_num = self.num*other_fraction.den + self.den*other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other_fraction):
        new_num = self.num*other_fraction.den - self.den*other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    # Multiplication
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    # Division
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    # Deep Equality
    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num == second_num
    
    # Less than
    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num < second_num
    
    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num > second_num

##x = Fraction(1, 2)
##y = Fraction(1, 4)
##z = x + y
##print(x + y)
##print(x == y)
##print(x - y)
##print(x*y)
##print(x/y)
##print(x != y)


class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
    
class NandGate(AndGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class NorGate(OrGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print(g4.getOutput())
    # NandGate
    n1 = AndGate('N1')
    n2 = NandGate('N2')
    print(n2.getOutput())
main()
