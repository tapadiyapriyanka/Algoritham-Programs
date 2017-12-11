prime_no = ['125','521','215','195','591','915']
word1    = []
word2    = []
anagrams = {}
angram_list = []

for x in prime_no:  
    for i in range(len(x)):
        word1.append(x[i])
    for y in prime_no:
        for j in range(len(y)):
            word2.append(y[j])
        if set(word1) == set(word2):
            anagrams[x]=y
            angram_list.append(anagrams)
            word2 = []
        else:
            word2 = []
        anagrams = {}
    word1 = []

print("anagrams_list = ",angram_list)

prime = [121,535,852]
palendrome = []
for x in prime:
    x2=str(x)
    x1 = x2[::-1]
    if x2 == x1:
        palendrome.append(x)

print("pallendrome = ",palendrome)    


