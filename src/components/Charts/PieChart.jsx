import React from 'react';
import { PieChart as RechartsPieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { formatCurrency, formatPercent } from '../../utils/formatters';
import './Charts.css';

const PieChart = ({ data }) => {
  // Convert allocation data to chart format
  const chartData = data.map(item => ({
    name: item.symbol,
    value: item.holdingValue,
    allocation: item.allocation
  }));

  // Vibrant retro-futuristic colors
  const COLORS = [
    '#00ffff', // Cyan
    '#00ff88', // Green
    '#ff00ff', // Magenta
    '#ffff00', // Yellow
    '#ff0080', // Pink
    '#0080ff', // Blue
    '#ff8800', // Orange
    '#b000ff', // Purple
    '#00ff00', // Lime
    '#ff0000', // Red
  ];

  // Custom tooltip
  const CustomTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      return (
        <div className="custom-tooltip">
          <p className="tooltip-label">{payload[0].name}</p>
          <p className="tooltip-value">{formatCurrency(payload[0].value)}</p>
          <p className="tooltip-percent">{formatPercent(payload[0].payload.allocation / 100)}</p>
        </div>
      );
    }
    return null;
  };

  // Custom label
  const renderCustomLabel = ({ cx, cy, midAngle, innerRadius, outerRadius, percent }) => {
    const RADIAN = Math.PI / 180;
    const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
    const x = cx + radius * Math.cos(-midAngle * RADIAN);
    const y = cy + radius * Math.sin(-midAngle * RADIAN);

    if (percent < 0.05) return null; // Don't show label if slice is too small

    return (
      <text
        x={x}
        y={y}
        fill="white"
        textAnchor={x > cx ? 'start' : 'end'}
        dominantBaseline="central"
        style={{
          fontSize: '14px',
          fontWeight: 'bold',
          fontFamily: 'Orbitron, sans-serif',
          textShadow: '0 0 10px rgba(0, 0, 0, 0.8)'
        }}
      >
        {`${(percent * 100).toFixed(0)}%`}
      </text>
    );
  };

  if (!data || data.length === 0) {
    return (
      <div className="chart-empty">
        <p>No allocation data available</p>
      </div>
    );
  }

  return (
    <div className="pie-chart-container">
      <ResponsiveContainer width="100%" height={350}>
        <RechartsPieChart>
          <Pie
            data={chartData}
            cx="50%"
            cy="50%"
            labelLine={false}
            label={renderCustomLabel}
            outerRadius={120}
            innerRadius={60}
            fill="#8884d8"
            dataKey="value"
            animationBegin={0}
            animationDuration={800}
            animationEasing="ease-out"
          >
            {chartData.map((entry, index) => (
              <Cell 
                key={`cell-${index}`} 
                fill={COLORS[index % COLORS.length]}
                stroke="var(--bg-dark-1)"
                strokeWidth={2}
                style={{
                  filter: `drop-shadow(0 0 8px ${COLORS[index % COLORS.length]})`
                }}
              />
            ))}
          </Pie>
          <Tooltip content={<CustomTooltip />} />
          <Legend 
            verticalAlign="bottom" 
            height={36}
            iconType="circle"
            wrapperStyle={{
              fontFamily: 'Rajdhani, sans-serif',
              fontSize: '14px',
              fontWeight: '600'
            }}
          />
        </RechartsPieChart>
      </ResponsiveContainer>

      {/* Legend with values */}
      <div className="pie-legend">
        {chartData.map((item, index) => (
          <div key={index} className="legend-item">
            <div 
              className="legend-color" 
              style={{ 
                backgroundColor: COLORS[index % COLORS.length],
                boxShadow: `0 0 10px ${COLORS[index % COLORS.length]}`
              }}
            ></div>
            <span className="legend-symbol">{item.name}</span>
            <span className="legend-value">{formatCurrency(item.value)}</span>
            <span className="legend-percent">({formatPercent(item.allocation / 100)})</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PieChart;