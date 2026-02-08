import React, { useState, useEffect } from 'react';
import { getMultipleQuotes } from '../../services/stockAPI';
import { 
  calculateHoldingGainLoss, 
  calculatePortfolioValue,
  calculatePortfolioAllocation 
} from '../../utils/calculations';
import { 
  formatCurrency, 
  formatPercent, 
  formatPercentChange, 
  getColorClass,
  getBadgeClass 
} from '../../utils/formatters';
import PieChart from '../Charts/PieChart';
import './Portfolio.css';

const Portfolio = ({ portfolio, selectedStock }) => {
  const [currentPrices, setCurrentPrices] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  const [portfolioValue, setPortfolioValue] = useState(portfolio.totalValue);
  const [totalGainLoss, setTotalGainLoss] = useState(0);
  const [totalGainLossPercent, setTotalGainLossPercent] = useState(0);

  // Fetch current prices for all holdings
  useEffect(() => {
    const fetchPrices = async () => {
      if (!portfolio.holdings || portfolio.holdings.length === 0) {
        setIsLoading(false);
        return;
      }

      try {
        const symbols = portfolio.holdings.map(h => h.symbol);
        const quotes = await getMultipleQuotes(symbols);
        
        const prices = {};
        Object.values(quotes).forEach(quote => {
          prices[quote.symbol] = quote.currentPrice;
        });
        
        setCurrentPrices(prices);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching portfolio prices:', error);
        setIsLoading(false);
      }
    };

    fetchPrices();

    // Update every 15 seconds
    const interval = setInterval(fetchPrices, 15000);
    return () => clearInterval(interval);
  }, [portfolio.holdings]);

  // Calculate portfolio metrics
  useEffect(() => {
    if (Object.keys(currentPrices).length > 0) {
      const totalValue = calculatePortfolioValue(portfolio.holdings, currentPrices, portfolio.cash);
      setPortfolioValue(totalValue);

      // Calculate total gain/loss
      let totalCost = 0;
      let totalCurrentValue = 0;

      portfolio.holdings.forEach(holding => {
        const currentPrice = currentPrices[holding.symbol] || 0;
        const { costBasis, currentValue } = calculateHoldingGainLoss(holding, currentPrice);
        totalCost += costBasis;
        totalCurrentValue += currentValue;
      });

      const gainLoss = totalCurrentValue - totalCost;
      const gainLossPercent = totalCost > 0 ? gainLoss / totalCost : 0;

      setTotalGainLoss(gainLoss);
      setTotalGainLossPercent(gainLossPercent);
    }
  }, [currentPrices, portfolio.holdings, portfolio.cash]);

  // Calculate allocation for pie chart
  const allocation = calculatePortfolioAllocation(portfolio.holdings, currentPrices);

  return (
    <div className="portfolio section-container">
      <div className="section-header">
        <div>
          <h2 className="section-title">💼 Portfolio Overview</h2>
          <p className="section-subtitle">[ HOLDINGS • PERFORMANCE • ALLOCATION ]</p>
        </div>
      </div>

      {/* Portfolio Summary */}
      <div className="portfolio-summary">
        <div className="summary-card">
          <span className="summary-label">Total Value</span>
          <span className="summary-value primary">{formatCurrency(portfolioValue)}</span>
        </div>
        <div className="summary-card">
          <span className="summary-label">Cash Available</span>
          <span className="summary-value success">{formatCurrency(portfolio.cash)}</span>
        </div>
        <div className="summary-card">
          <span className="summary-label">Total Gain/Loss</span>
          <span className={`summary-value ${getColorClass(totalGainLoss)}`}>
            {totalGainLoss >= 0 ? '+' : ''}{formatCurrency(totalGainLoss)}
          </span>
          <span className={`summary-percent ${getColorClass(totalGainLoss)}`}>
            {formatPercentChange(totalGainLossPercent)}
          </span>
        </div>
        <div className="summary-card">
          <span className="summary-label">Holdings</span>
          <span className="summary-value neutral">{portfolio.holdings.length}</span>
        </div>
      </div>

      {/* Portfolio Allocation Chart */}
      {allocation.length > 0 && (
        <div className="allocation-section">
          <h3 className="subsection-title">Portfolio Allocation</h3>
          <PieChart data={allocation} />
        </div>
      )}

      {/* Holdings Table */}
      <div className="holdings-section">
        <h3 className="subsection-title">Current Holdings</h3>
        
        {isLoading ? (
          <div className="loading-holdings">
            <div className="spinner"></div>
            <p>Loading holdings...</p>
          </div>
        ) : portfolio.holdings.length === 0 ? (
          <div className="no-holdings">
            <div className="no-holdings-icon">📭</div>
            <h4>No Holdings Yet</h4>
            <p>Start trading to build your portfolio</p>
          </div>
        ) : (
          <div className="holdings-table">
            <div className="table-header">
              <div className="table-cell">Symbol</div>
              <div className="table-cell">Shares</div>
              <div className="table-cell">Avg Cost</div>
              <div className="table-cell">Current Price</div>
              <div className="table-cell">Value</div>
              <div className="table-cell">Gain/Loss</div>
              <div className="table-cell">%</div>
            </div>
            {portfolio.holdings.map((holding, index) => {
              const currentPrice = currentPrices[holding.symbol] || 0;
              const { gainLoss, gainLossPercent, currentValue } = calculateHoldingGainLoss(holding, currentPrice);
              const isSelected = holding.symbol === selectedStock;

              return (
                <div 
                  key={`${holding.symbol}-${index}`} 
                  className={`table-row ${isSelected ? 'selected' : ''}`}
                >
                  <div className="table-cell symbol-cell">
                    <span className="holding-symbol">{holding.symbol}</span>
                  </div>
                  <div className="table-cell">{holding.quantity}</div>
                  <div className="table-cell">{formatCurrency(holding.averageCost)}</div>
                  <div className="table-cell">
                    {currentPrice > 0 ? formatCurrency(currentPrice) : 'Loading...'}
                  </div>
                  <div className="table-cell">{formatCurrency(currentValue)}</div>
                  <div className={`table-cell ${getColorClass(gainLoss)}`}>
                    {gainLoss >= 0 ? '+' : ''}{formatCurrency(gainLoss)}
                  </div>
                  <div className="table-cell">
                    <span className={`badge ${getBadgeClass(gainLoss)}`}>
                      {gainLoss >= 0 ? '▲' : '▼'} {formatPercent(Math.abs(gainLossPercent))}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
};

export default Portfolio;