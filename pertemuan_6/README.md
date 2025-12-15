# Aplikasi Manajemen Matakuliah (Pyramid)

## Deskripsi Proyek

Proyek ini merupakan **API sederhana** untuk manajemen data matakuliah yang dibuat menggunakan **Pyramid (web framework)**, **SQLAlchemy (ORM)**, dan **SQLite**.

Aplikasi ini dikembangkan sebagai bagian dari tugas praktikum backend dengan tujuan memahami konsep **REST API**, **CRUD**, **ORM**, dan **manajemen database**.

### Fitur Utama

* CRUD (Create, Read, Update, Delete) untuk entitas `Matakuliah`
* Data matakuliah terdiri dari:

  * `id`
  * `kode_mk`
  * `nama_mk`
  * `sks`
  * `semester`

---

## Cara Instalasi

### 1. Membuat dan Mengaktifkan Virtual Environment (Direkomendasikan)

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 2. Menginstal Dependensi

```powershell
pip install -r requirements.txt

# Jika terdapat paket yang belum tercantum
pip install pyramid_tm zope.sqlalchemy
```

### 3. Verifikasi Interpreter (Opsional)

```powershell
python --version
where python
```

---

## Konfigurasi Database

* Database default menggunakan **SQLite** dengan file `matakuliah.db`
* Lokasi database berada di folder `pertemuan_6`
* Skema tabel dibuat otomatis melalui fungsi `init_db()`
* Data awal dapat ditambahkan menggunakan script `seed_db.py`

---

## Migrasi Database (Alembic)

Project ini telah disiapkan untuk mendukung migrasi database menggunakan **Alembic**.

Direktori `alembic/` dan file `alembic.ini` sudah tersedia.

Contoh perintah migrasi:

```powershell
# Membuat revision otomatis setelah perubahan model
alembic revision --autogenerate -m "create matakuliah"

# Menerapkan migrasi ke database
alembic upgrade head
```

Pastikan konfigurasi database pada `alembic.ini` sesuai dengan database yang digunakan aplikasi.

---

## Cara Menjalankan Aplikasi

### 1. Menambahkan Data Awal (Seed Database)

Jalankan perintah berikut **hanya jika tabel masih kosong**:

```powershell
python seed_db.py
```

### 2. Menjalankan Server

```powershell
python app.py
```

Aplikasi akan berjalan pada alamat:

```
http://localhost:6543
```

---

## API Endpoints

Semua endpoint mengembalikan response dalam format **JSON**.

### 1. Get All Matakuliah

* **Method:** `GET`
* **URL:** `/api/matakuliah`

Contoh request:

```bash
curl -X GET http://localhost:6543/api/matakuliah
```

Contoh response (200):

```json
{
  "status": "success",
  "matakuliahs": [
    {
      "id": 1,
      "kode_mk": "IF101",
      "nama_mk": "Algoritma dan Pemrograman",
      "sks": 3,
      "semester": 1
    }
  ]
}
```

---

### 2. Get Single Matakuliah

* **Method:** `GET`
* **URL:** `/api/matakuliah/{id}`

```bash
curl -X GET http://localhost:6543/api/matakuliah/1
```

---

### 3. Create Matakuliah

* **Method:** `POST`
* **URL:** `/api/matakuliah`
* **Body:** `kode_mk`, `nama_mk`, `sks`, `semester` (wajib)

```bash
curl -X POST http://localhost:6543/api/matakuliah \
-H "Content-Type: application/json" \
-d '{"kode_mk":"IF301","nama_mk":"Pemrograman Web","sks":3,"semester":5}'
```

---

### 4. Update Matakuliah

* **Method:** `PUT`
* **URL:** `/api/matakuliah/{id}`

```bash
curl -X PUT http://localhost:6543/api/matakuliah/1 \
-H "Content-Type: application/json" \
-d '{"nama_mk":"Algoritma Lanjut"}'
```

---

### 5. Delete Matakuliah

* **Method:** `DELETE`
* **URL:** `/api/matakuliah/{id}`

```bash
curl -X DELETE http://localhost:6543/api/matakuliah/1
```

---

## Testing API

### Menggunakan `curl.exe` (Windows / Git Bash)

```powershell
curl.exe -X GET http://localhost:6543/api/matakuliah
```

### Menggunakan PowerShell (`Invoke-WebRequest`)

```powershell
Invoke-WebRequest -Uri http://localhost:6543/api/matakuliah -Method GET
```

---

## File Penting

* **Entry Point & Views:** `pertemuan_6/app.py`
* **Model Database:** `pertemuan_6/models.py`
* **Konfigurasi Database:** `pertemuan_6/database.py`
* **Seed Database:** `pertemuan_6/seed_db.py`
* **Konfigurasi Alembic:** `pertemuan_6/alembic.ini`

---

## Catatan Penting

* Pastikan virtual environment aktif sebelum menjalankan aplikasi
* Jalankan `seed_db.py` hanya satu kali
* Port default aplikasi adalah **6543**
* Penamaan `matakuliahs` mengikuti konvensi internal API
