> **Tugas Praktikum – Pemrograman Web **  
> Oleh: **Jefri Wahyu Fernando Sembiring – 123140206 – RC**

---
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




# Pertemuan 2
## Deskripsi Singkat
Aplikasi Personal Dashboard (Dasbor Pribadi) adalah sebuah aplikasi yang memungkinkan pengguna untuk menambahkan daftar tugas , dan membuat catatan dimana memiliki beberapa fungsi yaitu untuk mengedit , menghapus  , dan mengeubah status
tugas, dimana pembuatan aplikasi ini bertujuan untuk membantu pribadi atau pengguna mengelolah tugas , dan catatan pribadi.


## Fitur Fitur 

### Penyimpanan Data Lokal ( Local Storage ) 
- **Menggunakan Class `Penyimpanan` untuk menyimpan dan membuat data ke `localStorage` Browser**
- **Data yang disimpan berupa objeck `{ tugas : [] , catatan : [] }` jadi informasi tidak hilang saat halaman di refresh**

### Manajemen Tugas (To - Do List)
Fitur ini mengelola tugas pengguna
- **Tambah tugas :** lewat form `taskForm` , pengguna bisa menambahkan tugas berisi judul dan deskripsi
- **Tandai Selesai / Batal :** tombol "Selesai" atau "Batal" untuk menandai tugas selesai atau belum.
- **Edit Tugas :** pengguna bisa mengubah judul dan deskripsi lewat prompt.
- **Hapus Tugas :** tugas bisa dihapus dengan konfirmasi.
- **Tampilan Dinamis:** daftar tugas diperbaharui secara langsung tanpa reload.


### Manajemen Catatan (Notes)
Mirip seperti fitur tugas , tapi khusus untuk catatan.
- **Tambah Catatan :**  lewat form  `noteForm` , bisa menbamhkan catatan baru judul dan isi.
- **Edit Catatan :** ubah judul dan isi catatan lewat prompt.
- **Hapus Catatan :** hapus catatan dengan konfirmasi
- **Tampilkan Langsung :** daftar catatan diperbarui otomatis di halaman.


### Jam Real-Time
- Elemen `#Clock` akan menampilkan waktu sekarang `(toLocaleString(`id-ID`))` yang diperbarui setiap detik menggunakan `SetInterval`

### ID Unik dan Format Tanggal
- Fungsi `buatID()` menghasilkan ID acak unik untuk setiap tugas/catatan.
- Fungsi `FormatTanggal()` menampilkan tanggal dalam format lokal Indonesia.

## Screenshot

<img width="1657" height="757" alt="image" src="https://github.com/user-attachments/assets/415ae7ed-4e64-403a-bd22-d368559d7c4b" />



## Daftar Fitur ES6+ yang Diimplementasikan
|  No |  Fitur ES6+                                                    |  Contoh dalam Kode                                                                                                |  Penjelasan Singkat                                                                                              |
| :---: | :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------- |
|   1   | **Class Syntax (`class`, `constructor`)**                        | `js class Penyimpanan { constructor(kunci = 'dasbor_pribadi_v1') { this.kunci = kunci; } } `                        | Pendeklarasian class `Penyimpanan` untuk membungkus fungsi `simpan()` dan `muat()` — gaya OOP modern ES6.          |
|   2   | **Default Parameter**                                            | `js constructor(kunci = 'dasbor_pribadi_v1')`                                                                       | Nilai default diberikan ke parameter `kunci` jika tidak ada argumen saat class diinstansiasi.                      |
|   3   | **Arrow Function (`=>`)**                                        | `js const buatID = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 7);`                         | Fungsi pendek tanpa kata `function`, otomatis mewarisi `this` dari scope di atasnya.                               |
|   4   | **Template Literal (Backtick & Interpolasi)**                    | ``js div.innerHTML = `<div class="title">${c.judul}</div>`;``                                                       | Menggunakan backtick `` ` `` dan `${}` untuk menyisipkan variabel langsung dalam string HTML.                      |
|   5   | **Destructuring Assignment (parsial)**                           | Tidak eksplisit besar, tapi ada pola seperti `const { tugas, catatan } = data;` yang bisa ditambahkan dengan mudah. | ES6 mendukung pembongkaran objek, walau di sini lebih banyak memakai akses langsung `data.tugas`.                  |
|   6   | **Object Literal Enhancements**                                  | `js const baru = { id: buatID(), judul, isi, dibuat: Date.now() };`                                                 | Menyingkat penulisan `judul: judul` menjadi `judul` karena nama variabel dan properti sama.                        |
|   7   | **Promise & Async/Await**                                        | `js async simpan(data) { return new Promise((resolve) => { ... }); }` dan `await simpan();`                         | Menggunakan `Promise` untuk simulasi penyimpanan asynchronous, serta `async/await` agar penulisan lebih sederhana. |
|   8   | **`const` dan `let`**                                            | `js const simpanan = new Penyimpanan(); let data = { tugas: [], catatan: [] };`                                     | Mengganti `var` dari JS lama dengan `let` (bisa diubah) dan `const` (tidak bisa diubah referensinya).              |
|   9   | **Array Method Modern (`forEach`, `find`, `filter`, `unshift`)** | `js data.tugas.forEach(t => {...}); data.tugas.find(t => t.id === id); data.tugas = data.tugas.filter(...);`        | Metode array modern ES5–ES6 untuk iterasi, pencarian, dan manipulasi elemen secara deklaratif.                     |
|   10  | **String Method Modern (`includes`, `trim`)**                    | `js const judul = document.getElementById('taskTitle').value.trim();`                                               | `trim()` adalah fitur ES6+ untuk menghapus spasi di awal/akhir string.                                             |
|   11  | **Optional Chaining (tidak digunakan, tapi mudah ditambah)**     | Bisa diterapkan seperti: `tugas?.judul`                                                                             | Walau belum ada di kode, sintaks ini bisa digunakan jika kamu ingin akses aman ke properti bersarang.              |
|   12  | **Arrow Function dalam Callback Event Listener**                 | `js formTugas.addEventListener('submit', async (e) => { ... });`                                                    | Fungsi callback berbentuk arrow untuk event handling.                                                              |
|   13  | **Dynamic Property Access dan Data Attribute (`dataset`)**       | `js const id = e.target.closest('.item').dataset.id;`                                                               | Mengambil data dari atribut `data-id` menggunakan fitur modern DOM ES6.                                            |












