# main.py
import time
import os

# init empty row and res
rows = []
res = ''

# init array char DARI fungsi yang memasukan karakter unik ke array (STATIK dan TIDAK BERUBAH)
arrChar = []

# function untuk melakukan pengecekan unik
def uniqueChar(letter):
  for i in range(len(arrChar)):
    if (arrChar[i]==letter):
      return False
  return True

# counting file line length
lineCount = len(open(os.path.join('../test', 'test.txt')).readlines())

# opening, printing and reading file
f = open(os.path.join('../test', 'test.txt'))
print("PERSOALAN cryptarithmetics adalah sebagai berikut:")

for l in f:
  rows.append(l.strip("\n+- "))
  print(l.strip('\n'))
  for j in range(len(l)):
    if (uniqueChar(l[j]) and ord(l[j])>=65 and ord(l[j])<=90):
      arrChar.append(l[j])
res = rows.pop(-1)
rows.pop(-1)

# timer start
start_time = time.time()
# init variabel num untuk angka dari jumlah digit yang sama dengan huruf unik, untuk keperluan inkremen angka
num = (10**len(arrChar))-1    
# init counter solutions found
found = 0

# masuk loop untuk iterasi permutasi inkremental angka-angka yang mungkin
while (num>=10**(len(arrChar)-1)):
  if ( (len(str(num)) == len(set(str(num)))) and (len(set(str(num))) == len(arrChar)) ):
    keyValue = {} # init empty dictionary
    
    # define key-value pairs
    for i in range(len(arrChar)):
      keyValue.update({arrChar[i] : str(num)[i]})
    
    # substitute rows with key-value
    fail = False
    sum = 0; j = 0
    while(j<len(rows) and not(fail)):
      storeStr = ""
      for k in range(len(rows[j])):
        storeStr += keyValue[rows[j][k]]
        if (k==0 and keyValue[rows[j][k]]=='0'):
          fail = True
      sum += int(storeStr)
      j += 1

    # substitute res with key-value
    if (not(fail)):
        storeStr = ""
        for i in range(len(res)):
          storeStr += keyValue[res[i]]
          if (i==0 and keyValue[res[i]]=='0'):
            fail = True
        sumRes = int(storeStr)

    # check if math is true
    if (sum==sumRes and not(fail)):
      print("\nSalah satu SOLUSI yang cocok (%s PERCOBAAN) adalah:" % ((10**len(arrChar))-num))
      print("--- Waktu menemukan solusi: %s detik ---" % (time.time() - start_time))
      start_time = time.time()
      
      file = open(os.path.join('../test', 'test.txt'))
      for line in file:
        for character in line:
          if (ord(character)>=65 and ord(character)<=90):
            print(keyValue[character],end="")
          else:
            print(character,end="")
      found += 1
      print()
  num -= 1

# print jumlah solusi
print("\nJumlah semua JAWABAN yang mungkin ada :  "+str(found)+" solusi")