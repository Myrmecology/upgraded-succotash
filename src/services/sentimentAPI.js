/* ============================================
   SENTIMENT API SERVICE
   Advanced sentiment analysis for news and market data
   ============================================ */

/**
 * Analyze text sentiment with scoring
 * @param {string} text - Text to analyze
 * @returns {Object} Sentiment analysis result
 */
export const analyzeSentiment = (text) => {
  if (!text) {
    return {
      sentiment: 'neutral',
      score: 0,
      confidence: 0
    };
  }
  
  const lowerText = text.toLowerCase();
  
  // Comprehensive keyword lists with weights
  const positiveKeywords = {
    // Strong positive (weight: 3)
    'surge': 3, 'soar': 3, 'boom': 3, 'skyrocket': 3, 'breakthrough': 3,
    'record-high': 3, 'exceptional': 3, 'outstanding': 3, 'tremendous': 3,
    
    // Moderate positive (weight: 2)
    'gain': 2, 'profit': 2, 'growth': 2, 'rise': 2, 'rally': 2,
    'strong': 2, 'beat': 2, 'exceed': 2, 'positive': 2, 'success': 2,
    'jump': 2, 'spike': 2, 'advance': 2, 'upgrade': 2, 'bullish': 2,
    
    // Mild positive (weight: 1)
    'up': 1, 'high': 1, 'improve': 1, 'optimistic': 1, 'confidence': 1,
    'recover': 1, 'rebound': 1, 'momentum': 1, 'opportunity': 1
  };
  
  const negativeKeywords = {
    // Strong negative (weight: 3)
    'crash': 3, 'plunge': 3, 'collapse': 3, 'disaster': 3, 'crisis': 3,
    'bankruptcy': 3, 'fraud': 3, 'scandal': 3, 'devastate': 3,
    
    // Moderate negative (weight: 2)
    'loss': 2, 'fall': 2, 'decline': 2, 'drop': 2, 'weak': 2,
    'miss': 2, 'negative': 2, 'fail': 2, 'concern': 2, 'risk': 2,
    'tumble': 2, 'slide': 2, 'slump': 2, 'downgrade': 2, 'bearish': 2,
    
    // Mild negative (weight: 1)
    'down': 1, 'low': 1, 'worry': 1, 'struggle': 1, 'challenge': 1,
    'uncertain': 1, 'volatile': 1, 'pressure': 1, 'caution': 1
  };
  
  let positiveScore = 0;
  let negativeScore = 0;
  let totalMatches = 0;
  
  // Calculate positive score
  Object.entries(positiveKeywords).forEach(([word, weight]) => {
    const regex = new RegExp(`\\b${word}\\b`, 'gi');
    const matches = (lowerText.match(regex) || []).length;
    if (matches > 0) {
      positiveScore += matches * weight;
      totalMatches += matches;
    }
  });
  
  // Calculate negative score
  Object.entries(negativeKeywords).forEach(([word, weight]) => {
    const regex = new RegExp(`\\b${word}\\b`, 'gi');
    const matches = (lowerText.match(regex) || []).length;
    if (matches > 0) {
      negativeScore += matches * weight;
      totalMatches += matches;
    }
  });
  
  // Calculate net sentiment score (-100 to +100)
  const netScore = positiveScore - negativeScore;
  const maxPossibleScore = Math.max(positiveScore + negativeScore, 1);
  const normalizedScore = Math.round((netScore / maxPossibleScore) * 100);
  
  // Determine sentiment category
  let sentiment;
  if (normalizedScore > 20) {
    sentiment = 'positive';
  } else if (normalizedScore < -20) {
    sentiment = 'negative';
  } else {
    sentiment = 'neutral';
  }
  
  // Calculate confidence (0-100)
  const confidence = Math.min(100, Math.round((totalMatches / (text.split(' ').length || 1)) * 100));
  
  return {
    sentiment,
    score: normalizedScore,
    confidence,
    positiveScore,
    negativeScore,
    totalMatches
  };
};

/**
 * Analyze sentiment for multiple texts and aggregate
 * @param {Array<string>} texts - Array of texts to analyze
 * @returns {Object} Aggregated sentiment analysis
 */
export const analyzeBulkSentiment = (texts) => {
  if (!texts || texts.length === 0) {
    return {
      sentiment: 'neutral',
      averageScore: 0,
      averageConfidence: 0,
      distribution: { positive: 0, negative: 0, neutral: 0 }
    };
  }
  
  const results = texts.map(text => analyzeSentiment(text));
  
  const totalScore = results.reduce((sum, r) => sum + r.score, 0);
  const totalConfidence = results.reduce((sum, r) => sum + r.confidence, 0);
  
  const distribution = {
    positive: results.filter(r => r.sentiment === 'positive').length,
    negative: results.filter(r => r.sentiment === 'negative').length,
    neutral: results.filter(r => r.sentiment === 'neutral').length
  };
  
  const averageScore = Math.round(totalScore / results.length);
  
  let overallSentiment;
  if (averageScore > 20) {
    overallSentiment = 'positive';
  } else if (averageScore < -20) {
    overallSentiment = 'negative';
  } else {
    overallSentiment = 'neutral';
  }
  
  return {
    sentiment: overallSentiment,
    averageScore,
    averageConfidence: Math.round(totalConfidence / results.length),
    distribution,
    count: results.length
  };
};

/**
 * Get sentiment emoji representation
 * @param {string} sentiment - Sentiment value
 * @returns {string} Emoji
 */
export const getSentimentEmoji = (sentiment) => {
  const emojis = {
    'positive': '😊',
    'negative': '😟',
    'neutral': '😐'
  };
  return emojis[sentiment] || '😐';
};

/**
 * Get sentiment icon
 * @param {string} sentiment - Sentiment value
 * @returns {string} Icon character
 */
export const getSentimentIcon = (sentiment) => {
  const icons = {
    'positive': '▲',
    'negative': '▼',
    'neutral': '■'
  };
  return icons[sentiment] || '■';
};

/**
 * Get sentiment color
 * @param {string} sentiment - Sentiment value
 * @returns {string} CSS color variable
 */
export const getSentimentColor = (sentiment) => {
  const colors = {
    'positive': 'var(--color-up)',
    'negative': 'var(--color-down)',
    'neutral': 'var(--color-neutral)'
  };
  return colors[sentiment] || 'var(--color-neutral)';
};

/**
 * Get sentiment label with intensity
 * @param {number} score - Sentiment score (-100 to +100)
 * @returns {string} Descriptive label
 */
export const getSentimentLabel = (score) => {
  if (score >= 70) return 'Very Bullish';
  if (score >= 40) return 'Bullish';
  if (score >= 20) return 'Slightly Bullish';
  if (score > -20) return 'Neutral';
  if (score > -40) return 'Slightly Bearish';
  if (score > -70) return 'Bearish';
  return 'Very Bearish';
};

/**
 * Analyze market sentiment from news headlines
 * @param {Array<Object>} newsArticles - Array of news article objects
 * @returns {Object} Market sentiment analysis
 */
export const analyzeMarketSentiment = (newsArticles) => {
  if (!newsArticles || newsArticles.length === 0) {
    return {
      overallSentiment: 'neutral',
      sentimentScore: 0,
      bullishCount: 0,
      bearishCount: 0,
      neutralCount: 0,
      confidence: 0
    };
  }
  
  const headlines = newsArticles.map(article => article.headline || article.title || '');
  const analysis = analyzeBulkSentiment(headlines);
  
  return {
    overallSentiment: analysis.sentiment,
    sentimentScore: analysis.averageScore,
    bullishCount: analysis.distribution.positive,
    bearishCount: analysis.distribution.negative,
    neutralCount: analysis.distribution.neutral,
    confidence: analysis.averageConfidence,
    totalArticles: newsArticles.length
  };
};

/**
 * Generate sentiment trend from time-series data
 * @param {Array<Object>} historicalData - Array of {date, sentiment} objects
 * @returns {Object} Trend analysis
 */
export const analyzeSentimentTrend = (historicalData) => {
  if (!historicalData || historicalData.length < 2) {
    return {
      trend: 'stable',
      direction: 0,
      volatility: 0
    };
  }
  
  const scores = historicalData.map(d => d.score || 0);
  const recentScores = scores.slice(-7); // Last 7 data points
  const earlierScores = scores.slice(-14, -7); // Previous 7 data points
  
  const recentAvg = recentScores.reduce((a, b) => a + b, 0) / recentScores.length;
  const earlierAvg = earlierScores.reduce((a, b) => a + b, 0) / earlierScores.length;
  
  const direction = recentAvg - earlierAvg;
  
  // Calculate volatility (standard deviation)
  const mean = scores.reduce((a, b) => a + b, 0) / scores.length;
  const variance = scores.reduce((sum, score) => sum + Math.pow(score - mean, 2), 0) / scores.length;
  const volatility = Math.sqrt(variance);
  
  let trend;
  if (direction > 10) trend = 'improving';
  else if (direction < -10) trend = 'declining';
  else trend = 'stable';
  
  return {
    trend,
    direction: Math.round(direction),
    volatility: Math.round(volatility),
    recentAverage: Math.round(recentAvg),
    earlierAverage: Math.round(earlierAvg)
  };
};

/**
 * Get sentiment recommendation
 * @param {Object} sentimentAnalysis - Sentiment analysis object
 * @returns {string} Investment recommendation
 */
export const getSentimentRecommendation = (sentimentAnalysis) => {
  const { sentiment, score, confidence } = sentimentAnalysis;
  
  if (confidence < 30) {
    return 'Insufficient data for recommendation';
  }
  
  if (sentiment === 'positive' && score > 50) {
    return 'Strong positive sentiment - Consider buying';
  } else if (sentiment === 'positive') {
    return 'Positive sentiment - Cautiously optimistic';
  } else if (sentiment === 'negative' && score < -50) {
    return 'Strong negative sentiment - Exercise caution';
  } else if (sentiment === 'negative') {
    return 'Negative sentiment - Monitor closely';
  }
  
  return 'Neutral sentiment - Hold current position';
};