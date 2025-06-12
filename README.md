# Aplikasi Web TrashScan

**TrashScan** adalah aplikasi berbasis web untuk mendeteksi jenis sampah menggunakan teknologi machine learning. Aplikasi ini bertujuan untuk membantu pengguna memilah sampah dengan lebih mudah dan mendukung praktik daur ulang yang berkelanjutan.

## Teknologi yang Digunakan

- Python 3.x
- Flask (Backend)
- HTML, CSS, JavaScript (Frontend)
- TensorFlow/Keras (Model Machine Learning)
- OpenCV (Pengolahan Gambar)
- Bootstrap (UI Framework)

## Fitur Utama

- Upload gambar sampah dan deteksi jenisnya
- Tampilan antarmuka yang responsif
- Informasi edukatif tentang jenis sampah
- Lokasi daur ulang

## Persyaratan Sistem

- Python 3.8 atau lebih baru
- Git
- pip (Python package manager)
- Virtual environment (opsional tapi disarankan)

  ```python -m venv venv
  source venv/bin/activate     # Linux/Mac
  venv\Scripts\activate        # Windows
  ```

- Depedensi yang dibutuhkan

  [Lihat daftar dependensi di requirements.txt](requirements.txt)

## Instalasi

```bash
git clone https://github.com/sabinawrim/App-TrashScan.git
cd App-TrashScan
pip install -r requirements.txt
```

## Cara Menjalankan Aplikasi di Lokal

1. Ketikkan ini di Terminal `python app.py`
2. Jalankan file `webTrashScan.html`

## Cara Penggunaan

1. Buka halaman utama TrashScan di browser.
2. Klik tombol **"Unggah Gambar"**.
3. Pilih gambar dari perangkat.
4. Aplikasi akan menampilkan jenis sampah yang terdeteksi secara otomatis serta memberikan penjelasan dan rekomendasi pengolahan sampah sesuai jenisnya.

## Struktur Folder Proyek

```
trashscan/
├── static/uploads          # Berisi gambar yang telah diunggah
├── templates/              # Berisi file html dan css
style.css
webTrashScan.html
├── model/model.h5          # Model ML (.h5)
├── app.py                  # Main Flask app
├── requirements.txt        # Daftar dependensi
└── README.md               # Dokumentasi ini

```

## Tentang Model ML

- Dataset terdiri dari gambar berbagai jenis sampah
- Arsitektur: CNN sederhana dengan akurasi >90%

  ```
  model = Sequential([
  base_model,
  Conv2D(64, (3, 3), activation='relu', padding='same'),
  MaxPooling2D(pool_size=(2, 2)),
  # Dropout(0.5), #ditambahkan

  Conv2D(64, (3, 3), activation='relu', padding='same'),
  MaxPooling2D(pool_size=(2, 2)),
  # Dropout(0.5),

  GlobalAveragePooling2D(),
  Dropout(0.5),
  Dense(128, activation='relu', kernel_regularizer=regularizers.l2(l2=l2_val)),
  Dense(64, activation='relu', kernel_regularizer=regularizers.l2(l2=l2_val)),
  Dropout(0.5),
  Dense(2, activation='softmax')])
  ```

- Model disimpan dalam folder `model/model.h5` dan diload saat server berjalan

## Contoh Tampilan

- **Tampilan beranda aplikasi**

![tampilan beranda](/static/hero.png)

- **Daftar layanan aplikasi**

![tamplan layanan](/static/layanan.png)

- **Formulir unggah gambar**

![tampilan ungaah gambar](/static/unggah-gambar.png)

- **Artikel Dokumentasi**

![tampilan artikel](/static/artikel.png)

- **Hasil klasifikasi jenis sampah**

![tampilan hasil klasifikasi](/static/hasil.png)

- **Lokasi Daur Ulang**

![tampilan lokasi daur ulang](/static/lokasi.png)

## Catatan

- Pastikan model deteksi sampah (model.h5 atau model.pkl) sudah ada di folder model/.
- Jika menggunakan model besar, pastikan komputer memiliki cukup RAM dan prosesor yang mendukung.

```

```
