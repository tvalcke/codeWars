def find_smallest_int(arr):
    return min(arr)

def greet(name):
    #Good Luck (like you need it)
    return "Hello, "+name+" how are you doing today?"

def find_needle(haystack):  #haystack is a list here
    position = 0
    for i in haystack:
        if i == 'needle':
            return('found the needle at position '+str(position))
        else :
            position +=1

def hero(bullets, dragons):
    return bullets/2>=dragons

def disemvowel(string_):
    stringReturned = ''
    for i in string_:
        if i.lower() == 'a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u':
            continue
        else:
            stringReturned+=i
    return stringReturned

#####################

#print(greet('Tris'))
#print(find_smallest_int([1,2,3,4,5]))
#print(find_needle(['needle','haystack','needle']))
#print(hero(10,5))
#print(disemvowel('Tu es très moche'))

