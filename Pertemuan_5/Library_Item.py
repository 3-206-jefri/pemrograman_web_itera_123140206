from abc import ABC, abstractmethod

class LibraryItem(ABC):
    """
    Abstract Base Class untuk semua item di perpustakaan.
    
    Class ini menjadi template dasar untuk semua jenis item perpustakaan
    seperti buku, majalah, DVD, dll. Menggunakan konsep abstraction untuk
    memaksa subclass mengimplementasikan method tertentu.
    
    Attributes:
        __item_id (str): ID unik item (private)
        _title (str): Judul item (protected)
        _year (int): Tahun terbit (protected)
        _is_available (bool): Status ketersediaan (protected)
    """
    
    def __init__(self, item_id: str, title: str, year: int):
        """
        Constructor untuk inisialisasi item perpustakaan.
        
        Args:
            item_id (str): ID unik untuk item
            title (str): Judul item
            year (int): Tahun terbit
        """
        self.__item_id = item_id  # Private: tidak bisa diakses langsung
        self._title = title        # Protected: bisa diakses oleh subclass
        self._year = year
        self._is_available = True  # Default: item tersedia
    
    # ========== PROPERTY DECORATORS (Encapsulation) ==========
    
    @property
    def item_id(self):
        """Getter untuk mengakses ID item (read-only)"""
        return self.__item_id
    
    @property
    def title(self):
        """Getter untuk mengakses judul item"""
        return self._title
    
    @title.setter
    def title(self, value):
        """
        Setter untuk mengubah judul dengan validasi.
        
        Args:
            value (str): Judul baru
            
        Raises:
            ValueError: Jika judul kosong
        """
        if not value or len(value.strip()) == 0:
            raise ValueError("Judul tidak boleh kosong")
        self._title = value
    
    @property
    def is_available(self):
        """Getter untuk mengecek ketersediaan item"""
        return self._is_available
    
    # ========== ABSTRACT METHODS (harus diimplementasikan subclass) ==========
    
    @abstractmethod
    def display_info(self) -> str:
        """
        Method abstract untuk menampilkan informasi item.
        Setiap subclass HARUS mengimplementasikan method ini.
        
        Returns:
            str: Informasi lengkap item dalam format string
        """
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        """
        Method abstract untuk mendapatkan tipe item.
        Setiap subclass HARUS mengimplementasikan method ini.
        
        Returns:
            str: Tipe item (contoh: "Buku", "Majalah")
        """
        pass
    
    # ========== CONCRETE METHODS (bisa langsung digunakan) ==========
    
    def borrow(self) -> bool:
        """
        Method untuk meminjam item dari perpustakaan.
        
        Returns:
            bool: True jika berhasil dipinjam, False jika tidak tersedia
        """
        if self._is_available:
            self._is_available = False
            return True
        return False
    
    def return_item(self) -> bool:
        """
        Method untuk mengembalikan item ke perpustakaan.
        
        Returns:
            bool: True jika berhasil dikembalikan, False jika sudah tersedia
        """
        if not self._is_available:
            self._is_available = True
            return True
        return False
