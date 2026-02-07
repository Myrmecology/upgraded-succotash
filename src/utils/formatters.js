/* ============================================
   FORMATTING UTILITIES
   Currency, numbers, dates, percentages
   ============================================ */

/**
 * Format number as USD currency
 * @param {number} value - The value to format
 * @param {number} decimals - Number of decimal places (default: 2)
 * @returns {string} Formatted currency string
 */
export const formatCurrency = (value, decimals = 2) => {
  if (value === null || value === undefined || isNaN(value)) {
    return '$0.00';
  }
  
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals
  }).format(value);
};

/**
 * Format number with commas
 * @param {number} value - The value to format
 * @param {number} decimals - Number of decimal places (default: 2)
 * @returns {string} Formatted number string
 */
export const formatNumber = (value, decimals = 2) => {
  if (value === null || value === undefined || isNaN(value)) {
    return '0';
  }
  
  return new Intl.NumberFormat('en-US', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals
  }).format(value);
};

/**
 * Format percentage
 * @param {number} value - The value to format (e.g., 0.05 for 5%)
 * @param {number} decimals - Number of decimal places (default: 2)
 * @returns {string} Formatted percentage string
 */
export const formatPercent = (value, decimals = 2) => {
  if (value === null || value === undefined || isNaN(value)) {
    return '0.00%';
  }
  
  return `${(value * 100).toFixed(decimals)}%`;
};

/**
 * Format percentage with + or - sign
 * @param {number} value - The value to format
 * @param {number} decimals - Number of decimal places (default: 2)
 * @returns {string} Formatted percentage with sign
 */
export const formatPercentChange = (value, decimals = 2) => {
  if (value === null || value === undefined || isNaN(value)) {
    return '0.00%';
  }
  
  const sign = value >= 0 ? '+' : '';
  return `${sign}${(value * 100).toFixed(decimals)}%`;
};

/**
 * Format large numbers with abbreviations (K, M, B, T)
 * @param {number} value - The value to format
 * @returns {string} Abbreviated number string
 */
export const formatLargeNumber = (value) => {
  if (value === null || value === undefined || isNaN(value)) {
    return '0';
  }
  
  const absValue = Math.abs(value);
  const sign = value < 0 ? '-' : '';
  
  if (absValue >= 1e12) {
    return `${sign}${(absValue / 1e12).toFixed(2)}T`;
  } else if (absValue >= 1e9) {
    return `${sign}${(absValue / 1e9).toFixed(2)}B`;
  } else if (absValue >= 1e6) {
    return `${sign}${(absValue / 1e6).toFixed(2)}M`;
  } else if (absValue >= 1e3) {
    return `${sign}${(absValue / 1e3).toFixed(2)}K`;
  }
  
  return `${sign}${absValue.toFixed(2)}`;
};

/**
 * Format date to readable string
 * @param {string|Date} date - The date to format
 * @returns {string} Formatted date string
 */
export const formatDate = (date) => {
  if (!date) return 'N/A';
  
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  
  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  }).format(dateObj);
};

/**
 * Format date and time to readable string
 * @param {string|Date} date - The date to format
 * @returns {string} Formatted datetime string
 */
export const formatDateTime = (date) => {
  if (!date) return 'N/A';
  
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  
  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  }).format(dateObj);
};

/**
 * Format time ago (e.g., "2 hours ago")
 * @param {string|Date} date - The date to format
 * @returns {string} Time ago string
 */
export const formatTimeAgo = (date) => {
  if (!date) return 'N/A';
  
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  const now = new Date();
  const seconds = Math.floor((now - dateObj) / 1000);
  
  const intervals = {
    year: 31536000,
    month: 2592000,
    week: 604800,
    day: 86400,
    hour: 3600,
    minute: 60
  };
  
  for (const [unit, secondsInUnit] of Object.entries(intervals)) {
    const interval = Math.floor(seconds / secondsInUnit);
    if (interval >= 1) {
      return `${interval} ${unit}${interval === 1 ? '' : 's'} ago`;
    }
  }
  
  return 'Just now';
};

/**
 * Get color class based on value (positive/negative)
 * @param {number} value - The value to check
 * @returns {string} CSS class name
 */
export const getColorClass = (value) => {
  if (value > 0) return 'text-up';
  if (value < 0) return 'text-down';
  return 'text-neutral';
};

/**
 * Get badge class based on value (positive/negative)
 * @param {number} value - The value to check
 * @returns {string} CSS class name
 */
export const getBadgeClass = (value) => {
  if (value > 0) return 'badge-up';
  if (value < 0) return 'badge-down';
  return 'badge-neutral';
};

/**
 * Format stock symbol (uppercase)
 * @param {string} symbol - Stock symbol
 * @returns {string} Formatted symbol
 */
export const formatSymbol = (symbol) => {
  if (!symbol) return '';
  return symbol.toUpperCase().trim();
};

/**
 * Truncate text with ellipsis
 * @param {string} text - Text to truncate
 * @param {number} maxLength - Maximum length
 * @returns {string} Truncated text
 */
export const truncateText = (text, maxLength = 100) => {
  if (!text || text.length <= maxLength) return text;
  return text.substring(0, maxLength) + '...';
};

/**
 * Format volume (shares traded)
 * @param {number} volume - Trading volume
 * @returns {string} Formatted volume
 */
export const formatVolume = (volume) => {
  if (volume === null || volume === undefined || isNaN(volume)) {
    return '0';
  }
  
  return formatLargeNumber(volume);
};

/**
 * Calculate percentage change
 * @param {number} current - Current value
 * @param {number} previous - Previous value
 * @returns {number} Percentage change as decimal
 */
export const calculatePercentChange = (current, previous) => {
  if (!previous || previous === 0) return 0;
  return (current - previous) / previous;
};

/**
 * Format market cap
 * @param {number} marketCap - Market capitalization
 * @returns {string} Formatted market cap
 */
export const formatMarketCap = (marketCap) => {
  if (marketCap === null || marketCap === undefined || isNaN(marketCap)) {
    return 'N/A';
  }
  
  return formatLargeNumber(marketCap);
};