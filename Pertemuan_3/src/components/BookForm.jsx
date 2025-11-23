import React, { useState } from 'react';
import { X } from 'lucide-react';
import { useBooks } from '../context/BookContext';
import './BookForm.css';

const BookForm = ({ bookToEdit, onClose }) => {
  const { addBook, updateBook } = useBooks();
  
  const [formData, setFormData] = useState({
    title: bookToEdit?.title || '',
    author: bookToEdit?.author || '',
    status: bookToEdit?.status || 'milik'
  });
  
  const [errors, setErrors] = useState({});

  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.title.trim()) {
      newErrors.title = 'Judul buku harus diisi';
    } else if (formData.title.length > 100) {
      newErrors.title = 'Judul maksimal 100 karakter';
    }
    
    if (!formData.author.trim()) {
      newErrors.author = 'Penulis harus diisi';
    } else if (formData.author.length > 50) {
      newErrors.author = 'Nama penulis maksimal 50 karakter';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }

    if (bookToEdit) {
      updateBook(bookToEdit.id, formData);
    } else {
      addBook(formData);
    }
    
    onClose();
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };

  return (
    <div className="modal-overlay">
      <div className="modal-container">
        {/* Header */}
        <div className="modal-header">
          <h2 className="modal-title">
            {bookToEdit ? 'Edit Buku' : 'Tambah Buku Baru'}
          </h2>
          <button 
            onClick={onClose} 
            className="close-button"
            aria-label="Tutup"
          >
            <X className="close-icon" />
          </button>
        </div>

        {/* Form */}
        <div className="form-content">
          {/* Title Input */}
          <div className="form-group">
            <label className="form-label">
              Judul Buku <span className="required">*</span>
            </label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleChange}
              className={`form-input ${errors.title ? 'error' : ''}`}
              placeholder="Masukkan judul buku"
            />
            {errors.title && (
              <p className="error-message">{errors.title}</p>
            )}
          </div>

          {/* Author Input */}
          <div className="form-group">
            <label className="form-label">
              Penulis <span className="required">*</span>
            </label>
            <input
              type="text"
              name="author"
              value={formData.author}
              onChange={handleChange}
              className={`form-input ${errors.author ? 'error' : ''}`}
              placeholder="Masukkan nama penulis"
            />
            {errors.author && (
              <p className="error-message">{errors.author}</p>
            )}
          </div>

          {/* Status Select */}
          <div className="form-group">
            <label className="form-label">
              Status <span className="required">*</span>
            </label>
            <select
              name="status"
              value={formData.status}
              onChange={handleChange}
              className="form-select"
            >
              <option value="milik">Dimiliki</option>
              <option value="baca">Sedang Dibaca</option>
              <option value="beli">Ingin Beli</option>
            </select>
          </div>

          {/* Action Buttons */}
          <div className="form-actions">
            <button
              type="button"
              onClick={onClose}
              className="btn btn-cancel"
            >
              Batal
            </button>
            <button
              type="button"
              onClick={handleSubmit}
              className="btn btn-submit"
            >
              {bookToEdit ? 'Update' : 'Tambah'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BookForm;