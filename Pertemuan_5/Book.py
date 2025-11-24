from Library_Item import LibraryItem
class Book(LibraryItem):
    """
    Class Book yang mewarisi dari LibraryItem.
    
    Merepresentasikan buku dalam sistem perpustakaan dengan informasi
    tambahan seperti penulis dan jumlah halaman.
    
    Attributes:
        _author (str): Nama penulis buku
        _pages (int): Jumlah halaman buku
    """
    
    def __init__(self, item_id: str, title: str, author: str, year: int, pages: int):
        """
        Constructor untuk membuat object Book.
        
        Args:
            item_id (str): ID unik buku
            title (str): Judul buku
            author (str): Nama penulis
            year (int): Tahun terbit
            pages (int): Jumlah halaman
        """
        # Memanggil constructor parent class
        super().__init__(item_id, title, year)
        self._author = author
        self._pages = pages
    
    # ========== PROPERTY DECORATORS ==========
    
    @property
    def author(self):
        """Getter untuk mengakses nama penulis"""
        return self._author
    
    @property
    def pages(self):
        """Getter untuk mengakses jumlah halaman"""
        return self._pages
    
    # ========== IMPLEMENTASI ABSTRACT METHODS (Polymorphism) ==========
    
    def display_info(self) -> str:
        """
        Implementasi method abstract untuk menampilkan info buku.
        Ini adalah contoh POLYMORPHISM - method yang sama tapi implementasi berbeda.
        
        Returns:
            str: Informasi lengkap buku dalam format terstruktur
        """
        status = "Tersedia" if self._is_available else "Dipinjam"
        return (f"[BUKU] ID: {self.item_id} | Judul: {self._title} | "
                f"Penulis: {self._author} | Tahun: {self._year} | "
                f"Halaman: {self._pages} | Status: {status}")
    
    def get_type(self) -> str:
        """
        Implementasi method abstract untuk mendapatkan tipe item.
        
        Returns:
            str: Tipe item yaitu "Buku"
        """
        return "Buku"