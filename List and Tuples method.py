li=['gautam','Gandotra','sangeeta','aafsd','is','the','best']


# Python Lists Methods

li.append('person') #Adding element to list
print(li)




print(len(li))

second=list(('sahil','zara','eshbaan')) # using list constructor


print(second+li)
li.pop(3) # removing element from list
print(li+second)


# using tuples 
tup=('gautam','gandotra','is','very','good')

(a,*c,d)=tup


i=0
while i<len(tup):
    print(tup[i])
    i+=1

print(tup.count('gautam'))

print(tup.index('good'))