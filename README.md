3. Buka file `index.html` di browser (Chrome, Edge, Firefox, dll).
4. Aplikasi langsung dapat digunakan tanpa server tambahan.

---

## 💡 Fitur-Fitur yang Diimplementasikan

| Fitur | Deskripsi |
|-------|------------|
| ➕ **Tambah Tugas** | Menambahkan tugas baru dengan nama, mata kuliah, dan deadline |
| ✏️ **Edit Tugas** | Mengubah nama, mata kuliah, atau deadline tugas |
| ✅ **Tandai Selesai/Belum** | Mengubah status tugas menjadi selesai atau belum selesai |
| ❌ **Hapus Tugas** | Menghapus tugas yang tidak diperlukan |
| 🔍 **Pencarian / Filter** | Mencari tugas berdasarkan nama atau mata kuliah |
| 📊 **Hitung Jumlah Tugas Belum Selesai** | Menampilkan jumlah tugas yang belum diselesaikan |
| 💾 **Penyimpanan Lokal (localStorage)** | Menyimpan semua data di browser pengguna |
| ⚠️ **Validasi Form** | Mencegah input kosong atau deadline tidak valid |

---

## 🧠 Penjelasan Teknis

### 1. Penyimpanan Data Menggunakan `localStorage`
Aplikasi ini menggunakan **localStorage** untuk menyimpan data secara lokal di browser pengguna.  
Data akan tetap tersimpan meskipun browser ditutup atau halaman direfresh.

#### Kode penyimpanan:
```javascript
// Menyimpan array tugas ke localStorage
localStorage.setItem('tasks', JSON.stringify(tasks));

// Mengambil data saat halaman pertama kali dibuka
let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
