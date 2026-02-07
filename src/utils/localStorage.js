/* ============================================
   LOCAL STORAGE UTILITIES
   Save and load portfolio data
   ============================================ */

const PORTFOLIO_KEY = 'stock_dashboard_portfolio';
const WATCHLIST_KEY = 'stock_dashboard_watchlist';
const SETTINGS_KEY = 'stock_dashboard_settings';

/**
 * Load portfolio from localStorage
 * @returns {Object|null} Portfolio object or null if not found
 */
export const loadPortfolio = () => {
  try {
    const savedData = localStorage.getItem(PORTFOLIO_KEY);
    if (savedData) {
      return JSON.parse(savedData);
    }
    return null;
  } catch (error) {
    console.error('Error loading portfolio from localStorage:', error);
    return null;
  }
};

/**
 * Save portfolio to localStorage
 * @param {Object} portfolio - Portfolio object to save
 */
export const savePortfolio = (portfolio) => {
  try {
    localStorage.setItem(PORTFOLIO_KEY, JSON.stringify(portfolio));
  } catch (error) {
    console.error('Error saving portfolio to localStorage:', error);
  }
};

/**
 * Clear portfolio data
 */
export const clearPortfolio = () => {
  try {
    localStorage.removeItem(PORTFOLIO_KEY);
  } catch (error) {
    console.error('Error clearing portfolio from localStorage:', error);
  }
};

/**
 * Load watchlist from localStorage
 * @returns {Array|null} Array of stock symbols or null if not found
 */
export const loadWatchlist = () => {
  try {
    const savedData = localStorage.getItem(WATCHLIST_KEY);
    if (savedData) {
      return JSON.parse(savedData);
    }
    return null;
  } catch (error) {
    console.error('Error loading watchlist from localStorage:', error);
    return null;
  }
};

/**
 * Save watchlist to localStorage
 * @param {Array} watchlist - Array of stock symbols
 */
export const saveWatchlist = (watchlist) => {
  try {
    localStorage.setItem(WATCHLIST_KEY, JSON.stringify(watchlist));
  } catch (error) {
    console.error('Error saving watchlist to localStorage:', error);
  }
};

/**
 * Load user settings from localStorage
 * @returns {Object|null} Settings object or null if not found
 */
export const loadSettings = () => {
  try {
    const savedData = localStorage.getItem(SETTINGS_KEY);
    if (savedData) {
      return JSON.parse(savedData);
    }
    return null;
  } catch (error) {
    console.error('Error loading settings from localStorage:', error);
    return null;
  }
};

/**
 * Save user settings to localStorage
 * @param {Object} settings - Settings object to save
 */
export const saveSettings = (settings) => {
  try {
    localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
  } catch (error) {
    console.error('Error saving settings to localStorage:', error);
  }
};

/**
 * Clear all app data from localStorage
 */
export const clearAllData = () => {
  try {
    localStorage.removeItem(PORTFOLIO_KEY);
    localStorage.removeItem(WATCHLIST_KEY);
    localStorage.removeItem(SETTINGS_KEY);
  } catch (error) {
    console.error('Error clearing all data from localStorage:', error);
  }
};

/**
 * Export portfolio data as JSON for backup
 * @returns {string} JSON string of portfolio data
 */
export const exportPortfolioData = () => {
  try {
    const portfolio = loadPortfolio();
    const watchlist = loadWatchlist();
    const settings = loadSettings();
    
    const exportData = {
      portfolio,
      watchlist,
      settings,
      exportDate: new Date().toISOString()
    };
    
    return JSON.stringify(exportData, null, 2);
  } catch (error) {
    console.error('Error exporting portfolio data:', error);
    return null;
  }
};

/**
 * Import portfolio data from JSON backup
 * @param {string} jsonData - JSON string to import
 * @returns {boolean} Success status
 */
export const importPortfolioData = (jsonData) => {
  try {
    const importData = JSON.parse(jsonData);
    
    if (importData.portfolio) {
      savePortfolio(importData.portfolio);
    }
    if (importData.watchlist) {
      saveWatchlist(importData.watchlist);
    }
    if (importData.settings) {
      saveSettings(importData.settings);
    }
    
    return true;
  } catch (error) {
    console.error('Error importing portfolio data:', error);
    return false;
  }
};