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
