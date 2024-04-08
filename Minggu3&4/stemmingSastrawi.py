import pandas as pd

#Menampilkan isi Data pada file CSV
print("Menampilkan isi Data pada file CSV")
dataset = pd.read_csv('clean_dataset.csv', sep=';')
print(dataset.head())

#Load Sastrawi sebagai Stemmer melalui Library Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()
#Testing kata untuk di Stemming
kata = 'kebersihan'
kata_dasar = stemmer.stem(kata)
print("\nKata dasar dari kebersihan = "+kata_dasar)

