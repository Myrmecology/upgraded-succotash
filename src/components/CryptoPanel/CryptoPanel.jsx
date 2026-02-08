import React, { useState, useEffect } from 'react';
import { getCryptoPrices } from '../../services/cryptoAPI';
import { formatCurrency, formatPercentChange, formatLargeNumber, getColorClass } from '../../utils/formatters';
import './CryptoPanel.css';

const CryptoPanel = () => {
  const [cryptos, setCryptos] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  // Default cryptos to track
  const DEFAULT_CRYPTOS = ['bitcoin', 'ethereum', 'cardano', 'solana', 'dogecoin'];

  // Fetch crypto prices
  useEffect(() => {
    const fetchCryptos = async () => {
      try {
        const data = await getCryptoPrices(DEFAULT_CRYPTOS);
        setCryptos(data);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching crypto prices:', error);
        setIsLoading(false);
      }
    };

    fetchCryptos();

    // Update every 30 seconds
    const interval = setInterval(fetchCryptos, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="crypto-panel section-container">
      <div className="section-header">
        <div>
          <h2 className="section-title">₿ Cryptocurrency</h2>
          <p className="section-subtitle">[ DIGITAL ASSETS • LIVE PRICES ]</p>
        </div>
      </div>

      {isLoading ? (
        <div className="loading-crypto">
          <div className="spinner"></div>
          <p>Loading crypto data...</p>
        </div>
      ) : cryptos.length === 0 ? (
        <div className="no-crypto">
          <div className="no-crypto-icon">🪙</div>
          <h4>No Crypto Data</h4>
          <p>Unable to load cryptocurrency prices</p>
        </div>
      ) : (
        <div className="crypto-grid">
          {cryptos.map((crypto) => {
            const colorClass = getColorClass(crypto.priceChange24h);

            return (
              <div key={crypto.id} className="crypto-card">
                {/* Crypto Header */}
                <div className="crypto-header">
                  {crypto.image && (
                    <img src={crypto.image} alt={crypto.name} className="crypto-icon" />
                  )}
                  <div className="crypto-info">
                    <h3 className="crypto-name">{crypto.name}</h3>
                    <span className="crypto-symbol">{crypto.symbol}</span>
                  </div>
                  <div className="crypto-rank">
                    #{crypto.marketCapRank}
                  </div>
                </div>

                {/* Crypto Price */}
                <div className="crypto-price">
                  <span className={`price-value ${colorClass}`}>
                    {formatCurrency(crypto.currentPrice)}
                  </span>
                </div>

                {/* Crypto Change */}
                <div className="crypto-change">
                  <span className={`change-value ${colorClass}`}>
                    {crypto.priceChange24h >= 0 ? '▲' : '▼'} {crypto.priceChange24h >= 0 ? '+' : ''}
                    {formatCurrency(Math.abs(crypto.priceChange24h))}
                  </span>
                  <span className={`change-percent ${colorClass}`}>
                    ({formatPercentChange(crypto.priceChangePercent24h / 100)})
                  </span>
                </div>

                {/* Crypto Stats */}
                <div className="crypto-stats">
                  <div className="stat-row">
                    <span className="stat-label">Market Cap:</span>
                    <span className="stat-value">{formatLargeNumber(crypto.marketCap)}</span>
                  </div>
                  <div className="stat-row">
                    <span className="stat-label">24h Volume:</span>
                    <span className="stat-value">{formatLargeNumber(crypto.volume24h)}</span>
                  </div>
                  <div className="stat-row">
                    <span className="stat-label">24h High:</span>
                    <span className="stat-value">{formatCurrency(crypto.high24h)}</span>
                  </div>
                  <div className="stat-row">
                    <span className="stat-label">24h Low:</span>
                    <span className="stat-value">{formatCurrency(crypto.low24h)}</span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default CryptoPanel;