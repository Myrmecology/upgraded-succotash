/* ============================================
   CRYPTOCURRENCY API SERVICE
   Fetch crypto prices and market data
   ============================================ */

import axios from 'axios';

// CoinGecko API (No key required for free tier!)
const COINGECKO_BASE = 'https://api.coingecko.com/api/v3';

/**
 * Get cryptocurrency prices
 * @param {Array<string>} ids - Array of crypto IDs (bitcoin, ethereum, etc.)
 * @returns {Promise<Array>} Array of crypto data
 */
export const getCryptoPrices = async (ids = ['bitcoin', 'ethereum', 'cardano', 'solana', 'dogecoin']) => {
  try {
    const response = await axios.get(`${COINGECKO_BASE}/coins/markets`, {
      params: {
        vs_currency: 'usd',
        ids: ids.join(','),
        order: 'market_cap_desc',
        per_page: ids.length,
        page: 1,
        sparkline: false,
        price_change_percentage: '24h'
      }
    });
    
    return response.data.map(coin => ({
      id: coin.id,
      symbol: coin.symbol.toUpperCase(),
      name: coin.name,
      image: coin.image,
      currentPrice: coin.current_price,
      marketCap: coin.market_cap,
      marketCapRank: coin.market_cap_rank,
      volume24h: coin.total_volume,
      priceChange24h: coin.price_change_24h,
      priceChangePercent24h: coin.price_change_percentage_24h,
      high24h: coin.high_24h,
      low24h: coin.low_24h,
      circulatingSupply: coin.circulating_supply,
      totalSupply: coin.total_supply,
      lastUpdated: coin.last_updated
    }));
  } catch (error) {
    console.error('Error fetching crypto prices:', error);
    
    // Return mock data if API fails
    return getMockCryptoData();
  }
};

/**
 * Get single cryptocurrency data
 * @param {string} id - Crypto ID (bitcoin, ethereum, etc.)
 * @returns {Promise<Object>} Crypto data
 */
export const getCryptoById = async (id) => {
  try {
    const response = await axios.get(`${COINGECKO_BASE}/coins/${id}`, {
      params: {
        localization: false,
        tickers: false,
        community_data: false,
        developer_data: false
      }
    });
    
    return {
      id: response.data.id,
      symbol: response.data.symbol.toUpperCase(),
      name: response.data.name,
      image: response.data.image.large,
      description: response.data.description.en,
      currentPrice: response.data.market_data.current_price.usd,
      marketCap: response.data.market_data.market_cap.usd,
      marketCapRank: response.data.market_cap_rank,
      volume24h: response.data.market_data.total_volume.usd,
      priceChange24h: response.data.market_data.price_change_24h,
      priceChangePercent24h: response.data.market_data.price_change_percentage_24h,
      high24h: response.data.market_data.high_24h.usd,
      low24h: response.data.market_data.low_24h.usd,
      ath: response.data.market_data.ath.usd,
      athDate: response.data.market_data.ath_date.usd,
      atl: response.data.market_data.atl.usd,
      atlDate: response.data.market_data.atl_date.usd,
      circulatingSupply: response.data.market_data.circulating_supply,
      totalSupply: response.data.market_data.total_supply,
      maxSupply: response.data.market_data.max_supply
    };
  } catch (error) {
    console.error(`Error fetching crypto data for ${id}:`, error);
    return null;
  }
};

/**
 * Get cryptocurrency historical data
 * @param {string} id - Crypto ID
 * @param {number} days - Number of days (1, 7, 30, 90, 365, max)
 * @returns {Promise<Array>} Array of price data points
 */
export const getCryptoHistoricalData = async (id, days = 30) => {
  try {
    const response = await axios.get(`${COINGECKO_BASE}/coins/${id}/market_chart`, {
      params: {
        vs_currency: 'usd',
        days: days,
        interval: days <= 1 ? 'hourly' : 'daily'
      }
    });
    
    return response.data.prices.map(([timestamp, price]) => ({
      date: new Date(timestamp).toISOString(),
      price: price
    }));
  } catch (error) {
    console.error(`Error fetching historical data for ${id}:`, error);
    return [];
  }
};

/**
 * Search cryptocurrencies
 * @param {string} query - Search query
 * @returns {Promise<Array>} Array of matching cryptocurrencies
 */
export const searchCrypto = async (query) => {
  try {
    const response = await axios.get(`${COINGECKO_BASE}/search`, {
      params: {
        query: query
      }
    });
    
    return response.data.coins.slice(0, 10).map(coin => ({
      id: coin.id,
      name: coin.name,
      symbol: coin.symbol.toUpperCase(),
      marketCapRank: coin.market_cap_rank,
      thumb: coin.thumb,
      large: coin.large
    }));
  } catch (error) {
    console.error('Error searching crypto:', error);
    return [];
  }
};

/**
 * Get trending cryptocurrencies
 * @returns {Promise<Array>} Array of trending cryptos
 */
export const getTrendingCrypto = async () => {
  try {
    const response = await axios.get(`${COINGECKO_BASE}/search/trending`);
    
    return response.data.coins.map(item => ({
      id: item.item.id,
      name: item.item.name,
      symbol: item.item.symbol,
      marketCapRank: item.item.market_cap_rank,
      thumb: item.item.thumb,
      small: item.item.small,
      large: item.item.large,
      score: item.item.score
    }));
  } catch (error) {
    console.error('Error fetching trending crypto:', error);
    return [];
  }
};

/**
 * Get global crypto market data
 * @returns {Promise<Object>} Global market stats
 */
export const getGlobalCryptoData = async () => {
  try {
    const response = await axios.get(`${COINGECKO_BASE}/global`);
    
    return {
      totalMarketCap: response.data.data.total_market_cap.usd,
      total24hVolume: response.data.data.total_volume.usd,
      marketCapPercentage: response.data.data.market_cap_percentage,
      marketCapChangePercent24h: response.data.data.market_cap_change_percentage_24h_usd,
      activeCryptocurrencies: response.data.data.active_cryptocurrencies,
      markets: response.data.data.markets,
      updatedAt: response.data.data.updated_at
    };
  } catch (error) {
    console.error('Error fetching global crypto data:', error);
    return null;
  }
};

/**
 * Format crypto symbol with icon
 * @param {string} symbol - Crypto symbol
 * @returns {string} Symbol with emoji icon
 */
export const formatCryptoSymbol = (symbol) => {
  const icons = {
    'BTC': '₿',
    'ETH': 'Ξ',
    'DOGE': '🐕',
    'ADA': '₳',
    'SOL': '◎'
  };
  
  return icons[symbol.toUpperCase()] || symbol.toUpperCase();
};

/**
 * Get crypto category label
 * @param {number} marketCapRank - Market cap rank
 * @returns {string} Category label
 */
export const getCryptoCategory = (marketCapRank) => {
  if (marketCapRank <= 10) return 'Large Cap';
  if (marketCapRank <= 50) return 'Mid Cap';
  if (marketCapRank <= 200) return 'Small Cap';
  return 'Micro Cap';
};

// ==================== MOCK DATA FOR DEVELOPMENT ====================

/**
 * Get mock crypto data
 */
const getMockCryptoData = () => {
  return [
    {
      id: 'bitcoin',
      symbol: 'BTC',
      name: 'Bitcoin',
      image: 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png',
      currentPrice: 45678.90,
      marketCap: 890000000000,
      marketCapRank: 1,
      volume24h: 25000000000,
      priceChange24h: 567.89,
      priceChangePercent24h: 1.26,
      high24h: 46000.00,
      low24h: 45200.00,
      circulatingSupply: 19500000,
      totalSupply: 21000000,
      lastUpdated: new Date().toISOString()
    },
    {
      id: 'ethereum',
      symbol: 'ETH',
      name: 'Ethereum',
      image: 'https://assets.coingecko.com/coins/images/279/large/ethereum.png',
      currentPrice: 2456.78,
      marketCap: 295000000000,
      marketCapRank: 2,
      volume24h: 15000000000,
      priceChange24h: -45.67,
      priceChangePercent24h: -1.82,
      high24h: 2500.00,
      low24h: 2400.00,
      circulatingSupply: 120000000,
      totalSupply: null,
      lastUpdated: new Date().toISOString()
    },
    {
      id: 'cardano',
      symbol: 'ADA',
      name: 'Cardano',
      image: 'https://assets.coingecko.com/coins/images/975/large/cardano.png',
      currentPrice: 0.5678,
      marketCap: 20000000000,
      marketCapRank: 8,
      volume24h: 450000000,
      priceChange24h: 0.0123,
      priceChangePercent24h: 2.21,
      high24h: 0.58,
      low24h: 0.55,
      circulatingSupply: 35000000000,
      totalSupply: 45000000000,
      lastUpdated: new Date().toISOString()
    },
    {
      id: 'solana',
      symbol: 'SOL',
      name: 'Solana',
      image: 'https://assets.coingecko.com/coins/images/4128/large/solana.png',
      currentPrice: 98.45,
      marketCap: 42000000000,
      marketCapRank: 5,
      volume24h: 1800000000,
      priceChange24h: 3.21,
      priceChangePercent24h: 3.37,
      high24h: 100.00,
      low24h: 95.00,
      circulatingSupply: 425000000,
      totalSupply: 555000000,
      lastUpdated: new Date().toISOString()
    },
    {
      id: 'dogecoin',
      symbol: 'DOGE',
      name: 'Dogecoin',
      image: 'https://assets.coingecko.com/coins/images/5/large/dogecoin.png',
      currentPrice: 0.0789,
      marketCap: 11000000000,
      marketCapRank: 10,
      volume24h: 380000000,
      priceChange24h: 0.0012,
      priceChangePercent24h: 1.54,
      high24h: 0.08,
      low24h: 0.077,
      circulatingSupply: 140000000000,
      totalSupply: null,
      lastUpdated: new Date().toISOString()
    }
  ];
};