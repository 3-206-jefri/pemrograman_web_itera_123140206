import React, { useState } from 'react';
import { Book, Home, BarChart3 } from 'lucide-react';
import { BookProvider } from './context/BookContext';
import HomePage from './pages/Home';
import StatsPage from './pages/Stats';
import './App.css';

function App() {
  const [currentPage, setCurrentPage] = useState('home');

  const navItems = [
    { id: 'home', label: 'Beranda', icon: Home },
    { id: 'stats', label: 'Statistik', icon: BarChart3 }
  ];

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <HomePage />;
      case 'stats':
        return <StatsPage />;
      default:
        return <HomePage />;
    }
  };

  return (
    <BookProvider>
      <div className="app-container">
        {/* Navigation Bar */}
        <nav className="navbar">
          <div className="navbar-container">
            <div className="navbar-content">
              {/* Logo */}
              <div className="logo-container">
                <Book className="logo-icon" />
                <span className="logo-text">MyBookshelf</span>
              </div>
              
              {/* Navigation Buttons */}
              <div className="nav-buttons">
                {navItems.map(item => {
                  const Icon = item.icon;
                  return (
                    <button
                      key={item.id}
                      onClick={() => setCurrentPage(item.id)}
                      className={`nav-button ${currentPage === item.id ? 'active' : ''}`}
                      aria-label={item.label}
                      aria-current={currentPage === item.id ? 'page' : undefined}
                    >
                      <Icon className="nav-button-icon" />
                      <span className="nav-button-text">{item.label}</span>
                    </button>
                  );
                })}
              </div>
            </div>
          </div>
        </nav>

        {/* Main Content */}
        <main className="main-content">
          {renderPage()}
        </main>

        {/* Footer */}
        <footer className="footer">
          <div className="footer-content">
            <p className="footer-text">
              © 2024 MyBookshelf - Kelola koleksi buku Anda dengan mudah
            </p>
          </div>
        </footer>
      </div>
    </BookProvider>
  );
}

export default App;