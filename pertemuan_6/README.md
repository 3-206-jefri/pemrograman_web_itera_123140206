# Aplikasi Manajemen Matakuliah (Pyramid)

## Deskripsi Proyek

API sederhana untuk manajemen data matakuliah menggunakan Pyramid (web framework), SQLAlchemy (ORM), dan SQLite.

Fitur:
- CRUD untuk entitas `Matakuliah` (id, kode_mk, nama_mk, sks, semester)

## Cara Instalasi

1. Buat virtual environment dan aktifkan (direkomendasikan):

```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Instal dependensi:

```powershell
pip install -r requirements.txt
# Jika ada paket yang belum tercantum, pasang manual:
pip install pyramid_tm zope.sqlalchemy
```

3. Verifikasi interpreter (opsional):

```powershell
python --version
where python
```

## Konfigurasi Database

- Default: SQLite file `matakuliah.db` di folder `pertemuan_6`.
- Skema tabel dibuat otomatis melalui `init_db()` yang dipanggil saat aplikasi mulai atau lewat `seed_db.py`.

Jika ingin menggunakan Alembic (migrasi), lihat bagian Migrasi di bawah.

## Migrasi Database (Alembic)

Direktori `alembic/` dan `alembic.ini` tersedia. Contoh perintah:

```powershell
# Buat revision otomatis (setelah mengubah model)
alembic revision --autogenerate -m "create matakuliah"

# Terapkan migration ke head
alembic upgrade head
```

Pastikan `alembic.ini` dan env mengarah ke database yang sama.

## Cara Menjalankan

1. Tambahkan data awal (seed) — hanya jika tabel kosong:

```powershell
python seed_db.py
```

2. Jalankan server:

```powershell
python app.py
```

Server akan tersedia di: `http://localhost:6543`

## API Endpoints

Semua response berformat JSON.

1) Get All Matakuliah
- Method: `GET`
- URL: `/api/matakuliah`
- Contoh request:

```bash
curl -X GET http://localhost:6543/api/matakuliah
```
- Contoh response (200):

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

2) Get Single Matakuliah
- Method: `GET`
- URL: `/api/matakuliah/{id}`
- Contoh request:

```bash
curl -X GET http://localhost:6543/api/matakuliah/1
```
- Contoh response (200):

```json
{
  "status": "success",
  "matakuliah": {
    "id": 1,
    "kode_mk": "IF101",
    "nama_mk": "Algoritma dan Pemrograman",
    "sks": 3,
    "semester": 1
  }
}
```

3) Create Matakuliah
- Method: `POST`
- URL: `/api/matakuliah`
- Body (JSON): `kode_mk`, `nama_mk`, `sks`, `semester` (semua wajib)
- Contoh request:

```bash
curl -X POST http://localhost:6543/api/matakuliah -H "Content-Type: application/json" -d '{"kode_mk":"IF301","nama_mk":"Pemrograman Web","sks":3,"semester":5}'
```
- Contoh response (201):

```json
{
  "status": "success",
  "message": "Matakuliah berhasil ditambahkan",
  "matakuliah": {
    "id": 4,
    "kode_mk": "IF301",
    "nama_mk": "Pemrograman Web",
    "sks": 3,
    "semester": 5
  }
}
```

4) Update Matakuliah
- Method: `PUT`
- URL: `/api/matakuliah/{id}`
- Body: salah satu atau beberapa field untuk diupdate
- Contoh request:

```bash
curl -X PUT http://localhost:6543/api/matakuliah/1 -H "Content-Type: application/json" -d '{"nama_mk":"Algoritma Lanjut"}'
```
- Contoh response (200):

```json
{
  "status": "success",
  "message": "Matakuliah berhasil diupdate",
  "matakuliah": {
    "id": 1,
    "kode_mk": "IF101",
    "nama_mk": "Algoritma Lanjut",
    "sks": 3,
    "semester": 1
  }
}
```

5) Delete Matakuliah
- Method: `DELETE`
- URL: `/api/matakuliah/{id}`
- Contoh request:

```bash
curl -X DELETE http://localhost:6543/api/matakuliah/1
```
- Contoh response (200):

```json
{
  "status": "success",
  "message": "Matakuliah berhasil dihapus"
}
```

## Testing

**Menggunakan `curl.exe` (Windows Git Bash atau WSL):**

```powershell
# 1. Pastikan server berjalan
curl.exe -X GET http://localhost:6543/api/matakuliah

# 2. Tambah data baru
curl.exe -X POST http://localhost:6543/api/matakuliah -H "Content-Type: application/json" -d '{"kode_mk":"IF401","nama_mk":"Jaringan Komputer","sks":3,"semester":6}'

# 3. Update (ganti id sesuai hasil create)
curl.exe -X PUT http://localhost:6543/api/matakuliah/4 -H "Content-Type: application/json" -d '{"nama_mk":"Jaringan Lanjut"}'

# 4. Hapus
curl.exe -X DELETE http://localhost:6543/api/matakuliah/4
```

**Alternatif: Menggunakan PowerShell `Invoke-WebRequest`:**

```powershell
# 1. Get all
Invoke-WebRequest -Uri http://localhost:6543/api/matakuliah -Method GET

# 2. Create
$body = @{
    kode_mk = "IF401"
    nama_mk = "Jaringan Komputer"
    sks = 3
    semester = 6
} | ConvertTo-Json

Invoke-WebRequest -Uri http://localhost:6543/api/matakuliah `
  -Method POST `
  -Headers @{"Content-Type" = "application/json"} `
  -Body $body

# 3. Update
$body = @{nama_mk = "Jaringan Lanjut"} | ConvertTo-Json
Invoke-WebRequest -Uri http://localhost:6543/api/matakuliah/4 `
  -Method PUT `
  -Headers @{"Content-Type" = "application/json"} `
  -Body $body

# 4. Delete
Invoke-WebRequest -Uri http://localhost:6543/api/matakuliah/4 -Method DELETE
```

## File penting

- Entry point & semua views: [pertemuan_6/app.py](pertemuan_6/app.py) - semua endpoint view functions ada di sini
- Model: [pertemuan_6/models.py](pertemuan_6/models.py)
- Database config: [pertemuan_6/database.py](pertemuan_6/database.py)
- Seed script: [pertemuan_6/seed_db.py](pertemuan_6/seed_db.py)
- Alembic config: [pertemuan_6/alembic.ini](pertemuan_6/alembic.ini)
