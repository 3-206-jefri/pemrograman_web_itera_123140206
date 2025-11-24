from typing import List, Optional
from Library_Item import LibraryItem
from typing import List, Optional

class Library:
    """
    Class Library untuk mengelola koleksi item perpustakaan.
    
    Class ini bertanggung jawab untuk menyimpan, mengelola, dan menyediakan
    operasi CRUD (Create, Read, Update, Delete) untuk item perpustakaan.
    Menerapkan konsep ENCAPSULATION dengan menyembunyikan collection internal.
    
    Attributes:
        __name (str): Nama perpustakaan (private)
        __items (List[LibraryItem]): Daftar item perpustakaan (private)
    """
    
    def __init__(self, name: str):
        """
        Constructor untuk membuat object Library.
        
        Args:
            name (str): Nama perpustakaan
        """
        self.__name = name  # Private attribute
        self.__items: List[LibraryItem] = []  # Private collection
    
    # ========== PROPERTY DECORATORS ==========
    
    @property
    def name(self):
        """Getter untuk mengakses nama perpustakaan (read-only)"""
        return self.__name
    
    @property
    def total_items(self):
        """
        Property untuk mendapatkan jumlah total item.
        Computed property - tidak menyimpan nilai, tapi menghitung on-the-fly.
        
        Returns:
            int: Jumlah total item di perpustakaan
        """
        return len(self.__items)
    
    # ========== CRUD OPERATIONS ==========
    
    def add_item(self, item: LibraryItem) -> bool:
        """
        Menambahkan item baru ke perpustakaan.
        
        Method ini memvalidasi bahwa ID item belum ada sebelum menambahkan.
        Ini adalah operasi CREATE dalam CRUD.
        
        Args:
            item (LibraryItem): Object item yang akan ditambahkan
            
        Returns:
            bool: True jika berhasil ditambahkan, False jika ID sudah ada
        """
        # Validasi: cek apakah ID sudah ada
        if any(i.item_id == item.item_id for i in self.__items):
            print(f"❌ Item dengan ID {item.item_id} sudah ada!")
            return False
        
        self.__items.append(item)
        print(f"✅ {item.get_type()} '{item.title}' berhasil ditambahkan!")
        return True
    
    def display_all_items(self):
        """
        Menampilkan semua item di perpustakaan.
        
        Method ini adalah operasi READ dalam CRUD.
        Menggunakan POLYMORPHISM - memanggil display_info() yang berbeda
        untuk setiap tipe item.
        """
        if not self.__items:
            print("\n📚 Perpustakaan masih kosong.")
            return
        
        print(f"\n{'='*80}")
        print(f"📚 Daftar Item di Perpustakaan {self.__name}")
        print(f"{'='*80}")
        
        # Polymorphism: setiap item memanggil display_info() versi mereka sendiri
        for item in self.__items:
            print(item.display_info())
        
        print(f"{'='*80}")
        print(f"Total item: {self.total_items}")
    
    def display_available_items(self):
        """
        Menampilkan hanya item yang tersedia (belum dipinjam).
        
        Menggunakan list comprehension untuk filtering data.
        """
        # Filter item yang tersedia menggunakan list comprehension
        available = [item for item in self.__items if item.is_available]
        
        if not available:
            print("\n❌ Tidak ada item yang tersedia saat ini.")
            return
        
        print(f"\n{'='*80}")
        print(f"📗 Item Tersedia di Perpustakaan {self.__name}")
        print(f"{'='*80}")
        for item in available:
            print(item.display_info())
        print(f"{'='*80}")
        print(f"Total tersedia: {len(available)}")
    
    # ========== SEARCH OPERATIONS ==========
    
    def search_by_title(self, title: str) -> List[LibraryItem]:
        """
        Mencari item berdasarkan judul (case-insensitive, partial match).
        
        Args:
            title (str): Kata kunci judul yang dicari
            
        Returns:
            List[LibraryItem]: List item yang judulnya mengandung kata kunci
        """
        title_lower = title.lower()
        # List comprehension dengan kondisi substring matching
        results = [item for item in self.__items 
                   if title_lower in item.title.lower()]
        
        if not results:
            print(f"\n❌ Item dengan judul '{title}' tidak ditemukan.")
            return []
        
        print(f"\n🔍 Hasil pencarian untuk '{title}':")
        print(f"{'-'*80}")
        for item in results:
            print(item.display_info())
        print(f"{'-'*80}")
        return results
    
    def search_by_id(self, item_id: str) -> Optional[LibraryItem]:
        """
        Mencari item berdasarkan ID (exact match).
        
        Args:
            item_id (str): ID item yang dicari
            
        Returns:
            Optional[LibraryItem]: Object item jika ditemukan, None jika tidak
        """
        for item in self.__items:
            if item.item_id == item_id:
                print(f"\n🔍 Item ditemukan:")
                print(f"{'-'*80}")
                print(item.display_info())
                print(f"{'-'*80}")
                return item
        
        print(f"\n❌ Item dengan ID '{item_id}' tidak ditemukan.")
        return None
    
    # ========== BORROWING OPERATIONS ==========
    
    def borrow_item(self, item_id: str) -> bool:
        """
        Meminjam item dari perpustakaan berdasarkan ID.
        
        Args:
            item_id (str): ID item yang akan dipinjam
            
        Returns:
            bool: True jika berhasil dipinjam, False jika gagal
        """
        item = self.search_by_id(item_id)
        if item and item.borrow():
            print(f"✅ Berhasil meminjam '{item.title}'")
            return True
        elif item:
            print(f"❌ '{item.title}' sedang dipinjam")
        return False
    
    def return_item(self, item_id: str) -> bool:
        """
        Mengembalikan item yang dipinjam ke perpustakaan.
        
        Args:
            item_id (str): ID item yang akan dikembalikan
            
        Returns:
            bool: True jika berhasil dikembalikan, False jika gagal
        """
        item = self.search_by_id(item_id)
        if item and item.return_item():
            print(f"✅ Berhasil mengembalikan '{item.title}'")
            return True
        elif item:
            print(f"❌ '{item.title}' tidak sedang dipinjam")
        return False