import React, { useState, useRef, useEffect } from 'react';
import { searchStocks } from '../../services/stockAPI';
import './StockSearch.css';

const StockSearch = ({ onSelectStock, addToWatchlist }) => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isSearching, setIsSearching] = useState(false);
  const [showResults, setShowResults] = useState(false);
  const searchRef = useRef(null);

  // Handle click outside to close results
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (searchRef.current && !searchRef.current.contains(event.target)) {
        setShowResults(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Search with debounce
  useEffect(() => {
    const delayTimer = setTimeout(() => {
      if (query.length >= 1) {
        handleSearch();
      } else {
        setResults([]);
        setShowResults(false);
      }
    }, 500);

    return () => clearTimeout(delayTimer);
  }, [query]);

  const handleSearch = async () => {
    if (query.trim() === '') return;

    setIsSearching(true);

    try {
      const searchResults = await searchStocks(query);
      setResults(searchResults);
      setShowResults(true);
    } catch (error) {
      console.error('Error searching stocks:', error);
      setResults([]);
    } finally {
      setIsSearching(false);
    }
  };

  const handleSelectStock = (symbol) => {
    onSelectStock(symbol);
    setQuery('');
    setResults([]);
    setShowResults(false);
  };

  const handleAddToWatchlist = (symbol, event) => {
    event.stopPropagation();
    addToWatchlist(symbol);
    
    // Visual feedback
    const button = event.currentTarget;
    button.textContent = '✓ Added';
    button.style.background = 'var(--neon-green)';
    
    setTimeout(() => {
      button.textContent = '+ Watch';
      button.style.background = '';
    }, 2000);
  };

  return (
    <div className="stock-search section-container" ref={searchRef}>
      <div className="section-header">
        <div>
          <h2 className="section-title">🔍 Stock Search</h2>
          <p className="section-subtitle">[ SEARCH GLOBAL MARKETS ]</p>
        </div>
      </div>

      <div className="search-input-wrapper">
        <input
          type="text"
          className="search-input"
          placeholder="Enter stock symbol or company name..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onFocus={() => query.length >= 1 && setShowResults(true)}
        />
        <div className="search-icon">
          {isSearching ? (
            <div className="search-spinner"></div>
          ) : (
            <span>🔍</span>
          )}
        </div>
      </div>

      {showResults && results.length > 0 && (
        <div className="search-results">
          {results.map((stock, index) => (
            <div
              key={`${stock.symbol}-${index}`}
              className="search-result-item"
              onClick={() => handleSelectStock(stock.symbol)}
            >
              <div className="result-info">
                <span className="result-symbol">{stock.symbol}</span>
                <span className="result-name">{stock.name}</span>
                <span className="result-meta">
                  {stock.type} • {stock.region}
                </span>
              </div>
              <button
                className="btn-add-watch btn-small"
                onClick={(e) => handleAddToWatchlist(stock.symbol, e)}
              >
                + Watch
              </button>
            </div>
          ))}
        </div>
      )}

      {showResults && results.length === 0 && !isSearching && query.length >= 1 && (
        <div className="search-no-results">
          <span className="no-results-icon">🚫</span>
          <p>No stocks found for "{query}"</p>
          <p className="no-results-hint">Try a different symbol or company name</p>
        </div>
      )}
    </div>
  );
};

export default StockSearch;