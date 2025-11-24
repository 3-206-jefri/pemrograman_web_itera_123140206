from typing import List, Optional
from Library_Item import LibraryItem
from typing import List, Optional

class Library:

    
    def __init__(self, name: str):
        self.__name = name  # Private attribute
        self.__items: List[LibraryItem] = []  # Private collection
    
   
    @property
    def name(self):
        return self.__name
    
    @property
    def total_items(self):
       
        return len(self.__items)
    
  
    
    def add_item(self, item: LibraryItem) -> bool:
       
        # Validasi: cek apakah ID sudah ada
        if any(i.item_id == item.item_id for i in self.__items):
            print(f" Item dengan ID {item.item_id} sudah ada!")
            return False
        
        self.__items.append(item)
        print(f" {item.get_type()} '{item.title}' berhasil ditambahkan!")
        return True
    
    def display_all_items(self):
        if not self.__items:
            print("\n Perpustakaan masih kosong.")
            return
        
        print(f"\n{'='*80}")
        print(f" Daftar Item di Perpustakaan {self.__name}")
        print(f"{'='*80}")
        
        # Polymorphism: setiap item memanggil display_info() versi mereka sendiri
        for item in self.__items:
            print(item.display_info())
        
        print(f"{'='*80}")
        print(f"Total item: {self.total_items}")
    
    def display_available_items(self):
        
        # Filter item yang tersedia menggunakan list comprehension
        available = [item for item in self.__items if item.is_available]
        
        if not available:
            print("\n Tidak ada item yang tersedia saat ini.")
            return
        
        print(f"\n{'='*80}")
        print(f" Item Tersedia di Perpustakaan {self.__name}")
        print(f"{'='*80}")
        for item in available:
            print(item.display_info())
        print(f"{'='*80}")
        print(f"Total tersedia: {len(available)}")
    
    # ========== SEARCH OPERATIONS ==========
    
    def search_by_title(self, title: str) -> List[LibraryItem]:
        
        title_lower = title.lower()
        # List comprehension dengan kondisi substring matching
        results = [item for item in self.__items 
                   if title_lower in item.title.lower()]
        
        if not results:
            print(f"\n Item dengan judul '{title}' tidak ditemukan.")
            return []
        
        print(f"\n Hasil pencarian untuk '{title}':")
        print(f"{'-'*80}")
        for item in results:
            print(item.display_info())
        print(f"{'-'*80}")
        return results
    
    def search_by_id(self, item_id: str) -> Optional[LibraryItem]:
       
        for item in self.__items:
            if item.item_id == item_id:
                print(f"\n🔍 Item ditemukan:")
                print(f"{'-'*80}")
                print(item.display_info())
                print(f"{'-'*80}")
                return item
        
        print(f"\n Item dengan ID '{item_id}' tidak ditemukan.")
        return None
        
    def borrow_item(self, item_id: str) -> bool:
        
        item = self.search_by_id(item_id)
        if item and item.borrow():
            print(f" Berhasil meminjam '{item.title}'")
            return True
        elif item:
            print(f" '{item.title}' sedang dipinjam")
        return False
    
    def return_item(self, item_id: str) -> bool:
        
        item = self.search_by_id(item_id)
        if item and item.return_item():
            print(f" Berhasil mengembalikan '{item.title}'")
            return True
        elif item:
            print(f" '{item.title}' tidak sedang dipinjam")
        return False