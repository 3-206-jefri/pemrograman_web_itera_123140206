import React from 'react';
import { Book, Check, BookOpen, ShoppingCart } from 'lucide-react';
import { useBooks } from '../context/BookContext';
import useBookStats from '../hooks/useBookStats';
import './Stats.css';

const Stats = () => {
  const { books } = useBooks();
  const stats = useBookStats(books);

  const statsData = [
    { 
      label: 'Total Buku', 
      value: stats.total, 
      icon: Book, 
      colorClass: 'purple'
    },
    { 
      label: 'Dimiliki', 
      value: stats.owned, 
      icon: Check, 
      colorClass: 'green'
    },
    { 
      label: 'Sedang Dibaca', 
      value: stats.reading, 
      icon: BookOpen, 
      colorClass: 'blue'
    },
    { 
      label: 'Ingin Beli', 
      value: stats.wishlist, 
      icon: ShoppingCart, 
      colorClass: 'orange'
    }
  ];

  const getStatusBadge = (status) => {
    const badges = {
      milik: 'owned',
      baca: 'reading',
      beli: 'wishlist'
    };
    return badges[status] || '';
  };

  const getStatusLabel = (status) => {
    const labels = {
      milik: 'Dimiliki',
      baca: 'Sedang Dibaca',
      beli: 'Ingin Beli'
    };
    return labels[status] || status;
  };

  return (
    <div>
      <h1 className="stats-title">Statistik Buku</h1>
      
      {/* Stats Cards */}
      <div className="stats-grid">
        {statsData.map((stat, index) => {
          const Icon = stat.icon;
          return (
            <div key={index} className="stats-card">
              <div className="stats-card-header">
                <div className={`stats-icon-container ${stat.colorClass}`}>
                  <Icon className="stats-icon" />
                </div>
              </div>
              <p className="stats-label">{stat.label}</p>
              <p className="stats-value">{stat.value}</p>
            </div>
          );
        })}
      </div>

      {/* Table Section */}
      {books.length > 0 ? (
        <div className="table-section">
          <h2 className="table-title">Daftar Lengkap Buku</h2>
          
          <div className="table-container">
            <table className="books-table">
              <thead>
                <tr>
                  <th>No</th>
                  <th>Judul</th>
                  <th>Penulis</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {books.map((book, index) => (
                  <tr key={book.id}>
                    <td className="table-number">{index + 1}</td>
                    <td className="table-title-cell">{book.title}</td>
                    <td className="table-author">{book.author}</td>
                    <td>
                      <span className={`status-badge ${getStatusBadge(book.status)}`}>
                        {getStatusLabel(book.status)}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      ) : (
        <div className="stats-empty-state">
          <Book className="stats-empty-icon" />
          <p className="stats-empty-title">Belum ada buku</p>
          <p className="stats-empty-subtitle">
            Tambahkan buku pertama Anda untuk melihat statistik
          </p>
        </div>
      )}
    </div>
  );
};

export default Stats;