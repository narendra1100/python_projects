##sentence1=input("enter any sentence")
##sentence=sentence1.split()
##vowel=0
##consonents=0
##for word in sentence:
##    for latter in word:
##        if(latter=='a' or latter=='e' or latter=='i' or latter=='o' or latter=='u'):
##            vowel=vowel+1
##        else:
##            consonents=consonents+1
##
##print("number of vowel in the sentence is:",vowel)
##print("number of consonents in the sentence is:",consonents)
sentence=input("enter any sentence")
list=('a','e','i','o','u')
vowel=0
consonants=0
for ch in sentence:
    if(ch in list):
        vowel=vowel+1
    else:
        consonants=consonants+1
print("number of vowels in the sentence",vowel)
print("number of consonants in the sentence",consonants)
