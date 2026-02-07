/* ============================================
   STOCK API SERVICE
   Fetch real-time and historical stock data
   ============================================ */

import axios from 'axios';

const ALPHA_VANTAGE_KEY = process.env.REACT_APP_ALPHA_VANTAGE_API_KEY;
const FINNHUB_KEY = process.env.REACT_APP_FINNHUB_API_KEY;

// API Base URLs
const ALPHA_VANTAGE_BASE = 'https://www.alphavantage.co/query';
const FINNHUB_BASE = 'https://finnhub.io/api/v1';

/**
 * Get real-time stock quote
 * @param {string} symbol - Stock symbol
 * @returns {Promise<Object>} Stock quote data
 */
export const getStockQuote = async (symbol) => {
  try {
    // Using Finnhub for real-time quotes
    const response = await axios.get(`${FINNHUB_BASE}/quote`, {
      params: {
        symbol: symbol.toUpperCase(),
        token: FINNHUB_KEY
      }
    });
    
    return {
      symbol: symbol.toUpperCase(),
      currentPrice: response.data.c || 0,
      change: response.data.d || 0,
      changePercent: response.data.dp || 0,
      high: response.data.h || 0,
      low: response.data.l || 0,
      open: response.data.o || 0,
      previousClose: response.data.pc || 0,
      timestamp: Date.now()
    };
  } catch (error) {
    console.error(`Error fetching quote for ${symbol}:`, error);
    
    // Return mock data if API fails (for development)
    return getMockQuote(symbol);
  }
};

/**
 * Get multiple stock quotes at once
 * @param {Array<string>} symbols - Array of stock symbols
 * @returns {Promise<Object>} Object with symbol as key, quote data as value
 */
export const getMultipleQuotes = async (symbols) => {
  try {
    const promises = symbols.map(symbol => getStockQuote(symbol));
    const quotes = await Promise.all(promises);
    
    // Convert array to object with symbol as key
    return quotes.reduce((acc, quote) => {
      acc[quote.symbol] = quote;
      return acc;
    }, {});
  } catch (error) {
    console.error('Error fetching multiple quotes:', error);
    return {};
  }
};

/**
 * Get historical stock data
 * @param {string} symbol - Stock symbol
 * @param {string} interval - Time interval (daily, weekly, monthly)
 * @returns {Promise<Array>} Array of historical data points
 */
export const getHistoricalData = async (symbol, interval = 'daily') => {
  try {
    // Using Alpha Vantage for historical data
    const functionMap = {
      'daily': 'TIME_SERIES_DAILY',
      'weekly': 'TIME_SERIES_WEEKLY',
      'monthly': 'TIME_SERIES_MONTHLY'
    };
    
    const response = await axios.get(ALPHA_VANTAGE_BASE, {
      params: {
        function: functionMap[interval] || 'TIME_SERIES_DAILY',
        symbol: symbol.toUpperCase(),
        apikey: ALPHA_VANTAGE_KEY,
        outputsize: 'compact' // Last 100 data points
      }
    });
    
    const timeSeriesKey = Object.keys(response.data).find(key => key.includes('Time Series'));
    const timeSeries = response.data[timeSeriesKey];
    
    if (!timeSeries) {
      throw new Error('No time series data found');
    }
    
    // Convert to array format
    const data = Object.entries(timeSeries).map(([date, values]) => ({
      date,
      open: parseFloat(values['1. open']),
      high: parseFloat(values['2. high']),
      low: parseFloat(values['3. low']),
      close: parseFloat(values['4. close']),
      volume: parseInt(values['5. volume'])
    }));
    
    // Sort by date (oldest first)
    return data.reverse();
  } catch (error) {
    console.error(`Error fetching historical data for ${symbol}:`, error);
    
    // Return mock historical data if API fails
    return getMockHistoricalData(symbol);
  }
};

/**
 * Search for stock symbols
 * @param {string} query - Search query
 * @returns {Promise<Array>} Array of matching stocks
 */
export const searchStocks = async (query) => {
  try {
    // Using Alpha Vantage symbol search
    const response = await axios.get(ALPHA_VANTAGE_BASE, {
      params: {
        function: 'SYMBOL_SEARCH',
        keywords: query,
        apikey: ALPHA_VANTAGE_KEY
      }
    });
    
    const matches = response.data.bestMatches || [];
    
    return matches.map(match => ({
      symbol: match['1. symbol'],
      name: match['2. name'],
      type: match['3. type'],
      region: match['4. region'],
      currency: match['8. currency']
    }));
  } catch (error) {
    console.error('Error searching stocks:', error);
    return [];
  }
};

/**
 * Get company profile/info
 * @param {string} symbol - Stock symbol
 * @returns {Promise<Object>} Company information
 */
export const getCompanyProfile = async (symbol) => {
  try {
    // Using Finnhub for company profile
    const response = await axios.get(`${FINNHUB_BASE}/stock/profile2`, {
      params: {
        symbol: symbol.toUpperCase(),
        token: FINNHUB_KEY
      }
    });
    
    return {
      symbol: response.data.ticker,
      name: response.data.name,
      country: response.data.country,
      currency: response.data.currency,
      exchange: response.data.exchange,
      industry: response.data.finnhubIndustry,
      logo: response.data.logo,
      marketCap: response.data.marketCapitalization * 1000000, // Convert to actual value
      phone: response.data.phone,
      shareOutstanding: response.data.shareOutstanding,
      weburl: response.data.weburl
    };
  } catch (error) {
    console.error(`Error fetching company profile for ${symbol}:`, error);
    return getMockCompanyProfile(symbol);
  }
};

/**
 * Get stock fundamentals
 * @param {string} symbol - Stock symbol
 * @returns {Promise<Object>} Fundamental data
 */
export const getStockFundamentals = async (symbol) => {
  try {
    const response = await axios.get(`${FINNHUB_BASE}/stock/metric`, {
      params: {
        symbol: symbol.toUpperCase(),
        metric: 'all',
        token: FINNHUB_KEY
      }
    });
    
    const metrics = response.data.metric || {};
    
    return {
      peRatio: metrics['peNormalizedAnnual'] || null,
      eps: metrics['epsBasicExclExtraItemsTTM'] || null,
      dividendYield: metrics['dividendYieldIndicatedAnnual'] || null,
      beta: metrics['beta'] || null,
      week52High: metrics['52WeekHigh'] || null,
      week52Low: metrics['52WeekLow'] || null,
      marketCap: metrics['marketCapitalization'] || null
    };
  } catch (error) {
    console.error(`Error fetching fundamentals for ${symbol}:`, error);
    return {};
  }
};

// ==================== MOCK DATA FOR DEVELOPMENT ====================

/**
 * Get mock quote data (fallback when API is unavailable)
 */
const getMockQuote = (symbol) => {
  const basePrice = Math.random() * 500 + 50;
  const change = (Math.random() - 0.5) * 10;
  
  return {
    symbol: symbol.toUpperCase(),
    currentPrice: parseFloat(basePrice.toFixed(2)),
    change: parseFloat(change.toFixed(2)),
    changePercent: parseFloat(((change / basePrice) * 100).toFixed(2)),
    high: parseFloat((basePrice + Math.random() * 5).toFixed(2)),
    low: parseFloat((basePrice - Math.random() * 5).toFixed(2)),
    open: parseFloat((basePrice - Math.random() * 3).toFixed(2)),
    previousClose: parseFloat((basePrice - change).toFixed(2)),
    timestamp: Date.now()
  };
};

/**
 * Get mock historical data
 */
const getMockHistoricalData = (symbol) => {
  const data = [];
  const today = new Date();
  const basePrice = Math.random() * 500 + 50;
  
  for (let i = 100; i >= 0; i--) {
    const date = new Date(today);
    date.setDate(date.getDate() - i);
    
    const variance = (Math.random() - 0.5) * 20;
    const price = basePrice + variance;
    
    data.push({
      date: date.toISOString().split('T')[0],
      open: parseFloat(price.toFixed(2)),
      high: parseFloat((price + Math.random() * 5).toFixed(2)),
      low: parseFloat((price - Math.random() * 5).toFixed(2)),
      close: parseFloat((price + (Math.random() - 0.5) * 3).toFixed(2)),
      volume: Math.floor(Math.random() * 10000000)
    });
  }
  
  return data;
};

/**
 * Get mock company profile
 */
const getMockCompanyProfile = (symbol) => {
  return {
    symbol: symbol.toUpperCase(),
    name: `${symbol.toUpperCase()} Inc.`,
    country: 'US',
    currency: 'USD',
    exchange: 'NASDAQ',
    industry: 'Technology',
    logo: '',
    marketCap: Math.random() * 1000000000000,
    phone: '555-0100',
    shareOutstanding: Math.random() * 1000000000,
    weburl: `https://www.${symbol.toLowerCase()}.com`
  };
};