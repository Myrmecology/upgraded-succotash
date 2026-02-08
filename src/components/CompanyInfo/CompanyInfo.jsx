import React, { useState, useEffect } from 'react';
import { getCompanyProfile, getStockFundamentals } from '../../services/stockAPI';
import { formatCurrency, formatLargeNumber } from '../../utils/formatters';
import './CompanyInfo.css';

const CompanyInfo = ({ symbol }) => {
  const [profile, setProfile] = useState(null);
  const [fundamentals, setFundamentals] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  // Fetch company info
  useEffect(() => {
    const fetchCompanyInfo = async () => {
      if (!symbol) return;

      setIsLoading(true);

      try {
        const [profileData, fundamentalsData] = await Promise.all([
          getCompanyProfile(symbol),
          getStockFundamentals(symbol)
        ]);

        setProfile(profileData);
        setFundamentals(fundamentalsData);
      } catch (error) {
        console.error('Error fetching company info:', error);
        setProfile(null);
        setFundamentals(null);
      } finally {
        setIsLoading(false);
      }
    };

    fetchCompanyInfo();
  }, [symbol]);

  if (!symbol) {
    return null;
  }

  return (
    <div className="company-info section-container">
      <div className="section-header">
        <div>
          <h2 className="section-title">🏢 Company Information - {symbol}</h2>
          <p className="section-subtitle">[ PROFILE • FUNDAMENTALS • METRICS ]</p>
        </div>
      </div>

      {isLoading ? (
        <div className="loading-company">
          <div className="spinner"></div>
          <p>Loading company information...</p>
        </div>
      ) : !profile ? (
        <div className="no-company">
          <div className="no-company-icon">🏢</div>
          <h4>No Company Data</h4>
          <p>Unable to load information for {symbol}</p>
        </div>
      ) : (
        <div className="company-content">
          {/* Company Header */}
          <div className="company-header">
            {profile.logo && (
              <div className="company-logo-wrapper">
                <img src={profile.logo} alt={`${profile.name} logo`} className="company-logo" />
              </div>
            )}
            <div className="company-title-section">
              <h3 className="company-name">{profile.name}</h3>
              <div className="company-meta">
                <span className="meta-item">{profile.exchange}</span>
                <span className="meta-separator">•</span>
                <span className="meta-item">{profile.country}</span>
                <span className="meta-separator">•</span>
                <span className="meta-item">{profile.industry}</span>
              </div>
              {profile.weburl && (
                <a 
                  href={profile.weburl} 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="company-website"
                >
                  🌐 Visit Website →
                </a>
              )}
            </div>
          </div>

          {/* Fundamentals Grid */}
          {fundamentals && (
            <div className="fundamentals-grid">
              <div className="fundamental-card">
                <span className="fundamental-label">Market Cap</span>
                <span className="fundamental-value">
                  {profile.marketCap ? formatLargeNumber(profile.marketCap) : 'N/A'}
                </span>
              </div>

              <div className="fundamental-card">
                <span className="fundamental-label">P/E Ratio</span>
                <span className="fundamental-value">
                  {fundamentals.peRatio ? fundamentals.peRatio.toFixed(2) : 'N/A'}
                </span>
              </div>

              <div className="fundamental-card">
                <span className="fundamental-label">EPS</span>
                <span className="fundamental-value">
                  {fundamentals.eps ? formatCurrency(fundamentals.eps) : 'N/A'}
                </span>
              </div>

              <div className="fundamental-card">
                <span className="fundamental-label">Beta</span>
                <span className="fundamental-value">
                  {fundamentals.beta ? fundamentals.beta.toFixed(2) : 'N/A'}
                </span>
              </div>

              <div className="fundamental-card">
                <span className="fundamental-label">52W High</span>
                <span className="fundamental-value">
                  {fundamentals.week52High ? formatCurrency(fundamentals.week52High) : 'N/A'}
                </span>
              </div>

              <div className="fundamental-card">
                <span className="fundamental-label">52W Low</span>
                <span className="fundamental-value">
                  {fundamentals.week52Low ? formatCurrency(fundamentals.week52Low) : 'N/A'}
                </span>
              </div>

              <div className="fundamental-card">
                <span className="fundamental-label">Dividend Yield</span>
                <span className="fundamental-value">
                  {fundamentals.dividendYield ? `${fundamentals.dividendYield.toFixed(2)}%` : 'N/A'}
                </span>
              </div>

              <div className="fundamental-card">
                <span className="fundamental-label">Shares Outstanding</span>
                <span className="fundamental-value">
                  {profile.shareOutstanding ? formatLargeNumber(profile.shareOutstanding) : 'N/A'}
                </span>
              </div>
            </div>
          )}

          {/* Additional Info */}
          <div className="additional-info">
            {profile.phone && (
              <div className="info-item">
                <span className="info-icon">📞</span>
                <span className="info-text">{profile.phone}</span>
              </div>
            )}
            {profile.currency && (
              <div className="info-item">
                <span className="info-icon">💱</span>
                <span className="info-text">Currency: {profile.currency}</span>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default CompanyInfo;