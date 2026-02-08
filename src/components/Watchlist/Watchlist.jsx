import React, { useState, useEffect } from 'react';
import { getMultipleQuotes } from '../../services/stockAPI';
import { formatCurrency, formatPercentChange, getColorClass } from '../../utils/formatters';
import './Watchlist.css';

const Watchlist = ({ watchlist, removeFromWatchlist, onSelectStock }) => {
  const [quotes, setQuotes] = useState({});
  const [isLoading, setIsLoading] = useState(true);

  // Fetch quotes for watchlist
  useEffect(() => {
    const fetchQuotes = async () => {
      if (!watchlist || watchlist.length === 0) {
        setIsLoading(false);
        return;
      }

      try {
        const data = await getMultipleQuotes(watchlist);
        setQuotes(data);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching watchlist quotes:', error);
        setIsLoading(false);
      }
    };

    fetchQuotes();

    // Update every 10 seconds
    const interval = setInterval(fetchQuotes, 10000);
    return () => clearInterval(interval);
  }, [watchlist]);

  const handleRemove = (symbol, event) => {
    event.stopPropagation();
    removeFromWatchlist(symbol);
  };

  const handleSelectStock = (symbol) => {
    onSelectStock(symbol);
  };

  return (
    <div className="watchlist section-container">
      <div className="section-header">
        <div>
          <h2 className="section-title">👁️ Watchlist</h2>
          <p className="section-subtitle">[ MONITOR • TRACK • ANALYZE ]</p>
        </div>
        <div className="watchlist-count">
          <span className="count-number">{watchlist.length}</span>
          <span className="count-label">Stocks</span>
        </div>
      </div>

      {isLoading ? (
        <div className="loading-watchlist">
          <div className="spinner"></div>
          <p>Loading watchlist...</p>
        </div>
      ) : watchlist.length === 0 ? (
        <div className="no-watchlist">
          <div className="no-watchlist-icon">👀</div>
          <h4>Watchlist Empty</h4>
          <p>Search for stocks and add them to your watchlist</p>
        </div>
      ) : (
        <div className="watchlist-grid">
          {watchlist.map((symbol) => {
            const quote = quotes[symbol];
            if (!quote) return null;

            const colorClass = getColorClass(quote.change);

            return (
              <div
                key={symbol}
                className="watchlist-card"
                onClick={() => handleSelectStock(symbol)}
              >
                <button
                  className="btn-remove"
                  onClick={(e) => handleRemove(symbol, e)}
                  aria-label="Remove from watchlist"
                >
                  ✕
                </button>

                <div className="card-header">
                  <h3 className="card-symbol">{symbol}</h3>
                  <span className={`card-indicator ${colorClass}`}>
                    {quote.change >= 0 ? '▲' : '▼'}
                  </span>
                </div>

                <div className="card-price">
                  <span className={`price-value ${colorClass}`}>
                    {formatCurrency(quote.currentPrice)}
                  </span>
                </div>

                <div className="card-change">
                  <span className={`change-value ${colorClass}`}>
                    {quote.change >= 0 ? '+' : ''}{formatCurrency(quote.change)}
                  </span>
                  <span className={`change-percent ${colorClass}`}>
                    ({formatPercentChange(quote.changePercent / 100)})
                  </span>
                </div>

                <div className="card-stats">
                  <div className="stat-item">
                    <span className="stat-label">High</span>
                    <span className="stat-value">{formatCurrency(quote.high)}</span>
                  </div>
                  <div className="stat-item">
                    <span className="stat-label">Low</span>
                    <span className="stat-value">{formatCurrency(quote.low)}</span>
                  </div>
                </div>

                <div className="card-footer">
                  <span className="footer-text">Click to trade</span>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default Watchlist;