from Library_Item import LibraryItem
class Magazine(LibraryItem):

    
    def __init__(self, item_id: str, title: str, publisher: str, year: int, issue_number: int):
        
        super().__init__(item_id, title, year)
        self._publisher = publisher
        self._issue_number = issue_number
    
    
    @property
    def publisher(self):
        """Getter untuk mengakses nama penerbit"""
        return self._publisher
    
    @property
    def issue_number(self):
        """Getter untuk mengakses nomor edisi"""
        return self._issue_number
    
    
    def display_info(self) -> str:
        
        status = "Tersedia" if self._is_available else "Dipinjam"
        return (f"[MAJALAH] ID: {self.item_id} | Judul: {self._title} | "
                f"Penerbit: {self._publisher} | Tahun: {self._year} | "
                f"Edisi: #{self._issue_number} | Status: {status}")
    
    def get_type(self) -> str:
       
        return "Majalah"