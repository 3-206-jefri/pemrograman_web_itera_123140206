from abc import ABC, abstractmethod

class LibraryItem(ABC):
    
    
    def __init__(self, item_id: str, title: str, year: int):
      
        self.__item_id = item_id  # Private: tidak bisa diakses langsung
        self._title = title        # Protected: bisa diakses oleh subclass
        self._year = year
        self._is_available = True  # Default: item tersedia
  
    
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
        
        if not value or len(value.strip()) == 0:
            raise ValueError("Judul tidak boleh kosong")
        self._title = value
    
    @property
    def is_available(self):
        """Getter untuk mengecek ketersediaan item"""
        return self._is_available

    
    @abstractmethod
    def display_info(self) -> str:
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        
        pass
    
   
    
    def borrow(self) -> bool:
       
        if self._is_available:
            self._is_available = False
            return True
        return False
    
    def return_item(self) -> bool:
        
        if not self._is_available:
            self._is_available = True
            return True
        return False
