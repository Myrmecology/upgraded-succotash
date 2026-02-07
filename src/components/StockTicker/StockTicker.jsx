import React, { useState, useEffect } from 'react';
import { getMultipleQuotes } from '../../services/stockAPI';
import { formatCurrency, formatPercentChange, getColorClass } from '../../utils/formatters';
import './StockTicker.css';

const StockTicker = ({ watchlist }) => {
  const [quotes, setQuotes] = useState({});
  const [isLoading, setIsLoading] = useState(true);

  // Fetch stock quotes
  useEffect(() => {
    const fetchQuotes = async () => {
      if (!watchlist || watchlist.length === 0) return;
      
      try {
        const data = await getMultipleQuotes(watchlist);
        setQuotes(data);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching ticker quotes:', error);
      }
    };

    fetchQuotes();

    // Update every 15 seconds
    const interval = setInterval(fetchQuotes, 15000);

    return () => clearInterval(interval);
  }, [watchlist]);

  if (isLoading || !watchlist || watchlist.length === 0) {
    return (
      <div className="stock-ticker">
        <div className="ticker-content">
          <div className="ticker-item">
            <span className="ticker-symbol">LOADING...</span>
          </div>
        </div>
      </div>
    );
  }

  // Double the watchlist for seamless infinite scroll
  const tickerItems = [...watchlist, ...watchlist, ...watchlist];

  return (
    <div className="stock-ticker">
      <div className="ticker-label">
        <span className="ticker-live-dot"></span>
        LIVE MARKET
      </div>
      
      <div className="ticker-wrapper">
        <div className="ticker-content">
          {tickerItems.map((symbol, index) => {
            const quote = quotes[symbol];
            if (!quote) return null;

            const colorClass = getColorClass(quote.change);

            return (
              <div key={`${symbol}-${index}`} className="ticker-item">
                <span className="ticker-symbol">{symbol}</span>
                <span className={`ticker-price ${colorClass}`}>
                  {formatCurrency(quote.currentPrice)}
                </span>
                <span className={`ticker-change ${colorClass}`}>
                  {quote.change >= 0 ? '▲' : '▼'} {formatPercentChange(quote.changePercent / 100)}
                </span>
                <span className="ticker-separator">|</span>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default StockTicker;