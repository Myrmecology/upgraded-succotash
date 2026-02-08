import React from 'react';
import { BarChart as RechartsBarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';
import { formatLargeNumber, formatDate } from '../../utils/formatters';
import './Charts.css';

const BarChart = ({ data, dataKey = 'volume', title = 'Volume' }) => {
  // Custom tooltip
  const CustomTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      return (
        <div className="custom-tooltip">
          <p className="tooltip-label">{payload[0].payload.date ? formatDate(payload[0].payload.date) : payload[0].payload.name}</p>
          <p className="tooltip-value">{formatLargeNumber(payload[0].value)}</p>
        </div>
      );
    }
    return null;
  };

  // Color gradient for bars
  const COLORS = [
    '#00ffff', // Cyan
    '#00ff88', // Green
    '#ff00ff', // Magenta
    '#ffff00', // Yellow
    '#ff0080', // Pink
    '#0080ff', // Blue
    '#ff8800', // Orange
    '#b000ff', // Purple
  ];

  if (!data || data.length === 0) {
    return (
      <div className="chart-empty">
        <p>No volume data available</p>
      </div>
    );
  }

  return (
    <div className="bar-chart-container">
      <h4 className="chart-title">{title}</h4>
      <ResponsiveContainer width="100%" height={300}>
        <RechartsBarChart
          data={data}
          margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
        >
          <defs>
            <linearGradient id="barGradient" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#00ffff" stopOpacity={0.8}/>
              <stop offset="100%" stopColor="#00ff88" stopOpacity={0.3}/>
            </linearGradient>
          </defs>
          <CartesianGrid 
            strokeDasharray="3 3" 
            stroke="rgba(0, 255, 255, 0.1)"
            vertical={false}
          />
          <XAxis 
            dataKey={data[0]?.date ? 'date' : 'name'}
            tickFormatter={(value) => {
              if (data[0]?.date) {
                const d = new Date(value);
                return `${d.getMonth() + 1}/${d.getDate()}`;
              }
              return value;
            }}
            stroke="var(--text-muted)"
            style={{
              fontFamily: 'Share Tech Mono, monospace',
              fontSize: '11px'
            }}
            tick={{ fill: 'var(--text-muted)' }}
          />
          <YAxis 
            tickFormatter={(value) => formatLargeNumber(value)}
            stroke="var(--text-muted)"
            style={{
              fontFamily: 'Share Tech Mono, monospace',
              fontSize: '11px'
            }}
            tick={{ fill: 'var(--text-muted)' }}
          />
          <Tooltip content={<CustomTooltip />} />
          <Bar 
            dataKey={dataKey}
            fill="url(#barGradient)"
            radius={[8, 8, 0, 0]}
            animationBegin={0}
            animationDuration={1000}
            animationEasing="ease-out"
          >
            {data.map((entry, index) => (
              <Cell 
                key={`cell-${index}`}
                fill={COLORS[index % COLORS.length]}
                style={{
                  filter: `drop-shadow(0 0 8px ${COLORS[index % COLORS.length]})`
                }}
              />
            ))}
          </Bar>
        </RechartsBarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default BarChart;