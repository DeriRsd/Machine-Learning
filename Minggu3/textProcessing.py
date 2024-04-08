#Latihan 1
kata = '12345'
print("Menghitung Panjang Kalimat = 12345")
print(len(kata))

#Latihan 2
multiline = '''1
2
3
4
'''
print("\nFungsi Multiline")
print(len(multiline))

#Latihan 3
str1 = '1'
str2 = '2'
print("\nMenggabungkan String")
print(str1 + str2)

#Latihan Konversi Char ke ASCII
ch1 = 'a'
ch2 = ' ' #space
ch3 = 'A'
print("\nKonversi Char ke Kode ASCII")
print(ord(ch1))
print(ord(ch2))
print(ord(ch3))

#Latihan Konversi kode ASCII
print("\nKonversi Kode ASCII ke Char")
print(chr(65)+chr(75)+chr(85))

#Latihan Skip Huruf
print("\nLatihan Skip Huruf Tertentu di Python")
cthString="Aku Belajar Python Minggu 3"
vokal = ['a','i','u','e','o']

for i in range(len(cthString)):
    if cthString[i].lower() in vokal:
        continue
    print(cthString[i], end="")
    
    
#Latihan Menentukan Output Indeks Text dengan Jaraknya
print("\n\nLatihan Output String Indeks")
print(cthString[1::4])
print(cthString[1:5])
print(cthString[3:])
print(cthString[:3])
print(cthString[::2])

#Latihan Print String Sesuai Indeks
print("\nLatihan Output String Indeks Part 2")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0]+alphabet[10]+alphabet[20])

#Mencari Kata pada Kalimat berada pada indeks keberapa
txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

print("\nMenemukan Indeks dari Kata (the) Pada Kalimat")
fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

    
