class Stack:
  def __init__(self):
    self.items = []
    
  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.insert(0, item)
    
  def pop(self):
    return self.items.pop(0)

  def peek(self):
    return self.items[0]

  def size(self):
    return len(self.items)

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.is_empty():
        newString = newString + digits[remstack.pop()]

    return newString

print("binary: ",baseConverter(26,2))
print("octal : ",baseConverter(26,8))
print("hex   : ",baseConverter(26,16))