# ALMA-tools
Agriculture Land Mapping (ALMA Tool), Merupakan sebuah program aplikasi python berbasis desktop berfungsi untuk melakukan pemetaan dan analisis lahan pertanian secara digital.
Dengan memasukkan titik koordinat batas lahan, aplikasi ini dapat mensimulasikan luas lahan serta parameter lingkungan di area tersebut(seperti suhu, kelembaban, jenis tanah, dan itensitas cahaya). Hasil akhirnya akan diekspor menjadi sebuah peta interaktif dalam format .html dengan tampilan satelit dari ESRI WORLD IMAGERY.

# Base Language & Library
Project ini dibangun menggunakan bahasa pemrograman Python. beberapa library (pustaka) penting yang digunakan dalam kode ini meliputi :
- Tkinter : Digunakan untuk membuat tampilan antarmuka (GUI) desktop agar user bisa berinteraksi dengan aplikasi.
- Folium : Digunakan untuk membuat peta interaktif berbasis Leaflet.js. Di sini digunakan untuk memetakan poligon lahan dengan latar belakang citra satelit.
- Shapely.Geometery (polygon) : Digunakan untuk analisis geometri lahan, menghitungtitik tengah, dan menghitung estimasi luas berdasarkan koordinat.
- Datetime & Random : Digunakan untuk mencatat waktu pemrosesan data.

# Usefull
Meskipun logika analisisnya saat ini masih menggunakan simulasi matematis (belum terhubung ke sensor asli secara real-time), aplikasi ini memberikan usefull :
- Visualisasi Batas Lahan, Membantu user melihat bentuk dan batas lahan mereka secara jelas.
- Estimasi Luas Lahan, Memberikan hitungan perkiraan luas area (m2) dari titik koordinat yang diplot secara instan.
- Digitalisasi Data Pertanian, Memudahkan penyimpanan data pemetaan lahan ke dalam file HTML yang interaktif dan mudah.

# Information use
Sebelum menjalankan script ALMA tools.py, pastikan Anda sudah menginstal Python di komputer Anda beserta beberapa pustaka (library) pendukung yang dibutuhkan sebagai berikut:
pip install folium shapely (Pustaka tkinter dan datetime biasanya sudah bawaan dari Python).
Panduan Cara Penggunaan :

1. Memasukkan Titik Koordinat Lahan
- Siapkan Koordinat : Anda perlu menyiapkan data garis lintang (Latitude) dan garis bujur (Longitude) dari batas-batas lahan yang ingin diukur.  
- Input Data : Masukkan angka Latitude pada kolom teks "Latitude :" dan angka Longitude pada kolom teks "Longitude :".  
- Tambahkan Titik : Klik tombol "Tambah Titik Koordinat". Titik tersebut akan masuk ke dalam kotak daftar di bawahnya.  

Catatan Penting : Anda wajib memasukkan minimal 3 titik koordinat agar sistem bisa membentuk area poligon (bangun datar) dari lahan tersebut.  

2. Membuat Laporan dan Peta Visual
- Setelah minimal 3 titik koordinat dimasukkan, klik tombol biru bertuliskan "Generate".  
- Sistem akan menghitung secara otomatis estimasi luas lahan (dalam m²), suhu udara, kelembaban, struktur tanah, dan intensitas cahaya berdasarkan titik tengah dari area yang Anda buat.  
- Jendela penyimpanan (Save As) akan muncul. Pilih lokasi penyimpanan di komputer Anda, beri nama file, lalu simpan dalam format .html. Akan muncul notifikasi "Visualization has been saved!" jika berhasil.  

3. Melihat Hasil Pemetaan
- Buka file .html yang baru saja Anda simpan menggunakan peramban web (browser) seperti Chrome, Firefox, atau Edge.
- Anda akan melihat peta satelit (menggunakan citra Esri World Imagery) dengan area hijau transparan yang menunjukkan lahan Anda.  
- Klik ikon penanda (daun berwarna hijau) pada peta untuk memunculkan popup berisi tabel "Analisis Lahan" lengkap dengan data luas lahan, suhu, kelembaban, struktur tanah, dan intensitas cahaya. 

4. Mereset Data
Jika Anda ingin memetakan area baru, klik tombol merah bertuliskan "Reset" pada aplikasi. Tombol ini akan menghapus semua titik koordinat yang ada di daftar sehingga Anda bisa mulai dari awal.


created by @dynzprodc {2025}
