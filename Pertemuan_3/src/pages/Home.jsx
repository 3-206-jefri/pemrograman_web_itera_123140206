import React, { useState } from 'react';
import { Plus } from 'lucide-react';
import BookFilter from '../components/BookFilter';
import BookList from '../components/BookList';
import BookForm from '../components/BookForm';
import './Home.css';

const Home = () => {
  const [showForm, setShowForm] = useState(false);

  return (
    <div>
      {/* Header Section */}
      <div className="home-header">
        <h1 className="home-title">Koleksi Buku Saya</h1>
        
        <button
          onClick={() => setShowForm(true)}
          className="add-book-button"
        >
          <Plus className="add-icon" />
          Tambah Buku
        </button>
      </div>

      {/* Filter Component */}
      <BookFilter />
      
      {/* Book List Component */}
      <BookList />

      {/* Modal Form Tambah Buku */}
      {showForm && (
        <BookForm onClose={() => setShowForm(false)} />
      )}
    </div>
  );
};

export default Home;