from Library_Item import LibraryItem
from Book import Book
from Magazine import Magazine
from DVD import DVD
from Library import Library

def clear_screen():
    """Membersihkan layar (opsional, bisa di-uncomment jika diperlukan)"""
    # import os
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 2)

def display_menu():
    """
    Menampilkan menu utama aplikasi.
    """
    print("\n" + "="*80)
    print("SISTEM MANAJEMEN PERPUSTAKAAN".center(80))
    print("="*80)
    print("1. Tambah Buku")
    print("2. Tambah Majalah")
    print("3. Tambah DVD")
    print("4. Tampilkan Semua Item")
    print("5. Tampilkan Item Tersedia")
    print("6. Cari Item (berdasarkan Judul)")
    print("7. Cari Item (berdasarkan ID)")
    print("8. Pinjam Item")
    print("9. Kembalikan Item")
    print("0. Keluar")
    print("="*80)

def get_input(prompt: str, input_type=str, allow_empty=False):
    """
    Helper function untuk mendapatkan input dengan validasi.
    
    Args:
        prompt (str): Pesan yang ditampilkan ke user
        input_type: Tipe data yang diharapkan (str, int, dll)
        allow_empty (bool): Apakah input kosong diperbolehkan
        
    Returns:
        Input yang sudah divalidasi sesuai tipe
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            # Cek jika input kosong
            if not user_input and not allow_empty:
                print("❌ Input tidak boleh kosong!")
                continue
            
            # Konversi ke tipe yang diinginkan
            if input_type == int:
                return int(user_input)
            else:
                return user_input
                
        except ValueError:
            print(f"❌ Input harus berupa {input_type.__name__}!")
        except KeyboardInterrupt:
            print("\n\n❌ Program dibatalkan.")
            exit()

def add_book(library: Library):
    """
    Function untuk menambahkan buku melalui input user.
    
    Args:
        library (Library): Object perpustakaan tempat buku akan ditambahkan
    """
    print("\n" + "-"*80)
    print("TAMBAH BUKU BARU".center(80))
    print("-"*80)
    
    item_id = get_input("Masukkan ID Buku (contoh: B001): ")
    title = get_input("Masukkan Judul Buku: ")
    author = get_input("Masukkan Nama Penulis: ")
    year = get_input("Masukkan Tahun Terbit: ", int)
    pages = get_input("Masukkan Jumlah Halaman: ", int)
    
    # Buat object Book dan tambahkan ke library
    book = Book(item_id, title, author, year, pages)
    library.add_item(book)

def add_magazine(library: Library):
    """
    Function untuk menambahkan majalah melalui input user.
    
    Args:
        library (Library): Object perpustakaan tempat majalah akan ditambahkan
    """
    print("\n" + "-"*80)
    print("TAMBAH MAJALAH BARU".center(80))
    print("-"*80)
    
    item_id = get_input("Masukkan ID Majalah (contoh: M001): ")
    title = get_input("Masukkan Judul Majalah: ")
    publisher = get_input("Masukkan Nama Penerbit: ")
    year = get_input("Masukkan Tahun Terbit: ", int)
    issue_number = get_input("Masukkan Nomor Edisi: ", int)
    
    # Buat object Magazine dan tambahkan ke library
    magazine = Magazine(item_id, title, publisher, year, issue_number)
    library.add_item(magazine)

def add_dvd(library: Library):
    """
    Function untuk menambahkan DVD melalui input user.
    
    Args:
        library (Library): Object perpustakaan tempat DVD akan ditambahkan
    """
    print("\n" + "-"*80)
    print("TAMBAH DVD BARU".center(80))
    print("-"*80)
    
    item_id = get_input("Masukkan ID DVD (contoh: D001): ")
    title = get_input("Masukkan Judul DVD: ")
    director = get_input("Masukkan Nama Sutradara: ")
    year = get_input("Masukkan Tahun Rilis: ", int)
    duration = get_input("Masukkan Durasi (menit): ", int)
    
    # Buat object DVD dan tambahkan ke library
    dvd = DVD(item_id, title, director, year, duration)
    library.add_item(dvd)

def search_by_title_menu(library: Library):
    """
    Function untuk mencari item berdasarkan judul melalui input user.
    
    Args:
        library (Library): Object perpustakaan tempat pencarian dilakukan
    """
    print("\n" + "-"*80)
    print("PENCARIAN BERDASARKAN JUDUL".center(80))
    print("-"*80)
    
    title = get_input("Masukkan kata kunci judul: ")
    library.search_by_title(title)

def search_by_id_menu(library: Library):
    """
    Function untuk mencari item berdasarkan ID melalui input user.
    
    Args:
        library (Library): Object perpustakaan tempat pencarian dilakukan
    """
    print("\n" + "-"*80)
    print("PENCARIAN BERDASARKAN ID".center(80))
    print("-"*80)
    
    item_id = get_input("Masukkan ID item: ")
    library.search_by_id(item_id)

def borrow_item_menu(library: Library):
    """
    Function untuk meminjam item melalui input user.
    
    Args:
        library (Library): Object perpustakaan tempat peminjaman dilakukan
    """
    print("\n" + "-"*80)
    print("PINJAM ITEM".center(80))
    print("-"*80)
    
    item_id = get_input("Masukkan ID item yang akan dipinjam: ")
    library.borrow_item(item_id)

def return_item_menu(library: Library):
    """
    Function untuk mengembalikan item melalui input user.
    
    Args:
        library (Library): Object perpustakaan tempat pengembalian dilakukan
    """
    print("\n" + "-"*80)
    print("KEMBALIKAN ITEM".center(80))
    print("-"*80)
    
    item_id = get_input("Masukkan ID item yang akan dikembalikan: ")
    library.return_item(item_id)

def main():
    """
    Fungsi utama yang menjalankan program dengan menu interaktif.
    
    Program akan terus berjalan sampai user memilih untuk keluar.
    Semua operasi dilakukan secara dinamis berdasarkan input user.
    """
    
    # Inisialisasi perpustakaan
    print("\n" + "="*80)
    print("SELAMAT DATANG DI SISTEM MANAJEMEN PERPUSTAKAAN".center(80))
    print("="*80)
    
    library_name = get_input("\nMasukkan nama perpustakaan: ")
    library = Library(library_name)
    
    print(f"\n✅ Perpustakaan '{library.name}' berhasil dibuat!")
    
    # Loop menu utama
    while True:
        try:
            display_menu()
            choice = get_input("Pilih menu (0-9): ")
            
            # Proses pilihan user
            if choice == "1":
                add_book(library)
            elif choice == "2":
                add_magazine(library)
            elif choice == "3":
                add_dvd(library)
            elif choice == "4":
                library.display_all_items()
            elif choice == "5":
                library.display_available_items()
            elif choice == "6":
                search_by_title_menu(library)
            elif choice == "7":
                search_by_id_menu(library)
            elif choice == "8":
                borrow_item_menu(library)
            elif choice == "9":
                return_item_menu(library)
            elif choice == "0":
                print("\n" + "="*80)
                print("Terima kasih telah menggunakan Sistem Manajemen Perpustakaan!".center(80))
                print("="*80)
                break
            else:
                print("\n❌ Pilihan tidak valid! Silakan pilih menu 0-9.")
            
            # Pause sebelum kembali ke menu
            input("\nTekan Enter untuk melanjutkan...")
            
        except KeyboardInterrupt:
            print("\n\n" + "="*80)
            print("Program dihentikan oleh user.".center(80))
            print("="*80)
            break
        except Exception as e:
            print(f"\n❌ Terjadi error: {e}")
            input("\nTekan Enter untuk melanjutkan...")


# ========== ENTRY POINT ==========
if __name__ == "__main__":
    """
    Entry point program.
    Code di dalam blok ini hanya dijalankan jika file ini dijalankan langsung,
    tidak ketika di-import sebagai module.
    """
    main()
