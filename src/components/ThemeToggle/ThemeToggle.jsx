import React from 'react';
import './ThemeToggle.css';

const ThemeToggle = ({ theme, toggleTheme }) => {
  return (
    <div className="theme-toggle-container">
      <button 
        className="theme-toggle-btn"
        onClick={toggleTheme}
        aria-label="Toggle theme"
      >
        <div className={`toggle-track ${theme}`}>
          <div className="toggle-icons">
            <span className="icon-sun">☀️</span>
            <span className="icon-moon">🌙</span>
          </div>
          <div className="toggle-thumb"></div>
        </div>
        <span className="toggle-label">
          {theme === 'dark' ? 'DARK MODE' : 'LIGHT MODE'}
        </span>
      </button>
    </div>
  );
};

export default ThemeToggle;