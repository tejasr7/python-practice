tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


longest = 0   ####### to find the longest line  #####
lines = []  #######to keep lines ####

for elements in zip(tableData[0], tableData[1], tableData[2]):

    ## join elements in line - like 'apples' + ' ' + 'Alice' + ' ' + 'dogs'
    line = ' '.join(elements) 

    # add line to the list
    lines.append(line) 

    #print(line) # you can print it to see what you get

    # find the longest line
    length = len(line)
    if length > longest:
        longest = length

 ########print('the longest:', longest)##########

longest += 1 # to get one space more at left side

# ##########print lines using `%*s`########
# if `longest` is 21 then it will works as `%21s`
for line in lines:
    print('%*s' % (longest, line))


# empty dictonary for sorting the data
newTable = {0:[], 1:[], 2:[], 3:[]}

# iterate through each list in tableData
for li in tableData:
    for i in range(len(li)):
        # put each item of tableData into newTable by index
        newTable[i].append(li[i])
        
# determine the longest list by number of total characters
# for instance ['apples', 'Alice', 'dogs'] would be 15 characters
# we will start with longest being zero at the start
longest = 0
# iterate through newTable
# for example the first key:value will be 0:['apples', 'Alice', 'dogs']
# we only really care about the value (the list) in this case
for key, value in newTable.items():
    # determine the total characters in each list
    # so effectively len('applesAlicedogs') for the first list
    length = len(''.join(value))
    # if the length is the longest length so far,
    # make that equal longest
    if length > longest:
        longest = length

# we will loop through the newTable one last time
# printing spaces infront of each list equal to the difference
# between the length of the longest list and length of the current list
# this way it's all nice and tidy to the right
for key, value in newTable.items():
    print(' ' * (longest - len(''.join(value))) + ' '.join(value))
