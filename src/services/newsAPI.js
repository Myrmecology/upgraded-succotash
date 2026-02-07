/* ============================================
   NEWS API SERVICE
   Fetch financial news and market updates
   ============================================ */

import axios from 'axios';

const NEWS_API_KEY = process.env.REACT_APP_NEWS_API_KEY;
const FINNHUB_KEY = process.env.REACT_APP_FINNHUB_API_KEY;

// API Base URLs
const NEWS_API_BASE = 'https://newsapi.org/v2';
const FINNHUB_BASE = 'https://finnhub.io/api/v1';

/**
 * Get general market news
 * @param {number} limit - Number of articles to fetch
 * @returns {Promise<Array>} Array of news articles
 */
export const getMarketNews = async (limit = 10) => {
  try {
    // Using NewsAPI for general financial news
    const response = await axios.get(`${NEWS_API_BASE}/top-headlines`, {
      params: {
        category: 'business',
        country: 'us',
        pageSize: limit,
        apiKey: NEWS_API_KEY
      }
    });
    
    return response.data.articles.map(article => ({
      id: article.url,
      headline: article.title,
      summary: article.description,
      source: article.source.name,
      url: article.url,
      image: article.urlToImage,
      publishedAt: article.publishedAt,
      sentiment: analyzeSentiment(article.title + ' ' + article.description)
    }));
  } catch (error) {
    console.error('Error fetching market news:', error);
    
    // Return mock news if API fails
    return getMockMarketNews();
  }
};

/**
 * Get news for specific stock
 * @param {string} symbol - Stock symbol
 * @param {number} limit - Number of articles to fetch
 * @returns {Promise<Array>} Array of news articles
 */
export const getStockNews = async (symbol, limit = 10) => {
  try {
    // Using Finnhub for company-specific news
    const today = new Date();
    const weekAgo = new Date(today);
    weekAgo.setDate(today.getDate() - 7);
    
    const response = await axios.get(`${FINNHUB_BASE}/company-news`, {
      params: {
        symbol: symbol.toUpperCase(),
        from: weekAgo.toISOString().split('T')[0],
        to: today.toISOString().split('T')[0],
        token: FINNHUB_KEY
      }
    });
    
    const articles = response.data.slice(0, limit);
    
    return articles.map(article => ({
      id: article.id || article.url,
      headline: article.headline,
      summary: article.summary,
      source: article.source,
      url: article.url,
      image: article.image,
      publishedAt: new Date(article.datetime * 1000).toISOString(),
      sentiment: analyzeSentiment(article.headline + ' ' + article.summary),
      related: article.related || symbol.toUpperCase()
    }));
  } catch (error) {
    console.error(`Error fetching news for ${symbol}:`, error);
    
    // Return mock stock news if API fails
    return getMockStockNews(symbol);
  }
};

/**
 * Search news by keyword
 * @param {string} query - Search query
 * @param {number} limit - Number of articles to fetch
 * @returns {Promise<Array>} Array of news articles
 */
export const searchNews = async (query, limit = 10) => {
  try {
    const response = await axios.get(`${NEWS_API_BASE}/everything`, {
      params: {
        q: query + ' AND (stock OR market OR finance)',
        sortBy: 'publishedAt',
        pageSize: limit,
        apiKey: NEWS_API_KEY,
        language: 'en'
      }
    });
    
    return response.data.articles.map(article => ({
      id: article.url,
      headline: article.title,
      summary: article.description,
      source: article.source.name,
      url: article.url,
      image: article.urlToImage,
      publishedAt: article.publishedAt,
      sentiment: analyzeSentiment(article.title + ' ' + article.description)
    }));
  } catch (error) {
    console.error('Error searching news:', error);
    return [];
  }
};

/**
 * Simple sentiment analysis
 * @param {string} text - Text to analyze
 * @returns {string} Sentiment: 'positive', 'negative', or 'neutral'
 */
export const analyzeSentiment = (text) => {
  if (!text) return 'neutral';
  
  const lowerText = text.toLowerCase();
  
  // Positive keywords
  const positiveWords = [
    'gain', 'surge', 'bull', 'profit', 'growth', 'rise', 'up', 
    'soar', 'rally', 'boom', 'strong', 'beat', 'exceed', 
    'positive', 'win', 'success', 'breakthrough', 'record',
    'high', 'jump', 'spike', 'climbs', 'advance', 'upgrade'
  ];
  
  // Negative keywords
  const negativeWords = [
    'loss', 'fall', 'bear', 'decline', 'drop', 'down', 
    'plunge', 'crash', 'weak', 'miss', 'below', 'negative',
    'fail', 'risk', 'concern', 'worry', 'struggle', 'low',
    'tumble', 'slide', 'slump', 'retreat', 'downgrade'
  ];
  
  let positiveCount = 0;
  let negativeCount = 0;
  
  positiveWords.forEach(word => {
    if (lowerText.includes(word)) positiveCount++;
  });
  
  negativeWords.forEach(word => {
    if (lowerText.includes(word)) negativeCount++;
  });
  
  if (positiveCount > negativeCount) return 'positive';
  if (negativeCount > positiveCount) return 'negative';
  return 'neutral';
};

/**
 * Get sentiment color class
 * @param {string} sentiment - Sentiment value
 * @returns {string} CSS class name
 */
export const getSentimentClass = (sentiment) => {
  switch (sentiment) {
    case 'positive':
      return 'text-up';
    case 'negative':
      return 'text-down';
    default:
      return 'text-neutral';
  }
};

/**
 * Get sentiment badge class
 * @param {string} sentiment - Sentiment value
 * @returns {string} CSS class name
 */
export const getSentimentBadgeClass = (sentiment) => {
  switch (sentiment) {
    case 'positive':
      return 'badge-up';
    case 'negative':
      return 'badge-down';
    default:
      return 'badge-neutral';
  }
};

/**
 * Get sentiment emoji
 * @param {string} sentiment - Sentiment value
 * @returns {string} Emoji
 */
export const getSentimentEmoji = (sentiment) => {
  switch (sentiment) {
    case 'positive':
      return '📈';
    case 'negative':
      return '📉';
    default:
      return '➡️';
  }
};

// ==================== MOCK DATA FOR DEVELOPMENT ====================

/**
 * Get mock market news
 */
const getMockMarketNews = () => {
  return [
    {
      id: '1',
      headline: 'Tech Stocks Rally as Market Sentiment Improves',
      summary: 'Major technology stocks saw significant gains today as investors responded positively to economic data.',
      source: 'Financial Times',
      url: '#',
      image: 'https://via.placeholder.com/400x200?text=Market+News',
      publishedAt: new Date().toISOString(),
      sentiment: 'positive'
    },
    {
      id: '2',
      headline: 'Federal Reserve Maintains Interest Rates',
      summary: 'The Federal Reserve announced it will keep interest rates steady, signaling confidence in economic stability.',
      source: 'Bloomberg',
      url: '#',
      image: 'https://via.placeholder.com/400x200?text=Fed+News',
      publishedAt: new Date(Date.now() - 3600000).toISOString(),
      sentiment: 'neutral'
    },
    {
      id: '3',
      headline: 'Energy Sector Faces Challenges Amid Price Volatility',
      summary: 'Energy stocks declined as oil prices fluctuated on concerns about global demand.',
      source: 'Reuters',
      url: '#',
      image: 'https://via.placeholder.com/400x200?text=Energy+News',
      publishedAt: new Date(Date.now() - 7200000).toISOString(),
      sentiment: 'negative'
    },
    {
      id: '4',
      headline: 'AI Revolution Drives Record Investment in Tech Sector',
      summary: 'Artificial intelligence companies receive unprecedented funding as investors bet on future growth.',
      source: 'CNBC',
      url: '#',
      image: 'https://via.placeholder.com/400x200?text=AI+Investment',
      publishedAt: new Date(Date.now() - 10800000).toISOString(),
      sentiment: 'positive'
    },
    {
      id: '5',
      headline: 'Global Markets Mixed on Trade Policy Uncertainty',
      summary: 'International markets showed mixed performance as traders digest new trade policy announcements.',
      source: 'Wall Street Journal',
      url: '#',
      image: 'https://via.placeholder.com/400x200?text=Global+Markets',
      publishedAt: new Date(Date.now() - 14400000).toISOString(),
      sentiment: 'neutral'
    }
  ];
};

/**
 * Get mock stock-specific news
 */
const getMockStockNews = (symbol) => {
  return [
    {
      id: '1',
      headline: `${symbol} Reports Strong Quarterly Earnings`,
      summary: `${symbol} exceeded analyst expectations with robust revenue growth and positive guidance.`,
      source: 'MarketWatch',
      url: '#',
      image: 'https://via.placeholder.com/400x200?text=Earnings',
      publishedAt: new Date().toISOString(),
      sentiment: 'positive',
      related: symbol.toUpperCase()
    },
    {
      id: '2',
      headline: `Analysts Upgrade ${symbol} Price Target`,
      summary: `Several major banks raised their price targets for ${symbol} citing strong fundamentals.`,
      source: 'Seeking Alpha',
      url: '#',
      image: 'https://via.placeholder.com/400x200?text=Analyst+Upgrade',
      publishedAt: new Date(Date.now() - 3600000).toISOString(),
      sentiment: 'positive',
      related: symbol.toUpperCase()
    },
    {
      id: '3',
      headline: `${symbol} Announces New Product Launch`,
      summary: `Company reveals innovative new product line expected to drive future growth.`,
      source: 'TechCrunch',
      url: '#',
      image: 'https://via.placeholder.com/400x200?text=Product+Launch',
      publishedAt: new Date(Date.now() - 7200000).toISOString(),
      sentiment: 'positive',
      related: symbol.toUpperCase()
    }
  ];
};