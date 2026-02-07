import React, { useState, useEffect } from 'react';
import { getStockQuote } from '../../services/stockAPI';
import { formatCurrency, formatPercentChange, getColorClass } from '../../utils/formatters';
import { validateBuyTransaction, validateSellTransaction } from '../../utils/calculations';
import './Dashboard.css';

const Dashboard = ({ portfolio, selectedStock, buyStock, sellStock }) => {
  const [quote, setQuote] = useState(null);
  const [quantity, setQuantity] = useState(1);
  const [isLoading, setIsLoading] = useState(false);
  const [transactionType, setTransactionType] = useState('buy'); // 'buy' or 'sell'
  const [message, setMessage] = useState({ text: '', type: '' });

  // Fetch quote for selected stock
  useEffect(() => {
    if (selectedStock) {
      fetchQuote();
      
      // Update every 10 seconds
      const interval = setInterval(fetchQuote, 10000);
      return () => clearInterval(interval);
    }
  }, [selectedStock]);

  const fetchQuote = async () => {
    if (!selectedStock) return;
    
    setIsLoading(true);
    try {
      const data = await getStockQuote(selectedStock);
      setQuote(data);
    } catch (error) {
      console.error('Error fetching quote:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleBuy = () => {
    if (!quote) return;

    const validation = validateBuyTransaction(quantity, quote.currentPrice, portfolio.cash);
    
    if (!validation.valid) {
      setMessage({ text: validation.message, type: 'error' });
      setTimeout(() => setMessage({ text: '', type: '' }), 3000);
      return;
    }

    const success = buyStock(selectedStock, quantity, quote.currentPrice);
    
    if (success) {
      setMessage({ 
        text: `✓ Bought ${quantity} shares of ${selectedStock} at ${formatCurrency(quote.currentPrice)}`, 
        type: 'success' 
      });
      setQuantity(1);
      setTimeout(() => setMessage({ text: '', type: '' }), 5000);
    }
  };

  const handleSell = () => {
    if (!quote) return;

    const holding = portfolio.holdings.find(h => h.symbol === selectedStock);
    const validation = validateSellTransaction(quantity, holding);
    
    if (!validation.valid) {
      setMessage({ text: validation.message, type: 'error' });
      setTimeout(() => setMessage({ text: '', type: '' }), 3000);
      return;
    }

    const success = sellStock(selectedStock, quantity, quote.currentPrice);
    
    if (success) {
      setMessage({ 
        text: `✓ Sold ${quantity} shares of ${selectedStock} at ${formatCurrency(quote.currentPrice)}`, 
        type: 'success' 
      });
      setQuantity(1);
      setTimeout(() => setMessage({ text: '', type: '' }), 5000);
    }
  };

  const currentHolding = portfolio.holdings.find(h => h.symbol === selectedStock);

  return (
    <div className="dashboard section-container">
      <div className="section-header">
        <div>
          <h2 className="section-title">⚡ Trading Terminal</h2>
          <p className="section-subtitle">[ BUY • SELL • TRADE ]</p>
        </div>
        <div className="cash-display">
          <span className="cash-label">Available Cash:</span>
          <span className="cash-amount">{formatCurrency(portfolio.cash)}</span>
        </div>
      </div>

      {!selectedStock ? (
        <div className="no-stock-selected">
          <div className="no-stock-icon">📊</div>
          <h3>No Stock Selected</h3>
          <p>Search for a stock above to start trading</p>
          <div className="quick-picks">
            <p className="quick-picks-label">Quick Picks:</p>
            <div className="quick-picks-buttons">
              {/* These could be clickable in a real implementation */}
              <span className="quick-pick-badge">AAPL</span>
              <span className="quick-pick-badge">GOOGL</span>
              <span className="quick-pick-badge">TSLA</span>
              <span className="quick-pick-badge">MSFT</span>
              <span className="quick-pick-badge">AMZN</span>
            </div>
          </div>
        </div>
      ) : (
        <div className="trading-interface">
          {isLoading ? (
            <div className="loading-quote">
              <div className="spinner"></div>
              <p>Loading quote data...</p>
            </div>
          ) : quote ? (
            <>
              {/* Stock Quote Display */}
              <div className="quote-display">
                <div className="quote-header">
                  <h3 className="quote-symbol">{quote.symbol}</h3>
                  <div className={`quote-price ${getColorClass(quote.change)}`}>
                    {formatCurrency(quote.currentPrice)}
                  </div>
                </div>
                <div className="quote-details">
                  <div className="quote-stat">
                    <span className="stat-label">Change:</span>
                    <span className={`stat-value ${getColorClass(quote.change)}`}>
                      {quote.change >= 0 ? '▲' : '▼'} {formatCurrency(Math.abs(quote.change))} ({formatPercentChange(quote.changePercent / 100)})
                    </span>
                  </div>
                  <div className="quote-stat">
                    <span className="stat-label">High:</span>
                    <span className="stat-value">{formatCurrency(quote.high)}</span>
                  </div>
                  <div className="quote-stat">
                    <span className="stat-label">Low:</span>
                    <span className="stat-value">{formatCurrency(quote.low)}</span>
                  </div>
                  <div className="quote-stat">
                    <span className="stat-label">Open:</span>
                    <span className="stat-value">{formatCurrency(quote.open)}</span>
                  </div>
                </div>

                {currentHolding && (
                  <div className="current-position">
                    <h4>Your Position:</h4>
                    <div className="position-details">
                      <span>Shares: <strong>{currentHolding.quantity}</strong></span>
                      <span>Avg Cost: <strong>{formatCurrency(currentHolding.averageCost)}</strong></span>
                    </div>
                  </div>
                )}
              </div>

              {/* Transaction Type Toggle */}
              <div className="transaction-toggle">
                <button
                  className={`toggle-btn ${transactionType === 'buy' ? 'active buy' : ''}`}
                  onClick={() => setTransactionType('buy')}
                >
                  BUY
                </button>
                <button
                  className={`toggle-btn ${transactionType === 'sell' ? 'active sell' : ''}`}
                  onClick={() => setTransactionType('sell')}
                >
                  SELL
                </button>
              </div>

              {/* Quantity Input */}
              <div className="quantity-input-wrapper">
                <label className="input-label">Quantity (Shares)</label>
                <input
                  type="number"
                  min="1"
                  value={quantity}
                  onChange={(e) => setQuantity(parseInt(e.target.value) || 1)}
                  className="quantity-input"
                />
              </div>

              {/* Transaction Summary */}
              <div className="transaction-summary">
                <div className="summary-row">
                  <span>Price per Share:</span>
                  <span className="summary-value">{formatCurrency(quote.currentPrice)}</span>
                </div>
                <div className="summary-row">
                  <span>Quantity:</span>
                  <span className="summary-value">{quantity}</span>
                </div>
                <div className="summary-row total">
                  <span>Total {transactionType === 'buy' ? 'Cost' : 'Revenue'}:</span>
                  <span className="summary-value">{formatCurrency(quote.currentPrice * quantity)}</span>
                </div>
              </div>

              {/* Execute Button */}
              <button
                className={`btn-execute btn-${transactionType}`}
                onClick={transactionType === 'buy' ? handleBuy : handleSell}
              >
                {transactionType === 'buy' ? '🚀 EXECUTE BUY ORDER' : '💰 EXECUTE SELL ORDER'}
              </button>

              {/* Message Display */}
              {message.text && (
                <div className={`transaction-message ${message.type}`}>
                  {message.text}
                </div>
              )}
            </>
          ) : (
            <div className="error-message">
              <p>⚠️ Unable to load quote data</p>
              <button className="btn-retry" onClick={fetchQuote}>Retry</button>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default Dashboard;