import React, { useState, useEffect } from 'react';
import { getHistoricalData } from '../../services/stockAPI';
import LineChart from '../Charts/LineChart';
import BarChart from '../Charts/BarChart';
import { formatDate } from '../../utils/formatters';
import './HistoricalData.css';

const HistoricalData = ({ symbol }) => {
  const [historicalData, setHistoricalData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [timeRange, setTimeRange] = useState('daily'); // 'daily', 'weekly', 'monthly'
  const [chartType, setChartType] = useState('price'); // 'price' or 'volume'

  // Fetch historical data
  useEffect(() => {
    const fetchData = async () => {
      if (!symbol) return;

      setIsLoading(true);

      try {
        const data = await getHistoricalData(symbol, timeRange);
        setHistoricalData(data);
      } catch (error) {
        console.error('Error fetching historical data:', error);
        setHistoricalData([]);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, [symbol, timeRange]);

  const handleTimeRangeChange = (range) => {
    setTimeRange(range);
  };

  const handleChartTypeChange = (type) => {
    setChartType(type);
  };

  if (!symbol) {
    return null;
  }

  return (
    <div className="historical-data section-container">
      <div className="section-header">
        <div>
          <h2 className="section-title">📊 Historical Data - {symbol}</h2>
          <p className="section-subtitle">[ TRENDS • PATTERNS • ANALYSIS ]</p>
        </div>
      </div>

      {/* Controls */}
      <div className="historical-controls">
        {/* Time Range Toggle */}
        <div className="control-group">
          <label className="control-label">Time Range:</label>
          <div className="control-buttons">
            <button
              className={`control-btn ${timeRange === 'daily' ? 'active' : ''}`}
              onClick={() => handleTimeRangeChange('daily')}
            >
              Daily
            </button>
            <button
              className={`control-btn ${timeRange === 'weekly' ? 'active' : ''}`}
              onClick={() => handleTimeRangeChange('weekly')}
            >
              Weekly
            </button>
            <button
              className={`control-btn ${timeRange === 'monthly' ? 'active' : ''}`}
              onClick={() => handleTimeRangeChange('monthly')}
            >
              Monthly
            </button>
          </div>
        </div>

        {/* Chart Type Toggle */}
        <div className="control-group">
          <label className="control-label">View:</label>
          <div className="control-buttons">
            <button
              className={`control-btn ${chartType === 'price' ? 'active' : ''}`}
              onClick={() => handleChartTypeChange('price')}
            >
              📈 Price
            </button>
            <button
              className={`control-btn ${chartType === 'volume' ? 'active' : ''}`}
              onClick={() => handleChartTypeChange('volume')}
            >
              📊 Volume
            </button>
          </div>
        </div>
      </div>

      {/* Charts */}
      {isLoading ? (
        <div className="loading-historical">
          <div className="spinner"></div>
          <p>Loading historical data...</p>
        </div>
      ) : historicalData.length === 0 ? (
        <div className="no-historical">
          <div className="no-historical-icon">📉</div>
          <h4>No Historical Data</h4>
          <p>Unable to load data for {symbol}</p>
        </div>
      ) : (
        <div className="charts-container">
          {chartType === 'price' ? (
            <LineChart 
              data={historicalData} 
              dataKey="close" 
              title={`${symbol} Price History (${timeRange})`}
            />
          ) : (
            <BarChart 
              data={historicalData} 
              dataKey="volume" 
              title={`${symbol} Trading Volume (${timeRange})`}
            />
          )}
        </div>
      )}

      {/* Data Summary */}
      {!isLoading && historicalData.length > 0 && (
        <div className="data-summary">
          <div className="summary-item">
            <span className="summary-label">Data Points:</span>
            <span className="summary-value">{historicalData.length}</span>
          </div>
          <div className="summary-item">
            <span className="summary-label">First Date:</span>
            <span className="summary-value">{formatDate(historicalData[0].date)}</span>
          </div>
          <div className="summary-item">
            <span className="summary-label">Last Date:</span>
            <span className="summary-value">{formatDate(historicalData[historicalData.length - 1].date)}</span>
          </div>
        </div>
      )}
    </div>
  );
};

export default HistoricalData;