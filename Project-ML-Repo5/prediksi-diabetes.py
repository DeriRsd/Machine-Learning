import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Fungsi untuk memuat dan memproses data
def muat_dan_proses_data(url):
    nama_kolom = ['Kehamilan', 'Glukosa', 'TekananDarah', 'KetebalanKulit', 'Insulin', 'BMI', 'FungsiKeturunanDiabetes', 'Usia', 'Hasil']
    df = pd.read_csv(url, header=None, names=nama_kolom)
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    return X, y

# Fungsi untuk membagi dan menormalisasi data
def bagi_dan_normalisasi_data(X, y, ukuran_test=0.2, random_state=42):
    X_latih, X_uji, y_latih, y_uji = train_test_split(X, y, test_size=ukuran_test, random_state=random_state)
    scaler = StandardScaler()
    X_latih = scaler.fit_transform(X_latih)
    X_uji = scaler.transform(X_uji)
    return X_latih, X_uji, y_latih, y_uji, scaler

# Fungsi untuk melatih dan mengevaluasi model KNN
def latih_dan_evaluasi_knn(X_latih, X_uji, y_latih, y_uji, k):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_latih, y_latih)
    y_pred = knn.predict(X_uji)
    akurasi = accuracy_score(y_uji, y_pred)
    matriks_kebingungan = confusion_matrix(y_uji, y_pred)
    laporan_klasifikasi = classification_report(y_uji, y_pred)
    return knn, akurasi, matriks_kebingungan, laporan_klasifikasi

# Fungsi untuk mengambil input dari pengguna untuk prediksi
def ambil_input_pengguna():
    kehamilan = int(input("Masukkan jumlah kehamilan                                       : "))
    glukosa = float(input("Masukkan konsentrasi glukosa plasma                             : "))
    tekanan_darah = float(input("Masukkan tekanan darah diastolik (mm Hg)                        : "))
    ketebalan_kulit = float(input("Masukkan ketebalan lipatan kulit triceps (mm)                   : "))
    insulin = float(input("Masukkan kadar insulin serum 2 jam (mu U/ml)                    : "))
    bmi = float(input("Masukkan indeks massa tubuh (berat dalam kg/(tinggi dalam m)^2) : "))
    fungsi_keturunan = float(input("Masukkan fungsi garis keturunan diabetes                        : "))
    usia = int(input("Masukkan usia                                                   : "))
    
    return np.array([kehamilan, glukosa, tekanan_darah, ketebalan_kulit, insulin, bmi, fungsi_keturunan, usia]).reshape(1, -1)

# Fungsi utama
def main():
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    X, y = muat_dan_proses_data(url)
    X_latih, X_uji, y_latih, y_uji, scaler = bagi_dan_normalisasi_data(X, y)
    
    # Input untuk nilai k
    k = int(input("Masukkan nilai k untuk KNN : "))
    
    knn, akurasi, matriks_kebingungan, laporan_klasifikasi = latih_dan_evaluasi_knn(X_latih, X_uji, y_latih, y_uji, k)
    
    # Menampilkan hasil
    print(f"Akurasi: {akurasi}")
    print("Matriks Kebingungan:")
    print(matriks_kebingungan)
    print("Laporan Klasifikasi:")
    print(laporan_klasifikasi)
    
    # Input data untuk prediksi
    input_pengguna = ambil_input_pengguna()
    input_pengguna_tereskalasi = scaler.transform(input_pengguna)
    prediksi = knn.predict(input_pengguna_tereskalasi)
    
    print(f"Model memprediksi bahwa pasien {'menderita' if prediksi[0] == 1 else 'tidak menderita'} diabetes.")

if __name__ == "__main__":
    main()
