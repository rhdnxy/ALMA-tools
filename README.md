# ALMA-tools
Agriculture Land Mapping (ALMA Tool), Merupakan sebuah program aplikasi python berbasis desktop yang dikembangkan oleh @dynzprodc, yang berfungsi untuk melakukan pemetaan dan analisis lahan pertanian secara digital.
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
