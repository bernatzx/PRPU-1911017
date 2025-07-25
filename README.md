Panduan Singkat

Catatan : bagian “1. Pertama” tidak perlu dilakukan jika sudah pernah dilakukan atau ada folder “venv”
belum ada didalam folder “sistem”, jika sudah pernah dilakukan dan ada folder “venv” maka lanjut saja
ke bagia “2. Kedua”.

1. Pertama
A. Didalam folder “sistem” tekan alt+d lalu ketik “cmd” dan tekan enter
B. Sebelum jalankan sistem perlu dibuat variable lingkungan dengan cara
Pada cmd ketikkan “python –m venv venv” lalu tekan enter dan tunggu sampai proses selesai
  1. Setelah itu ketik “cd venv” lalu enter untuk masuk ke folder venv
  2. Setelah itu ketik “cd Scripts” lalu enter untuk masuk ke folder Scripts
  3. Setelah itu ketik “activate” lalu enter untuk mengaktifkan variable lingkungkannya
  4. Setelah itu ketik “cd../..” lalu enter untuk kembali ke direktori awal
  5. Setelah itu ketik “pip install -r requirements.txt” lalu tekan enter untuk menginstall paket yang
     dibutuhkan dan tunggu sampai proses selesai
Sebelum menjalankan sistem disarankan buka kodingan dulu, caranya setelah installasi paket selesai
pada cmd ketik “code .” lalu enter maka otomatis kodingan akan terbuka di vs code.
Untuk menjalankan sistem ketik pada cmd yang sama “streamlit run app.py” lalu enter tunggu beberapa
saat dan sistem akan terbuka di browser

2. Kedua
Untuk membuka kodingan dan menjalankan sistem, tidak perlu melakukan langkah 1-5 diatas jika sudah
pernah dilakukan sebelumnya, berikut caranya
  1. Masuk pada folder sistem tekan “alt+d” lalu ketik “cmd” lalu tekan ENTER 2.
  Kemudian cmd akan terbuka, pada cmd ketik “code .” lalu tekan ENTER
  3. Tunggu beberapa saat maka VSCODE akan terbuka.
  4. Lalu untuk menjalankan sistem pada cmd ketik “streamlit run app.py” lalu tekan ENTER
  5. Tunggu beberapa saat maka sistem akan otomatis terbuka di browser 
