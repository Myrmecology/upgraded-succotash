import React, { useState, useEffect } from 'react';
import './styles/variables.css';
import './styles/animations.css';
import './styles/themes.css';
import './styles/App.css';

// Components
import StockTicker from './components/StockTicker/StockTicker';
import Dashboard from './components/Dashboard/Dashboard';
import Portfolio from './components/Portfolio/Portfolio';
import Watchlist from './components/Watchlist/Watchlist';
import StockSearch from './components/StockSearch/StockSearch';
import NewsPanel from './components/NewsPanel/NewsPanel';
import ThemeToggle from './components/ThemeToggle/ThemeToggle';
import HistoricalData from './components/HistoricalData/HistoricalData';
import CompanyInfo from './components/CompanyInfo/CompanyInfo';
import CryptoPanel from './components/CryptoPanel/CryptoPanel';

// Utilities
import { loadPortfolio, savePortfolio } from './utils/localStorage';

function App() {
  // Theme state
  const [theme, setTheme] = useState('dark');
  
  // Portfolio state
  const [portfolio, setPortfolio] = useState({
    cash: 100000, // Starting virtual cash
    holdings: [],
    totalValue: 100000,
    totalGainLoss: 0,
    totalGainLossPercent: 0
  });
  
  // Watchlist state
  const [watchlist, setWatchlist] = useState([
    'AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN'
  ]);
  
  // Selected stock for detailed view
  const [selectedStock, setSelectedStock] = useState(null);
  
  // Load saved data on mount
  useEffect(() => {
    // Load theme preference
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    // Load portfolio
    const savedPortfolio = loadPortfolio();
    if (savedPortfolio) {
      setPortfolio(savedPortfolio);
    }
    
    // Load watchlist
    const savedWatchlist = localStorage.getItem('watchlist');
    if (savedWatchlist) {
      setWatchlist(JSON.parse(savedWatchlist));
    }
    
    // Remove preload class to enable transitions
    document.body.classList.remove('preload');
  }, []);
  
  // Save portfolio whenever it changes
  useEffect(() => {
    savePortfolio(portfolio);
  }, [portfolio]);
  
  // Save watchlist whenever it changes
  useEffect(() => {
    localStorage.setItem('watchlist', JSON.stringify(watchlist));
  }, [watchlist]);
  
  // Toggle theme
  const toggleTheme = () => {
    const newTheme = theme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  };
  
  // Buy stock
  const buyStock = (symbol, quantity, price) => {
    const totalCost = quantity * price;
    
    if (totalCost > portfolio.cash) {
      alert('Insufficient funds!');
      return false;
    }
    
    const existingHolding = portfolio.holdings.find(h => h.symbol === symbol);
    
    let newHoldings;
    if (existingHolding) {
      // Add to existing position
      newHoldings = portfolio.holdings.map(h => {
        if (h.symbol === symbol) {
          const newQuantity = h.quantity + quantity;
          const newAverageCost = ((h.averageCost * h.quantity) + totalCost) / newQuantity;
          return {
            ...h,
            quantity: newQuantity,
            averageCost: newAverageCost
          };
        }
        return h;
      });
    } else {
      // Create new position
      newHoldings = [
        ...portfolio.holdings,
        {
          symbol,
          quantity,
          averageCost: price,
          purchaseDate: new Date().toISOString()
        }
      ];
    }
    
    setPortfolio({
      ...portfolio,
      cash: portfolio.cash - totalCost,
      holdings: newHoldings
    });
    
    return true;
  };
  
  // Sell stock
  const sellStock = (symbol, quantity, price) => {
    const holding = portfolio.holdings.find(h => h.symbol === symbol);
    
    if (!holding || holding.quantity < quantity) {
      alert('Insufficient shares!');
      return false;
    }
    
    const totalRevenue = quantity * price;
    
    let newHoldings;
    if (holding.quantity === quantity) {
      // Remove position entirely
      newHoldings = portfolio.holdings.filter(h => h.symbol !== symbol);
    } else {
      // Reduce position
      newHoldings = portfolio.holdings.map(h => {
        if (h.symbol === symbol) {
          return {
            ...h,
            quantity: h.quantity - quantity
          };
        }
        return h;
      });
    }
    
    setPortfolio({
      ...portfolio,
      cash: portfolio.cash + totalRevenue,
      holdings: newHoldings
    });
    
    return true;
  };
  
  // Add to watchlist
  const addToWatchlist = (symbol) => {
    if (!watchlist.includes(symbol.toUpperCase())) {
      setWatchlist([...watchlist, symbol.toUpperCase()]);
    }
  };
  
  // Remove from watchlist
  const removeFromWatchlist = (symbol) => {
    setWatchlist(watchlist.filter(s => s !== symbol));
  };

  return (
    <div className="App">
      {/* Sticky Stock Ticker at Top */}
      <div className="app-header">
        <StockTicker watchlist={watchlist} />
      </div>
      
      {/* Main Content */}
      <div className="app-container">
        <header className="header-content">
          <div className="app-logo">
            <span className="app-logo-icon">📈</span>
            <h1>MARKET TERMINAL</h1>
          </div>
          
          <div className="header-controls">
            <ThemeToggle theme={theme} toggleTheme={toggleTheme} />
          </div>
        </header>
        
        <main className="app-main">
          <div className="dashboard-grid">
            {/* Search Bar */}
            <StockSearch 
              onSelectStock={setSelectedStock}
              addToWatchlist={addToWatchlist}
            />
            
            {/* Main Dashboard */}
            <Dashboard 
              portfolio={portfolio}
              selectedStock={selectedStock}
              buyStock={buyStock}
              sellStock={sellStock}
            />
            
            {/* Portfolio Overview */}
            <Portfolio 
              portfolio={portfolio}
              selectedStock={selectedStock}
            />
            
            {/* Watchlist */}
            <Watchlist 
              watchlist={watchlist}
              removeFromWatchlist={removeFromWatchlist}
              onSelectStock={setSelectedStock}
            />
            
            {/* Company Info (if stock selected) */}
            {selectedStock && (
              <CompanyInfo symbol={selectedStock} />
            )}
            
            {/* Historical Data (if stock selected) */}
            {selectedStock && (
              <HistoricalData symbol={selectedStock} />
            )}
            
            {/* News Panel */}
            <NewsPanel selectedStock={selectedStock} />
            
            {/* Crypto Panel */}
            <CryptoPanel />
          </div>
        </main>
      </div>
    </div>
  );
}

export default App;