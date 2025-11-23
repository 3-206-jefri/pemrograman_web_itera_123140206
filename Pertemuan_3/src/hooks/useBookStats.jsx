import { useState, useEffect } from 'react';

/**
 * Custom Hook untuk menghitung statistik buku
 * @param {Array} books - Array of book objects
 * @returns {Object} stats - Object berisi statistik buku
 */
const useBookStats = (books) => {
  const [stats, setStats] = useState({
    total: 0,
    owned: 0,
    reading: 0,
    wishlist: 0
  });

  useEffect(() => {
    // Hitung statistik setiap kali books berubah
    const newStats = {
      total: books.length,
      owned: books.filter(book => book.status === 'milik').length,
      reading: books.filter(book => book.status === 'baca').length,
      wishlist: books.filter(book => book.status === 'beli').length
    };
    
    setStats(newStats);
  }, [books]); // Dependency array - akan re-run jika books berubah

  return stats;
};

export default useBookStats;