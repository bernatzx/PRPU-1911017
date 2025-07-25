# pustaka untuk membuat tampilan siste
import streamlit as st

# pustaka untuk manipulasi data
import pandas as pd

# pustaka untuk dapat memuat metode yang sudah dilatih dalam hal ini metode KNN dan RF
import joblib

# pustaka untuk dapat melihat akurasi kedua metode
from sklearn.metrics import accuracy_score

# muat metode KNN
knn_model = joblib.load("knn_model.pkl")

# muat metode RF
rf_model = joblib.load("rf_model.pkl")

# muat file scalper untuk normalisasi data numerik
scaler = joblib.load("data/scaler.pkl")

# muat file encoder untuk encoding kolom KELAYAKAN, contoh Layak = 0, Tidak Layak 1
target_encoder = joblib.load("data/target_encoder.pkl")

# muat data latih
train_df = pd.read_csv("data/data_train.csv").drop(columns=['target'])

#muat data uji
test_df = pd.read_csv("data/data_test.csv")

# bagi data uji menjadi dua
# data uji yang tidak memiliki kolom "KELAYAKAN"
X_test = test_df.drop(columns=['target'])
# data uji lengkap
y_test = test_df['target']

# === Konfigurasi TAMPILAN atau UI ===
# pemberian judul halaman dan menempatkan layout di tengah
st.set_page_config(page_title="Prediksi Kelayakan Kredit", layout="centered")

# pemberian dan menampilkan judul pada layout
st.title("📊 Prediksi Kelayakan Kredit")

# sub judul
st.markdown("Aplikasi ini akan memprediksi kelayakan kredit menggunakan dua metode: KNN dan Random Forest.")

# menampilkan kalimat "Masukkan Data Calon Debitur" pada layout
st.subheader("📝 Masukkan Data Calon Debitur")

# Input sesuai fitur
pekerjaan = st.selectbox("Pekerjaan", ["Karyawan Swasta", "Nelayan", "PNS", "Pedagang", "Petani", "Wiraswasta", "Guru", "Mahasiswa", "Perawat", "TNI/Polri", "Dokter"])
penghasilan = st.number_input("Penghasilan (Rp)", min_value=0)
tanggungan = st.number_input("Jumlah Tanggungan", min_value=0)
usia = st.number_input("Usia", min_value=18, max_value=75)
besar_pinjaman = st.number_input("Besar Pinjaman (Rp)", min_value=0)
tenor = st.number_input("Tenor (bulan)", min_value=1)
dp = st.number_input("DP Presentase (%)", min_value=0)
jaminan = st.selectbox("Jaminan", ["BPKB Motor", "BPKB Mobil", "Sertifikat Rumah", "Emas", "Sertifikat Tanah"])
jenis_kredit = st.selectbox("Jenis Kredit", ["Kredit Rumah", "Kredit Motor", "Kredit Usaha", "Multiguna"])
status_rumah = st.selectbox("Status Kepemilikan Rumah", ["Milik Sendiri", "Kontrak", "Tinggal dengan Orang Tua", "Kost", "Keluarga"])
riwayat_kredit = st.selectbox("Riwayat Kredit", ["Baik", "Cukup", "Buruk", "Tidak Ada"])


# tombol "Prediksi", jika ditekan pada tampilan sistem maka kode didalam tombol ini akan dieksekusi
if st.button("Prediksi"):
    # Isi tombol
    # Buat dataframe input untuk nanti dapat dipakai yaitu menampilkannya sebagai rekapan data
    input_df = pd.DataFrame([{
        "PENGHASILAN": penghasilan,
        "TANGGUNGAN": tanggungan,
        "USIA": usia,
        "BESAR PINJAMAN": besar_pinjaman,
        "TENOR": tenor,
        "DP PRESENTASE": dp,
        "PEKERJAAN": pekerjaan,
        "JAMINAN": jaminan,
        "JENIS KREDIT": jenis_kredit,
        "STATUS KEPEMILIKAN RUMAH": status_rumah,
        "RIWAYAT KREDIT": riwayat_kredit
    }])

    # menampilkan "Rekap Data Input" pada layout
    st.subheader("📄 Rekap Data Input")
    # menampilkan dataframe Rekapan Data yang sudah dibuat diatas
    st.write(input_df)


    # Dilakukan penyesuaian terhadap kolom inputan diatas dengan data training dari hasil preprocessing pada file lain
    # ini dilakukan supaya tidak terjadi error
    input_encoded = pd.get_dummies(input_df)
    for col in train_df.columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[train_df.columns]

    # Normalisasi numerik
    numeric_cols = ['PENGHASILAN', 'TANGGUNGAN', 'USIA', 'BESAR PINJAMAN', 'TENOR', 'DP PRESENTASE']
    input_encoded[numeric_cols] = scaler.transform(input_encoded[numeric_cols])

    # === Prediksi ===
    pred_knn = knn_model.predict(input_encoded)[0]
    pred_rf = rf_model.predict(input_encoded)[0]
    label_knn = target_encoder.inverse_transform([pred_knn])[0]
    label_rf = target_encoder.inverse_transform([pred_rf])[0]
    prob_rf = rf_model.predict_proba(input_encoded)[0]

    # menampilkan "Hasil Prediksi" pada laytout
    st.subheader("📊 Hasil Prediksi")

    # buat dua kolom
    col1, col2 = st.columns(2)

    # untuk menampilkan hasil prediksi dari kedua metode terhadap data inputan
    with col1:
        st.markdown("**K-Nearest Neighbor**")
        st.write(f"Prediksi: **{label_knn}**")
    with col2:
        st.markdown("**Random Forest**")
        st.write(f"Prediksi: **{label_rf}**")

    # untuk mendapatkan akurasi metode KNN
    y_pred_knn_test = knn_model.predict(X_test)
    acc_knn = accuracy_score(y_test, y_pred_knn_test)

    # untuk mendapatkan akurasi metode RF
    y_pred_rf_test = rf_model.predict(X_test)
    acc_rf = accuracy_score(y_test, y_pred_rf_test)

    # menampilkan "Akurasi Model (Data Uji)" pada layout
    st.subheader("📈 Akurasi Model (Data Uji)")

    # menampilkan hasil akurasi metode KNN
    st.write(f"🔹 Akurasi KNN: **{acc_knn*100:.2f}%**")

    # menampilkan hasil akurasi metode RF
    st.write(f"🔹 Akurasi Random Forest: **{acc_rf*100:.2f}%**")