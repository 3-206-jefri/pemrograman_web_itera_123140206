# Pertemuan 1
###  Deskripsi Singkat
Aplikasi Manajemen Tugas Mahasiswa  adalah aplikasi berbasis web yang dirancang untuk membantu mahasiswa mengatur dan memantau tugas akademik mereka.  
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

## Screenshot

### UI
<img width="1215" height="688" alt="image" src="https://github.com/user-attachments/assets/6f67172e-d809-4c91-a73a-4453fe252a96" />

## Fitur CRUD Dasar
<img width="1061" height="644" alt="image" src="https://github.com/user-attachments/assets/33b2039e-a0b2-4f4c-b0f0-c16f55a993a2" />

<img width="1018" height="649" alt="image" src="https://github.com/user-attachments/assets/5ca66d41-5a99-4976-8025-0c8c166b2c65" />

<img width="1064" height="601" alt="image" src="https://github.com/user-attachments/assets/c9f64839-cdc4-42b0-af3a-6f9c0351d002" />

<img width="980" height="626" alt="image" src="https://github.com/user-attachments/assets/35dd34c2-a1ea-4f82-96a4-3e54eb671442" />

### Validation

<img width="934" height="409" alt="image" src="https://github.com/user-attachments/assets/b849296a-de4d-4e4d-b846-5b0a5e1fb5d7" />

<img width="943" height="459" alt="image" src="https://github.com/user-attachments/assets/3bc316ee-782d-4b9f-8759-3579b2bc34a1" />


## Search
<img width="939" height="67" alt="image" src="https://github.com/user-attachments/assets/5a74fcad-cb10-4ffa-b41a-f0c6a52bd4a8" />

## Status
<img width="915" height="286" alt="image" src="https://github.com/user-attachments/assets/790c5fde-84d7-47ab-8c1c-86e4804245f6" />


###  Cara Menjalankan

1. **Download** repository `Jefri Wahyu Fernando Sembiring_123140206_Tugas 1`
2. **Buka** file `index.html` menggunakan browser (disarankan Google Chrome)
3. Jika menggunakan **VS Code**, jalankan melalui ekstensi **Live Server**


## ⚙️ Penjelasan Teknis

### Penggunaan `localStorage`

Penggunaan `localStorage` pada aplikasi ini bertujuan untuk **menyimpan data tugas secara lokal di browser**.  
Data disimpan dalam bentuk **JSON**, sehingga data tetap tersedia meskipun browser ditutup atau halaman direfresh.

`localStorage` hanya dapat menyimpan data bertipe *string*, oleh karena itu data array JavaScript perlu dikonversi terlebih dahulu menggunakan `JSON.stringify()` sebelum disimpan, dan dikembalikan menjadi array menggunakan `JSON.parse()` saat dimuat kembali.

---

#### 🧩 Contoh Kode

```javascript
export const getTasks = () => JSON.parse(localStorage.getItem('tasks')) || [];
export const saveTasks = tasks => localStorage.setItem('tasks', JSON.stringify(tasks));
```

### Validasi Form 

Validasi form dengan **JavaScript** digunakan untuk memastikan data yang dimasukkan oleh pengguna **tidak kosong**, serta **tanggal deadline tidak lebih kecil dari hari ini** sebelum data disimpan ke `localStorage`.  
Dengan validasi ini, aplikasi menjadi lebih aman dari kesalahan input dan data yang tidak logis.

---

##  Kode Validasi

```javascript
taskForm.addEventListener('submit', e => {
  e.preventDefault(); // Mencegah halaman reload

  const name = document.getElementById('taskName').value.trim();
  const course = document.getElementById('taskCourse').value.trim();
  const deadline = document.getElementById('taskDeadline').value;

  let isValid = true;
  let message = '';

  // Validasi field kosong
  if (!name) {
    isValid = false;
    message += '- Judul tugas wajib diisi.\n';
  }

  if (!course) {
    isValid = false;
    message += '- Nama mata kuliah wajib diisi.\n';
  }

  if (!deadline) {
    isValid = false;
    message += '- Deadline wajib diisi.\n';
  }

  // Validasi tanggal deadline
  if (deadline) {
    const today = new Date();
    const selectedDate = new Date(deadline);

    today.setHours(0, 0, 0, 0);
    selectedDate.setHours(0, 0, 0, 0);

    if (selectedDate < today) {
      isValid = false;
      message += '- Tanggal deadline tidak boleh sebelum tanggal hari ini.\n';
    }
  }

  // Jika data tidak valid, tampilkan pesan peringatan dan hentikan proses
  if (!isValid) {
    alert('Periksa kembali input Anda:\n\n' + message);
    return;
  }

  // Jika semua validasi lolos, data disimpan ke localStorage
  tasks.push({ name, course, deadline, done: false });
  saveTasks();
  taskForm.reset();
});

```


| Bagian Kode                                  | Fungsi                                                                                              |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `preventDefault()`                           | Mencegah perilaku bawaan form agar tidak me-refresh halaman.                                        |
| `trim()`                                     | Menghapus spasi di awal dan akhir input agar tidak dianggap sebagai data kosong.                    |
| Pemeriksaan `if (!name)` dll.                | Mengecek apakah input kosong. Jika iya, `isValid` diset ke `false` dan pesan kesalahan ditambahkan. |
| Pemeriksaan tanggal (`selectedDate < today`) | Memastikan deadline tidak lebih kecil dari tanggal hari ini.                                        |
| `alert(message)`                             | Menampilkan pesan kesalahan jika validasi gagal.                                                    |
| `return`                                     | Menghentikan eksekusi fungsi jika validasi gagal agar data tidak tersimpan.                         |
| `saveTasks()`                                | Menyimpan data ke `localStorage` jika semua input valid.                                            |
| `reset()`                                    | Mengosongkan form setelah data berhasil disimpan.                                                   |
