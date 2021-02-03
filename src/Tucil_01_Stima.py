#Hizkia Raditya Pratama Roosadi/ 13519087
#Tugas Kecil Strategi Algoritma
#Membuat program untuk menyelesaikan Cryptarithmetics
import time

def isExist(c,arr): #check if a char exists in an array
    found=False;
    for i in range (0,len(arr)):
        if (arr[i]==c):
            found=True;
    return found;
def isUnique(arr): #check if a string has all different letters
    if (len(arr))>len(set(arr)):
        return False
    else:
        return True
def digits(n): #returns number of digits in a number
    count=0
    while (n>0):
        count=count+1
        n=n//10
    return count
def factorial(n): #returns n!
    if n==1 :
        return 1
    else:
        return n*factorial(n-1)
    
def permutation(s): #find all unique number with the same number of digits as the array of unique letters
    number=0
    for i in range (int(factorial(9)/factorial(9-len(s)))):
        number=number+1
        if (digits(number)==len(s) and isUnique(str(number))):
            print(number)
def sum(arrInt):#return sum of integer array
    tot=0
    for i in range (len(arrInt)):
        tot=tot+arrInt[i]
    return tot

print("Welcome to cryptaritmethics!\n");

#declare arrays to store alphabets and words
alphabetStore=[]
wordStore=[]
opStore=[]
ansStore=[]
#find all unique alphabets from the file and put it in the array
with open('test.txt') as my_file:
    for line in my_file:
        wordStore.append(line.replace("\n",""))
        for ch in line:
            if (not(isExist(ch,alphabetStore)) and  ch!='+' and ch!='-' and ch!='\n'):
                alphabetStore.append(ch);
#separate the operand and answers
for i in range(0,len(wordStore)-2):
    opStore.append(wordStore[i].replace("+",""));
ansStore.append(wordStore[len(wordStore)-1]);

#protection againts >10 unique characters
if (len(alphabetStore)>10):
    print("Sorry, there are more than 10 unique characters")
    exit()
#print the problem
print("your problem are as follow\n")
for i in range (len(wordStore)):
    print (wordStore[i])
print("\n")
#count the time
start=time.time()
print("Figuring solution(s)..\n")
#permutation
number=10**(len(alphabetStore)-1) #we use the number from 0 to some number to get the result (brute force)
countSolution=0; #counter for solutions
countTest=0; #counter for tests
for i in range (number,10**len(alphabetStore)):
    number=number+1
    countTest+=1
    if (digits(number)==len(alphabetStore) and isUnique(str(number))):
        #we enter this if statement if the digit of the number=number of unique characters
        #and its a unique number (all numbers are different for each digit)
        #we are using dict, a built in python type for key:value
        my_dict={}
        for j in range (len(alphabetStore)):
            my_dict.update({alphabetStore[j]:str(number)[j]})
        #now we do the conversion
        fail=False    
        sum =0
        for k in range(len(opStore)): #find sum of the operand
            storeStr=""
            for l in range(len(opStore[k])):
                storeStr+=my_dict[opStore[k][l]]
                if (l==0 and my_dict[opStore[k][l]]=='0'):#guard for first digit!=0
                    fail=True
            sum +=int(storeStr)
        sumres=0
        for k in range(len(ansStore)): #find the number of the result
            storeresStr=""
            for l in range(len(ansStore[k])):
                storeresStr+=my_dict[ansStore[k][l]]
                if (l==0 and my_dict[ansStore[k][l]]=='0'):#guard for first digit!=0
                    fail=True
            sumres +=int(storeresStr)
        if (sum==sumres and not(fail)): #if the sums are equal then print
            for k in range(len(opStore)):
                storeNum=""
                for l in range(len(opStore[k])):
                    storeNum+=my_dict[opStore[k][l]]
                print(storeNum)
            print("----+")
            print(sumres)
            print("\n")
            print("number of tests: "+str(countTest)+"\n")
            countSolution+=1
end=time.time()
print("time needed: " + str(end-start))
print("number of solution(s): "+str(countSolution))

#arbitrary print
#for i in range (0,len(opStore)):
#    print(opStore[i]);
#for i in range (0,len(ansStore)):
#    print(ansStore[i]);
#print("\n");
#for i in range (0,len(wordStore)):
#    print(wordStore[i]);
#for i in range (0,len(alphabetStore)):
#    print(alphabetStore[i]);
#if isUnique(alphabetStore):
#    print("yes it's unique")
