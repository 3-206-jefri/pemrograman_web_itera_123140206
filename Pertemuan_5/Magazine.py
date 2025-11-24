from Library_Item import LibraryItem
class Magazine(LibraryItem):
    """
    Class Magazine yang mewarisi dari LibraryItem.
    
    Merepresentasikan majalah dalam sistem perpustakaan dengan informasi
    tambahan seperti penerbit dan nomor edisi.
    
    Attributes:
        _publisher (str): Nama penerbit majalah
        _issue_number (int): Nomor edisi majalah
    """
    
    def __init__(self, item_id: str, title: str, publisher: str, year: int, issue_number: int):
        """
        Constructor untuk membuat object Magazine.
        
        Args:
            item_id (str): ID unik majalah
            title (str): Judul majalah
            publisher (str): Nama penerbit
            year (int): Tahun terbit
            issue_number (int): Nomor edisi
        """
        super().__init__(item_id, title, year)
        self._publisher = publisher
        self._issue_number = issue_number
    
    # ========== PROPERTY DECORATORS ==========
    
    @property
    def publisher(self):
        """Getter untuk mengakses nama penerbit"""
        return self._publisher
    
    @property
    def issue_number(self):
        """Getter untuk mengakses nomor edisi"""
        return self._issue_number
    
    # ========== IMPLEMENTASI ABSTRACT METHODS (Polymorphism) ==========
    
    def display_info(self) -> str:
        """
        Implementasi method abstract untuk menampilkan info majalah.
        Format berbeda dari Book - ini adalah POLYMORPHISM.
        
        Returns:
            str: Informasi lengkap majalah dalam format terstruktur
        """
        status = "Tersedia" if self._is_available else "Dipinjam"
        return (f"[MAJALAH] ID: {self.item_id} | Judul: {self._title} | "
                f"Penerbit: {self._publisher} | Tahun: {self._year} | "
                f"Edisi: #{self._issue_number} | Status: {status}")
    
    def get_type(self) -> str:
        """
        Implementasi method abstract untuk mendapatkan tipe item.
        
        Returns:
            str: Tipe item yaitu "Majalah"
        """
        return "Majalah"