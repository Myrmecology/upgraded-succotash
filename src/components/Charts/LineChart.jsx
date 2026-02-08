import React from 'react';
import { LineChart as RechartsLineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart } from 'recharts';
import { formatCurrency, formatDate } from '../../utils/formatters';
import './Charts.css';

const LineChart = ({ data, dataKey = 'close', title = 'Price History' }) => {
  // Custom tooltip
  const CustomTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      return (
        <div className="custom-tooltip">
          <p className="tooltip-label">{formatDate(payload[0].payload.date)}</p>
          <p className="tooltip-value">{formatCurrency(payload[0].value)}</p>
        </div>
      );
    }
    return null;
  };

  // Determine if price is trending up or down
  const isUptrend = data && data.length > 1 && 
    data[data.length - 1][dataKey] > data[0][dataKey];

  const lineColor = isUptrend ? '#00ff88' : '#ff0080';
  const gradientId = isUptrend ? 'colorUp' : 'colorDown';

  if (!data || data.length === 0) {
    return (
      <div className="chart-empty">
        <p>No historical data available</p>
      </div>
    );
  }

  return (
    <div className="line-chart-container">
      <h4 className="chart-title">{title}</h4>
      <ResponsiveContainer width="100%" height={300}>
        <AreaChart
          data={data}
          margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
        >
          <defs>
            <linearGradient id="colorUp" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#00ff88" stopOpacity={0.3}/>
              <stop offset="95%" stopColor="#00ff88" stopOpacity={0}/>
            </linearGradient>
            <linearGradient id="colorDown" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#ff0080" stopOpacity={0.3}/>
              <stop offset="95%" stopColor="#ff0080" stopOpacity={0}/>
            </linearGradient>
          </defs>
          <CartesianGrid 
            strokeDasharray="3 3" 
            stroke="rgba(0, 255, 255, 0.1)"
            vertical={false}
          />
          <XAxis 
            dataKey="date" 
            tickFormatter={(date) => {
              const d = new Date(date);
              return `${d.getMonth() + 1}/${d.getDate()}`;
            }}
            stroke="var(--text-muted)"
            style={{
              fontFamily: 'Share Tech Mono, monospace',
              fontSize: '11px'
            }}
            tick={{ fill: 'var(--text-muted)' }}
          />
          <YAxis 
            tickFormatter={(value) => `$${value.toFixed(0)}`}
            stroke="var(--text-muted)"
            style={{
              fontFamily: 'Share Tech Mono, monospace',
              fontSize: '11px'
            }}
            tick={{ fill: 'var(--text-muted)' }}
            domain={['auto', 'auto']}
          />
          <Tooltip content={<CustomTooltip />} />
          <Area
            type="monotone"
            dataKey={dataKey}
            stroke={lineColor}
            strokeWidth={3}
            fill={`url(#${gradientId})`}
            animationBegin={0}
            animationDuration={1000}
            animationEasing="ease-out"
            dot={false}
            activeDot={{ 
              r: 6, 
              fill: lineColor,
              stroke: 'var(--bg-dark-1)',
              strokeWidth: 2,
              style: {
                filter: `drop-shadow(0 0 8px ${lineColor})`
              }
            }}
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
};

export default LineChart;