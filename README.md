#  Aplikasi Manajemen Tugas Mahasiswa
> **Tugas Praktikum – Pemrograman Web (ITERA)**  
> Oleh: **Jefri Wahyu Fernando Sembiring – 123140206 – RC**

---

##  Deskripsi Singkat
Aplikasi **Manajemen Tugas Mahasiswa (MTM)** adalah aplikasi berbasis web yang dirancang untuk membantu mahasiswa mengatur dan memantau tugas akademik mereka.  
Aplikasi ini bersifat **interaktif**, **fungsional**, dan menyimpan data secara **lokal (localStorage)** sehingga data tetap tersimpan walaupun browser ditutup.

Dibuat menggunakan:
- **HTML5 Semantik** – untuk struktur halaman
- **CSS3** – untuk tampilan antarmuka
- **JavaScript (ES6+)** – untuk logika dan interaksi pengguna

---

## Fitur Utama

| No | Fitur | Status | Deskripsi |
|:--:|:------|:------:|:----------|
| 1 | **Tambah Tugas Baru** | ✅ | Pengguna dapat menambahkan tugas dengan nama, mata kuliah, dan deadline. |
| 2 | **Edit Tugas** | ✅ | Mengubah data tugas melalui dialog/prompt. |
| 3 | **Tandai Selesai / Belum** | ✅ | Mengubah status tugas tanpa menghapus data. |
| 4 | **Hapus Tugas** | ✅ | Menghapus tugas yang tidak diperlukan. |
| 5 | **Pencarian & Filter** | ✅ | Menyaring daftar tugas berdasarkan nama atau mata kuliah. |
| 6 | **Hitung Jumlah Tugas Belum Selesai** | ✅ | Menampilkan total tugas yang belum dikerjakan. |
| 7 | **Validasi Form** | ✅ | Memastikan semua input valid dan deadline tidak di masa lalu. |
| 8 | **Penyimpanan Lokal (localStorage)** | ✅ | Semua data disimpan secara permanen di browser pengguna. |

---

## 🧠 Penjelasan Teknis

### 🔹 1. Penggunaan `localStorage`
Data tugas disimpan secara lokal agar tetap tersimpan meski halaman direfresh.

```javascript
// Memuat data dari localStorage
let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// Menyimpan data ke localStorage
function saveTasks() {
  localStorage.setItem('tasks', JSON.stringify(tasks));
}
