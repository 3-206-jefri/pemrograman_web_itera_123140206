from Library_Item import LibraryItem

class DVD(LibraryItem):
    """
    Class DVD yang mewarisi dari LibraryItem.
    
    Merepresentasikan DVD dalam sistem perpustakaan dengan informasi
    tambahan seperti sutradara dan durasi.
    
    Attributes:
        _director (str): Nama sutradara
        _duration (int): Durasi dalam menit
    """
    
    def __init__(self, item_id: str, title: str, director: str, year: int, duration: int):
        """
        Constructor untuk membuat object DVD.
        
        Args:
            item_id (str): ID unik DVD
            title (str): Judul DVD
            director (str): Nama sutradara
            year (int): Tahun rilis
            duration (int): Durasi dalam menit
        """
        super().__init__(item_id, title, year)
        self._director = director
        self._duration = duration
    
    # ========== PROPERTY DECORATORS ==========
    
    @property
    def director(self):
        """Getter untuk mengakses nama sutradara"""
        return self._director
    
    @property
    def duration(self):
        """Getter untuk mengakses durasi"""
        return self._duration
    
    # ========== IMPLEMENTASI ABSTRACT METHODS (Polymorphism) ==========
    
    def display_info(self) -> str:
        """
        Implementasi method abstract untuk menampilkan info DVD.
        
        Returns:
            str: Informasi lengkap DVD dalam format terstruktur
        """
        status = "Tersedia" if self._is_available else "Dipinjam"
        return (f"[DVD] ID: {self.item_id} | Judul: {self._title} | "
                f"Sutradara: {self._director} | Tahun: {self._year} | "
                f"Durasi: {self._duration} menit | Status: {status}")
    
    def get_type(self) -> str:
        """
        Implementasi method abstract untuk mendapatkan tipe item.
        
        Returns:
            str: Tipe item yaitu "DVD"
        """
        return "DVD"