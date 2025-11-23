import React from 'react';
import { Search } from 'lucide-react';
import { useBooks } from '../context/BookContext';
import './BookFilter.css';

const BookFilter = () => {
  const { searchQuery, setSearchQuery, filterStatus, setFilterStatus } = useBooks();

  const filters = [
    { value: 'all', label: 'Semua' },
    { value: 'milik', label: 'Dimiliki' },
    { value: 'baca', label: 'Sedang Dibaca' },
    { value: 'beli', label: 'Ingin Beli' }
  ];

  return (
    <div className="book-filter">
      <div className="book-filter-content">
        {/* Search Input */}
        <div className="search-container">
          <Search className="search-icon" />
          <input
            type="text"
            placeholder="Cari judul atau penulis..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="search-input"
            aria-label="Cari buku"
          />
        </div>
        
        {/* Filter Buttons */}
        <div className="filter-buttons">
          {filters.map(filter => (
            <button
              key={filter.value}
              onClick={() => setFilterStatus(filter.value)}
              className={`filter-button ${filterStatus === filter.value ? 'active' : ''}`}
              aria-label={`Filter ${filter.label}`}
              aria-pressed={filterStatus === filter.value}
            >
              {filter.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default BookFilter;