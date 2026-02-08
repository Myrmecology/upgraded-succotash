import React, { useState, useEffect } from 'react';
import { getMarketNews, getStockNews } from '../../services/newsAPI';
import { getSentimentEmoji, getSentimentBadgeClass } from '../../services/sentimentAPI';
import { formatTimeAgo } from '../../utils/formatters';
import './NewsPanel.css';

const NewsPanel = ({ selectedStock }) => {
  const [news, setNews] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [newsType, setNewsType] = useState('market'); // 'market' or 'stock'

  // Fetch news
  useEffect(() => {
    const fetchNews = async () => {
      setIsLoading(true);
      
      try {
        let articles;
        if (selectedStock && newsType === 'stock') {
          articles = await getStockNews(selectedStock, 10);
        } else {
          articles = await getMarketNews(10);
        }
        setNews(articles);
      } catch (error) {
        console.error('Error fetching news:', error);
        setNews([]);
      } finally {
        setIsLoading(false);
      }
    };

    fetchNews();

    // Refresh every 5 minutes
    const interval = setInterval(fetchNews, 300000);
    return () => clearInterval(interval);
  }, [selectedStock, newsType]);

  // Switch between market and stock news
  useEffect(() => {
    if (selectedStock) {
      setNewsType('stock');
    } else {
      setNewsType('market');
    }
  }, [selectedStock]);

  const handleNewsTypeToggle = (type) => {
    setNewsType(type);
  };

  return (
    <div className="news-panel section-container">
      <div className="section-header">
        <div>
          <h2 className="section-title">📰 Financial News</h2>
          <p className="section-subtitle">[ HEADLINES • ANALYSIS • SENTIMENT ]</p>
        </div>
      </div>

      {/* News Type Toggle */}
      {selectedStock && (
        <div className="news-toggle">
          <button
            className={`news-toggle-btn ${newsType === 'market' ? 'active' : ''}`}
            onClick={() => handleNewsTypeToggle('market')}
          >
            Market News
          </button>
          <button
            className={`news-toggle-btn ${newsType === 'stock' ? 'active' : ''}`}
            onClick={() => handleNewsTypeToggle('stock')}
          >
            {selectedStock} News
          </button>
        </div>
      )}

      {/* News List */}
      {isLoading ? (
        <div className="loading-news">
          <div className="spinner"></div>
          <p>Loading latest news...</p>
        </div>
      ) : news.length === 0 ? (
        <div className="no-news">
          <div className="no-news-icon">📭</div>
          <h4>No News Available</h4>
          <p>Check back later for updates</p>
        </div>
      ) : (
        <div className="news-list">
          {news.map((article, index) => (
            <div key={article.id || index} className="news-card">
              <div className="news-content">
                <div className="news-header">
                  <span className="news-source">{article.source}</span>
                  <span className="news-time">{formatTimeAgo(article.publishedAt)}</span>
                </div>

                <h3 className="news-headline">
                  {article.headline}
                </h3>

                {article.summary && (
                  <p className="news-summary">{article.summary}</p>
                )}

                <div className="news-footer">
                  <span className={`sentiment-badge badge ${getSentimentBadgeClass(article.sentiment)}`}>
                    {getSentimentEmoji(article.sentiment)} {article.sentiment.toUpperCase()}
                  </span>
                  
                  {article.url && (
                    <a 
                      href={article.url} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="news-link"
                      onClick={(e) => e.stopPropagation()}
                    >
                      Read More →
                    </a>
                  )}
                </div>
              </div>

              {article.image && (
                <div 
                  className="news-image"
                  style={{ backgroundImage: `url(${article.image})` }}
                ></div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default NewsPanel;