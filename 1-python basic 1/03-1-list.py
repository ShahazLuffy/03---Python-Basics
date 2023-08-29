#list
firstList = [1,'2', True, 23,'stuff', 'False','Python', 13,'Swift', 'C++', 623, 'C', 'Java', 'akbar', 'Rust', 'R']
firstList[0]= 111
print(firstList)
newFirstList = firstList[0:2]
print(newFirstList)

#list methods
list =[81,  55, 'hello',
        'world', 
            'python', True, 
           False, 
            True,]
list.append('last item')
newList = list.append('new last item')
print('list: ',list)
#append add new element to the end of the list
print('newList :', newList) # append does not produce a value
newWorkingList = list
newWorkingList.append('now works')
print('newWorkingList :', newWorkingList)



#insert adds an element to a specific index of the list
newWorkingList.insert(1,'aaaaaaaaaaaaaaaaaaa')
print('inserted newworkinglist' , newWorkingList)
testingInsertMethod = newWorkingList.insert(0,'pfff')
print(testingInsertMethod)  #insert does not produce a value 
newWorkingList.extend([81, 'akbar joje'])
print(newWorkingList)

#remove first occurance of a value in the list
newWorkingList.remove(81)
print(newWorkingList)

#pop deletes the last item in the list, if you specify an index then it will delete the indexd item
newWorkingList.pop()
print(newWorkingList)
newWorkingList.pop(1)
print(newWorkingList)

#newworkinglist.clear()
#print(newWorkingList.index(True)) #return first appearence of True value
#print(newWorkingList.index(True, 0,2)) #error item is not in the list

#in
print('world' in newWorkingList)
print(newWorkingList.count(True)) #how many item in the list



#sort
numberList = [2,2,345,345,234,234,45,76,74356,2457,26,245673567,56]
print(newWorkingList.sort(numberList))