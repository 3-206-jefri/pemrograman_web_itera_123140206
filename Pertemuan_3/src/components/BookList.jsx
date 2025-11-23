import React, { useState } from 'react';
import { Book, BookOpen, ShoppingCart, Edit2, Trash2 } from 'lucide-react';
import { useBooks } from '../context/BookContext';
import BookForm from './BookForm';
import './BookList.css';

const BookList = () => {
  const { filteredBooks, deleteBook } = useBooks();
  const [editingBook, setEditingBook] = useState(null);

  const getStatusIcon = (status) => {
    switch (status) {
      case 'milik':
        return <Book className="status-icon owned" />;
      case 'baca':
        return <BookOpen className="status-icon reading" />;
      case 'beli':
        return <ShoppingCart className="status-icon wishlist" />;
      default:
        return null;
    }
  };

  const getStatusLabel = (status) => {
    switch (status) {
      case 'milik':
        return 'Dimiliki';
      case 'baca':
        return 'Sedang Dibaca';
      case 'beli':
        return 'Ingin Beli';
      default:
        return '';
    }
  };

  const handleDelete = (id, title) => {
    if (window.confirm(`Apakah Anda yakin ingin menghapus buku "${title}"?`)) {
      deleteBook(id);
    }
  };

  if (filteredBooks.length === 0) {
    return (
      <div className="empty-state">
        <Book className="empty-icon" />
        <p className="empty-title">Tidak ada buku ditemukan</p>
        <p className="empty-subtitle">
          Coba ubah filter atau kata kunci pencarian
        </p>
      </div>
    );
  }

  return (
    <>
      <div className="book-list-grid">
        {filteredBooks.map(book => (
          <div key={book.id} className="book-card">
            <div className="book-card-header">
              <div className="book-status">
                {getStatusIcon(book.status)}
                <span className="status-label">
                  {getStatusLabel(book.status)}
                </span>
              </div>
              
              <div className="book-actions">
                <button
                  onClick={() => setEditingBook(book)}
                  className="action-button edit"
                  title="Edit Buku"
                  aria-label={`Edit ${book.title}`}
                >
                  <Edit2 className="action-icon" />
                </button>
                <button
                  onClick={() => handleDelete(book.id, book.title)}
                  className="action-button delete"
                  title="Hapus Buku"
                  aria-label={`Hapus ${book.title}`}
                >
                  <Trash2 className="action-icon" />
                </button>
              </div>
            </div>
            
            <h3 className="book-title">{book.title}</h3>
            <p className="book-author">oleh {book.author}</p>
          </div>
        ))}
      </div>

      {editingBook && (
        <BookForm
          bookToEdit={editingBook}
          onClose={() => setEditingBook(null)}
        />
      )}
    </>
  );
};

export default BookList;