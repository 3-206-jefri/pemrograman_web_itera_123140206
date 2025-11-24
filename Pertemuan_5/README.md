# Sistem Manajemen Perpustakaan Sederhana

Sistem Manajemen perpustakaan sederhana yang dirancang menggunakan konsep OOP python.

## Fitur dan Fungsinya

### Inheritance
inheritance dimana ini merupakan konsep pewarisan antara subclass mewarisi attribute dan method dari super class. 
berikut merupakan contoh code dari penggunakan Inheritance.

```
from Library_Item import LibraryItem
class Book(LibraryItem):
    
    
    def __init__(self, item_id: str, title: str, author: str, year: int, pages: int):
        super().__init__(item_id, title, year)
```

Dapat dilihat di dalam class Book memanggil superclass dari class LibraryItem dan penggunaannya ada di `super().__init__(item_id, title, year)` yg artinya class ini memanggil atribute , item_id, title , dan year dari superclass.

### Abstact
Abtract class adalah class yang tidak membuat object langsung dimana artinya class ini dibuat sebagi kerangka untuk class lain atau child class.

Berikut merupakan contoh code penggunaan dari Abstract class

```
from abc import ABC, abstractmethod

class LibraryItem(ABC):

@abstractmethod
def display_info(self) -> str:
    pass
    
@abstractmethod
def get_type(self) -> str: 
    pass
```

Kenapa ini meruapakan abstact class ? karena dapat di lihat pada class `LibraryItem` itu mewarisi Abstract Base Class (ABC)  dan menggunakan `@abstactmethod` dimana metode ini lah yang akan menjadi kerangka dan harus di implementasikan di class lain nantinya.


### Encapsulation 
Encapsulation adalah konsep oop yang meyembunyikan attribute agar tidak bisa di akses langsung dari luar kelas yang hanya dapat di akses melalui method getter dan setter.

Contoh penerapannya.

`self.__name = name`

artinya attribute ini merupakan private attribute dan tidak bisa di akses langsung tanpa methode setter dan getter.

### Polymorphism
Polymorphism adalah konsep oop yang dimana memungkinkan untuk menamai metode dengan nama yang sama namun menghasilkan hasil yang dapat berbeda.

Contoh penerapan.

```
 def display_info(self) -> str:
       
        status = "Tersedia" if self._is_available else "Dipinjam"
        return (f"[BUKU] ID: {self.item_id} | Judul: {self._title} | "
                f"Penulis: {self._author} | Tahun: {self._year} | "
                f"Halaman: {self._pages} | Status: {status}")
```
```
def display_info(self) -> str:
       
        status = "Tersedia" if self._is_available else "Dipinjam"
        return (f"[DVD] ID: {self.item_id} | Judul: {self._title} | "
                f"Sutradara: {self._director} | Tahun: {self._year} | "
                f"Durasi: {self._duration} menit | Status: {status}")
```

bisa dilihat penamaan metodenya sama namun menghasilkan hasil yang berbeda , yang mana dapat dilihat pada bagian pertama untuk buku dan bagian 2 untuk dvd.

### Running Program & Screenshot

- Awal Running Program
<img width="758" height="179" alt="image" src="https://github.com/user-attachments/assets/bbb1ed77-df09-4dc7-9d3b-3d1d64dafdcd" />

Pengguna diminta untuk memasukkan nama perpustakaan

- Tampilan pilihan

<img width="741" height="342" alt="image" src="https://github.com/user-attachments/assets/3115e53b-ef3f-476b-a558-aefe924c8365" />


pengguna dapat memilih fitur fitur yang tersedia di dalam tampilan.

- Fitur Menambahkan Buku , Majalah dan DVD

<img width="764" height="333" alt="image" src="https://github.com/user-attachments/assets/bc9f4d20-a7a8-4eea-a6dc-d48ac0fff5b2" />
<img width="752" height="330" alt="image" src="https://github.com/user-attachments/assets/1f736acd-27c6-46b8-a0ea-733bc334c030" />
<img width="772" height="256" alt="image" src="https://github.com/user-attachments/assets/5366370b-0a05-4188-b278-ef6b0e5f99e5" />

Pengguna dapat menambahkan buku , majalah dan dvd dan saat ingin menamabahkan pengguna diminta untuk mengisi parameter -parameter yang sudah disediakan oleh program.

- Menampilkan item

<img width="992" height="248" alt="image" src="https://github.com/user-attachments/assets/f17e6aee-5cbc-443c-bb6e-13522177dfef" />

<img width="981" height="188" alt="image" src="https://github.com/user-attachments/assets/cb78c91a-a7e6-4424-8aa7-cc07483ce971" />

- Cari item berdasarkan judul atau id
  
<img width="926" height="261" alt="image" src="https://github.com/user-attachments/assets/4a774761-1502-4045-8048-dc9c0f14cef8" />

<img width="926" height="214" alt="image" src="https://github.com/user-attachments/assets/bc4af769-ffde-4315-836d-4b0159188166" />

Pda menu pencarian ini pengguna diminta memasukan judul atau id item tergantung pilihan dari pengguna ingin mengunakan metode pencarian seperti apa.

- Pinjam dan kembalikan item

<img width="1002" height="290" alt="image" src="https://github.com/user-attachments/assets/d4d07d8b-284b-42e4-a6a5-b3f7d14f8441" />

<img width="1040" height="247" alt="image" src="https://github.com/user-attachments/assets/6393516a-1512-435a-acae-e69ee39ace28" />

Fitur ini merupakan fitur dimana pengguna dapat meminjam dan pengembalikan buku yang sudah di pinjam. Ketika item dipinjam status item otomatis akan berubah menjadi tersedia -> dipinjam. Tampilan item akan berubah saat pengguna ingin menampilkan semua item.











