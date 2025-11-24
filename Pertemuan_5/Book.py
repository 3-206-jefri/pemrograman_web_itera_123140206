from Library_Item import LibraryItem
class Book(LibraryItem):
    
    
    def __init__(self, item_id: str, title: str, author: str, year: int, pages: int):
        super().__init__(item_id, title, year)
        self._author = author
        self._pages = pages
    
    
    @property
    def author(self):
        """Getter untuk mengakses nama penulis"""
        return self._author
    
    @property
    def pages(self):
        """Getter untuk mengakses jumlah halaman"""
        return self._pages
    
   
    
    def display_info(self) -> str:
       
        status = "Tersedia" if self._is_available else "Dipinjam"
        return (f"[BUKU] ID: {self.item_id} | Judul: {self._title} | "
                f"Penulis: {self._author} | Tahun: {self._year} | "
                f"Halaman: {self._pages} | Status: {status}")
    
    def get_type(self) -> str:
        
        return "Buku"