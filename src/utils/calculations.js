/* ============================================
   CALCULATION UTILITIES
   Portfolio calculations, gains/losses, etc.
   ============================================ */

/**
 * Calculate total portfolio value
 * @param {Array} holdings - Array of stock holdings
 * @param {Object} currentPrices - Object with current prices {symbol: price}
 * @param {number} cash - Available cash
 * @returns {number} Total portfolio value
 */
export const calculatePortfolioValue = (holdings, currentPrices, cash) => {
  const holdingsValue = holdings.reduce((total, holding) => {
    const currentPrice = currentPrices[holding.symbol] || 0;
    return total + (holding.quantity * currentPrice);
  }, 0);
  
  return holdingsValue + cash;
};

/**
 * Calculate gain/loss for a specific holding
 * @param {Object} holding - Holding object with symbol, quantity, averageCost
 * @param {number} currentPrice - Current stock price
 * @returns {Object} Object with gainLoss and gainLossPercent
 */
export const calculateHoldingGainLoss = (holding, currentPrice) => {
  if (!holding || !currentPrice) {
    return { gainLoss: 0, gainLossPercent: 0 };
  }
  
  const costBasis = holding.quantity * holding.averageCost;
  const currentValue = holding.quantity * currentPrice;
  const gainLoss = currentValue - costBasis;
  const gainLossPercent = costBasis > 0 ? gainLoss / costBasis : 0;
  
  return {
    gainLoss,
    gainLossPercent,
    costBasis,
    currentValue
  };
};

/**
 * Calculate total portfolio gain/loss
 * @param {Array} holdings - Array of stock holdings
 * @param {Object} currentPrices - Object with current prices
 * @param {number} initialCash - Initial starting cash
 * @param {number} currentCash - Current available cash
 * @returns {Object} Total gains/losses
 */
export const calculateTotalGainLoss = (holdings, currentPrices, initialCash, currentCash) => {
  let totalCostBasis = initialCash - currentCash;
  let totalCurrentValue = 0;
  
  holdings.forEach(holding => {
    const currentPrice = currentPrices[holding.symbol] || 0;
    const costBasis = holding.quantity * holding.averageCost;
    const currentValue = holding.quantity * currentPrice;
    
    totalCostBasis += costBasis;
    totalCurrentValue += currentValue;
  });
  
  const totalGainLoss = totalCurrentValue - totalCostBasis;
  const totalGainLossPercent = totalCostBasis > 0 ? totalGainLoss / totalCostBasis : 0;
  
  return {
    totalGainLoss,
    totalGainLossPercent,
    totalCostBasis,
    totalCurrentValue
  };
};

/**
 * Calculate portfolio allocation percentages
 * @param {Array} holdings - Array of stock holdings
 * @param {Object} currentPrices - Object with current prices
 * @returns {Array} Array of holdings with allocation percentages
 */
export const calculatePortfolioAllocation = (holdings, currentPrices) => {
  // Calculate total portfolio value (excluding cash)
  const totalValue = holdings.reduce((total, holding) => {
    const currentPrice = currentPrices[holding.symbol] || 0;
    return total + (holding.quantity * currentPrice);
  }, 0);
  
  if (totalValue === 0) return [];
  
  // Calculate allocation for each holding
  return holdings.map(holding => {
    const currentPrice = currentPrices[holding.symbol] || 0;
    const holdingValue = holding.quantity * currentPrice;
    const allocation = (holdingValue / totalValue) * 100;
    
    return {
      ...holding,
      currentPrice,
      holdingValue,
      allocation
    };
  }).sort((a, b) => b.allocation - a.allocation); // Sort by largest allocation
};

/**
 * Calculate moving average
 * @param {Array} data - Array of price data points
 * @param {number} period - Number of periods for the average
 * @returns {number} Moving average
 */
export const calculateMovingAverage = (data, period) => {
  if (!data || data.length < period) return null;
  
  const slice = data.slice(-period);
  const sum = slice.reduce((acc, val) => acc + val, 0);
  return sum / period;
};

/**
 * Calculate price change
 * @param {number} currentPrice - Current price
 * @param {number} previousPrice - Previous price
 * @returns {Object} Object with change amount and percent
 */
export const calculatePriceChange = (currentPrice, previousPrice) => {
  if (!currentPrice || !previousPrice) {
    return { change: 0, changePercent: 0 };
  }
  
  const change = currentPrice - previousPrice;
  const changePercent = (change / previousPrice);
  
  return { change, changePercent };
};

/**
 * Calculate risk metrics for portfolio
 * @param {Array} holdings - Array of stock holdings
 * @param {Object} currentPrices - Object with current prices
 * @returns {Object} Risk metrics
 */
export const calculateRiskMetrics = (holdings, currentPrices) => {
  const allocation = calculatePortfolioAllocation(holdings, currentPrices);
  
  // Diversification score (0-100)
  // Higher score = more diversified
  const holdingsCount = holdings.length;
  let diversificationScore = 0;
  
  if (holdingsCount === 0) {
    diversificationScore = 0;
  } else if (holdingsCount === 1) {
    diversificationScore = 20;
  } else {
    // Calculate based on distribution
    const largestAllocation = allocation[0]?.allocation || 0;
    diversificationScore = Math.min(100, (holdingsCount * 10) - (largestAllocation / 2));
  }
  
  return {
    diversificationScore: Math.round(diversificationScore),
    holdingsCount,
    largestPosition: allocation[0]?.symbol || 'N/A',
    largestPositionPercent: allocation[0]?.allocation || 0
  };
};

/**
 * Calculate daily return
 * @param {number} currentValue - Current portfolio value
 * @param {number} previousValue - Previous portfolio value
 * @returns {number} Daily return as percentage
 */
export const calculateDailyReturn = (currentValue, previousValue) => {
  if (!previousValue || previousValue === 0) return 0;
  return ((currentValue - previousValue) / previousValue);
};

/**
 * Calculate annualized return
 * @param {number} currentValue - Current portfolio value
 * @param {number} initialValue - Initial portfolio value
 * @param {number} daysHeld - Number of days held
 * @returns {number} Annualized return as percentage
 */
export const calculateAnnualizedReturn = (currentValue, initialValue, daysHeld) => {
  if (!initialValue || initialValue === 0 || daysHeld === 0) return 0;
  
  const totalReturn = (currentValue - initialValue) / initialValue;
  const yearsHeld = daysHeld / 365;
  const annualizedReturn = Math.pow(1 + totalReturn, 1 / yearsHeld) - 1;
  
  return annualizedReturn;
};

/**
 * Validate buy transaction
 * @param {number} quantity - Number of shares to buy
 * @param {number} price - Price per share
 * @param {number} availableCash - Available cash
 * @returns {Object} Validation result
 */
export const validateBuyTransaction = (quantity, price, availableCash) => {
  const totalCost = quantity * price;
  
  if (quantity <= 0) {
    return { valid: false, message: 'Quantity must be greater than 0' };
  }
  
  if (price <= 0) {
    return { valid: false, message: 'Invalid price' };
  }
  
  if (totalCost > availableCash) {
    return { valid: false, message: 'Insufficient funds' };
  }
  
  return { valid: true, totalCost };
};

/**
 * Validate sell transaction
 * @param {number} quantity - Number of shares to sell
 * @param {Object} holding - Current holding object
 * @returns {Object} Validation result
 */
export const validateSellTransaction = (quantity, holding) => {
  if (!holding) {
    return { valid: false, message: 'No position in this stock' };
  }
  
  if (quantity <= 0) {
    return { valid: false, message: 'Quantity must be greater than 0' };
  }
  
  if (quantity > holding.quantity) {
    return { valid: false, message: 'Insufficient shares' };
  }
  
  return { valid: true };
};

/**
 * Calculate tax implications (simplified)
 * @param {number} gainLoss - Gain or loss amount
 * @param {number} daysHeld - Number of days position was held
 * @returns {Object} Tax info
 */
export const calculateTaxImplications = (gainLoss, daysHeld) => {
  // Simplified tax calculation
  // Long-term capital gains (>365 days): 15%
  // Short-term capital gains (<=365 days): 25%
  
  if (gainLoss <= 0) {
    return {
      taxableGain: 0,
      estimatedTax: 0,
      taxRate: 0,
      isLongTerm: daysHeld > 365
    };
  }
  
  const isLongTerm = daysHeld > 365;
  const taxRate = isLongTerm ? 0.15 : 0.25;
  const estimatedTax = gainLoss * taxRate;
  
  return {
    taxableGain: gainLoss,
    estimatedTax,
    taxRate,
    isLongTerm
  };
};