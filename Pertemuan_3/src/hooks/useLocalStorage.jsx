import { useState } from 'react';

/**
 * Custom Hook untuk menyimpan dan mengambil data dari localStorage
 * @param {string} key - Key untuk localStorage
 * @param {any} initialValue - Nilai awal jika tidak ada data di localStorage
 * @returns {Array} [storedValue, setValue] - Value dan function untuk update
 */
const useLocalStorage = (key, initialValue) => {
  // State untuk menyimpan value
  const [storedValue, setStoredValue] = useState(() => {
    try {
      // Ambil data dari localStorage
      const item = window.localStorage.getItem(key);
      // Parse dan return data jika ada, jika tidak return initialValue
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error('Error reading from localStorage:', error);
      return initialValue;
    }
  });

  // Function untuk set value ke localStorage
  const setValue = (value) => {
    try {
      // Allow value to be a function so we have same API as useState
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      
      // Save state
      setStoredValue(valueToStore);
      
      // Save to localStorage
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error('Error saving to localStorage:', error);
    }
  };

  return [storedValue, setValue];
};

export default useLocalStorage;