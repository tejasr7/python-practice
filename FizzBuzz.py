for fizzbuzz in range(50):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)


### List
##
##lst = []
##for i in range(1, 51):
##    if i % 3 == 0 and i % 5 == 0:
##        lst.append('FizzBuzz')
##    elif i % 3 == 0:
##        lst.append('Fizz')
##    elif i % 5 == 0:
##        lst.append('Buzz')
##    else:
##        lst.append(i)
##print(lst)


##for i in range(1,51):
##    output = ""
##    if i % 3 == 0: output += "Fizz"
##    if i % 5 == 0: output += "Buzz"
##    if output == "": output += str(i)
##    print(output)
