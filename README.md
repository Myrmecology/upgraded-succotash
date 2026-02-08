# 📈 Interactive Stock Market Dashboard

A retro-futuristic stock market dashboard with real-time data, portfolio tracking, cryptocurrency prices, and wild 90s sci-fi aesthetics!

![Stock Dashboard](https://img.shields.io/badge/React-18.2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🌟 Features

### Core Trading Features
- ✅ **Virtual Portfolio** - Start with $100,000 virtual cash
- ✅ **Buy/Sell Stocks** - Execute trades with real-time prices
- ✅ **Portfolio Tracking** - Monitor holdings, gains/losses, and allocation
- ✅ **Watchlist** - Track your favorite stocks
- ✅ **Stock Search** - Find stocks by symbol or company name

### Data & Analytics
- 📊 **Real-Time Prices** - Live stock quotes that update every 10-15 seconds
- 📈 **Historical Charts** - Line and bar charts for price and volume analysis
- 🏢 **Company Information** - Fundamentals, P/E ratios, market cap, and more
- 📰 **Financial News** - Latest headlines with sentiment analysis
- 🪙 **Cryptocurrency** - Track Bitcoin, Ethereum, and other digital assets

### Visual Features
- 🎨 **Retro-Futuristic Design** - 90s sci-fi aesthetics with neon colors
- 🌈 **Wild CSS Animations** - Morphing buttons, glowing effects, sparkles
- 🌓 **Dark/Light Themes** - Switch between themes with animated toggle
- 📺 **Scrolling Ticker** - CNN-style stock ticker at the top
- ⚡ **3D Effects** - Card tilts, shadows, and depth

## 🚀 Installation

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Steps

1. **Clone or navigate to your repository**
```bash
cd your-repo-name
```

2. **Install dependencies**
```bash
npm install
```

3. **Set up API keys** (see API Setup section below)

4. **Start the development server**
```bash
npm start
```

5. **Open your browser**
```
http://localhost:3000
```

## 🔑 API Setup

This project uses multiple APIs for stock data, news, and cryptocurrency prices.

### Required APIs

1. **Alpha Vantage** (Stock Data & Historical Prices)
   - Sign up: https://www.alphavantage.co/support/#api-key
   - Free tier: 25 requests/day

2. **Finnhub** (Real-time Stock Quotes & Company Info)
   - Sign up: https://finnhub.io/register
   - Free tier: 60 calls/minute

3. **News API** (Financial News Headlines)
   - Sign up: https://newsapi.org/register
   - Free tier: 100 requests/day

4. **CoinGecko** (Cryptocurrency Prices)
   - **NO API KEY REQUIRED!** ✅
   - Free tier with no authentication

### Setting Up Your API Keys

1. Create a `.env` file in the root directory:
```bash
cp .env.example .env
```

2. Open `.env` and add your API keys:
```env
REACT_APP_ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
REACT_APP_FINNHUB_API_KEY=your_finnhub_key_here
REACT_APP_NEWS_API_KEY=your_news_api_key_here
```

3. Save the file and restart the development server

**⚠️ Important Notes:**
- The `.env` file is in `.gitignore` and will NOT be committed
- Never share your API keys publicly
- If APIs fail, the app will use mock data automatically
- Rate limits apply to free tiers - be mindful of usage

## 📁 Project Structure
```
interactive-stock-dashboard/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Charts/          # Pie, Line, Bar charts
│   │   ├── CompanyInfo/     # Company fundamentals
│   │   ├── CryptoPanel/     # Cryptocurrency tracking
│   │   ├── Dashboard/       # Buy/Sell trading terminal
│   │   ├── HistoricalData/  # Historical price charts
│   │   ├── NewsPanel/       # Financial news feed
│   │   ├── Portfolio/       # Portfolio overview
│   │   ├── StockSearch/     # Stock search bar
│   │   ├── StockTicker/     # Scrolling ticker
│   │   ├── ThemeToggle/     # Dark/Light mode toggle
│   │   └── Watchlist/       # Stock watchlist
│   ├── services/
│   │   ├── stockAPI.js      # Stock data API calls
│   │   ├── newsAPI.js       # News API calls
│   │   ├── cryptoAPI.js     # Crypto API calls
│   │   └── sentimentAPI.js  # Sentiment analysis
│   ├── utils/
│   │   ├── calculations.js  # Portfolio calculations
│   │   ├── formatters.js    # Number/date formatting
│   │   └── localStorage.js  # Local storage utilities
│   ├── styles/
│   │   ├── App.css          # Main app styles
│   │   ├── animations.css   # Wild animations
│   │   ├── themes.css       # Theme management
│   │   └── variables.css    # CSS variables
│   ├── App.jsx              # Main app component
│   ├── index.js             # React entry point
│   └── index.css            # Global styles
├── .env.example             # API key template
├── .gitignore               # Git ignore rules
├── package.json             # Dependencies
└── README.md                # You are here!
```

## 🛠️ Technologies Used

- **React 18.2** - UI framework
- **Recharts** - Chart library
- **Axios** - HTTP client
- **Framer Motion** - Animations
- **date-fns** - Date formatting
- **React Tooltip** - Interactive tooltips

## 🎨 Design Philosophy

This dashboard embraces a **retro-futuristic aesthetic** inspired by:
- 90s sci-fi interfaces
- Neon cyberpunk visuals
- CRT monitor effects
- Terminal/hacker aesthetics

### Key Design Elements
- 🌈 **Neon color palette** - Cyan, magenta, green, pink
- ✨ **Glowing effects** - Text shadows, box shadows
- 🔄 **Morphing animations** - Buttons that transform on hover
- 📺 **Scan lines** - CRT-style visual effects
- ⭐ **Particle effects** - Stars and sparkles on interactions

## 💾 Data Persistence

- **Portfolio data** is saved to localStorage
- **Watchlist** persists between sessions
- **Theme preference** is remembered
- **Trade history** is maintained locally

## 🔐 Security

- API keys stored in `.env` (NOT committed to git)
- Comprehensive `.gitignore` with YubiKey security
- Environment variables used throughout
- No sensitive data exposed in client code

## 📱 Responsive Design

The dashboard is fully responsive and works on:
- 💻 Desktop (1920px+)
- 💻 Laptop (1200px - 1920px)
- 📱 Tablet (768px - 1200px)
- 📱 Mobile (320px - 768px)

## 🐛 Known Limitations

- **Free API tiers** have rate limits
- **Mock data fallbacks** when APIs fail
- **No real money** - this is a simulation!
- **Simplified tax calculations**
- **No after-hours trading data**

## 🚀 Future Enhancements

Potential features for future versions:
- [ ] Options trading simulation
- [ ] Advanced charting (candlesticks, indicators)
- [ ] Social features (leaderboards)
- [ ] AI-powered trade suggestions
- [ ] Export portfolio reports
- [ ] Multi-currency support
- [ ] Futures and commodities

## 📝 License

MIT License - feel free to use this project however you'd like!

## 🙏 Acknowledgments

- Alpha Vantage for stock data
- Finnhub for real-time quotes
- NewsAPI for financial news
- CoinGecko for crypto data
- Recharts for beautiful charts

## 🎮 Have Fun Trading!

Remember: This is a simulation with virtual money. Use it to:
- Learn about stock trading
- Test investment strategies
- Explore market data
- Enjoy the retro aesthetics

**Happy Trading! 📈🚀**