# MoneyMate Dashboard - Ultimate Edition v9

A comprehensive financial analytics platform built with React, TypeScript, and modern web technologies. MoneyMate provides real-time insights into your financial health, including net worth tracking, credit monitoring, spending analysis, and investment projections.

![MoneyMate Dashboard](https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3)

## ✨ Features

### 🏆 Core Analytics
- **Real-time Net Worth Tracking** - Monitor your complete financial picture
- **Credit Score Monitoring** - Track credit health with visual gauge and alerts
- **Spending Analysis** - Categorized spending patterns with trend analysis
- **Asset Allocation** - Interactive pie charts showing portfolio distribution

### 📊 Advanced Visualizations
- **Credit Score Gauge** - Professional gauge with color-coded health indicators
- **Spending Trends** - Line charts showing monthly spending patterns
- **Category Heatmap** - Visual breakdown of spending by category
- **SIP Projection Charts** - Future value calculations with compound growth

### 🎯 Smart Features
- **What-if Analysis** - Interactive SIP calculator with projection scenarios
- **Sticky KPI Bar** - Always-visible key metrics at the top
- **Alert System** - Intelligent alerts for credit thresholds and financial goals
- **Dark/Light Mode** - Responsive theme switching with system preference detection

### 🔧 Technical Excellence
- **Modern Tech Stack** - React 18, TypeScript, TailwindCSS, Recharts
- **Responsive Design** - Mobile-first approach with tablet and desktop optimization
- **Real-time Data** - Integration with MoneyMate API for live financial data
- **Export Capabilities** - Download reports in Markdown format

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ 
- npm or yarn
- MoneyMate API access (LangFlow integration)

### Installation

1. **Clone and install dependencies:**
```bash
git clone <repository-url>
cd moneymate-dashboard
npm install
```

2. **Environment setup:**
```bash
cp .env.example .env
# Edit .env and add your VITE_LANGFLOW_API_KEY
```

3. **Start development server:**
```bash
npm run dev
```

4. **Open your browser:**
Navigate to `http://localhost:8080`

## 🔑 Environment Configuration

Create a `.env` file in the root directory:

```env
# Required: Your LangFlow API key for MoneyMate integration
VITE_LANGFLOW_API_KEY=your_api_key_here

# Optional: Override default API endpoint
# VITE_LANGFLOW_API_URL=http://localhost:7860/api/v1/run/your-flow-id
```

## 🏗️ Architecture

### Frontend Structure
```
client/
├── components/
│   ├── ui/              # Shadcn/ui components
│   ├── charts/          # Custom chart components
│   ├── DashboardLayout.tsx
│   ├── AuthPage.tsx
│   └── KPIBar.tsx
├── pages/               # Route components
│   ├── Overview.tsx     # Main dashboard
│   ├── Spend.tsx        # Spending analysis
│   ├── Credit.tsx       # Credit monitoring
│   ├── WhatIf.tsx       # Projection calculator
│   └── ...
├── hooks/               # Custom React hooks
├── lib/                 # Utilities and API integration
└── App.tsx             # Root component
```

### Key Components

#### 🎛️ Dashboard Layout
- Responsive sidebar navigation
- Dark mode toggle
- Mobile-friendly header
- Contextual navigation highlighting

#### 📈 Chart Components
- **AssetPieChart** - Portfolio allocation visualization
- **CreditGauge** - Credit score with color-coded ranges
- **SpendLineChart** - Monthly spending trends
- **CategoryHeatmap** - Spending category breakdown
- **ProjectionChart** - SIP growth projections

#### 🔐 Authentication
- Phone number validation with Indian format support
- Session management with localStorage persistence
- Secure API integration with MoneyMate backend

## 🎨 Design System

### Color Palette
- **Primary**: Financial Green (`hsl(142, 71%, 45%)`) - Growth and prosperity
- **Success**: Emerald green for positive metrics
- **Warning**: Amber for attention items
- **Destructive**: Red for alerts and negative values

### Typography
- System fonts with optimized fallbacks
- Consistent sizing scale
- Accessible contrast ratios

### Components
Built on **Radix UI** + **TailwindCSS** for:
- Accessibility-first design
- Consistent component behavior
- Themeable design tokens

## 📱 Pages Overview

### 🏠 Overview (Home)
- Net worth summary with trend indicators
- Asset allocation pie chart
- Quick action buttons for data refresh
- Raw data inspection tabs

### 💳 Credit Health
- Credit score gauge with ranges (300-900)
- Credit improvement tips
- Historical credit data
- Alert system for score changes

### 💰 Spending Analysis
- Monthly spending line chart
- Category-wise breakdown heatmap
- Spending pattern insights
- Budget vs actual comparisons

### 🎯 What-if Calculator
- Interactive SIP amount slider
- Investment duration selector
- Real-time projection calculations
- Multiple scenario comparisons

### 💬 Chat Interface
- Natural language queries to MoneyMate
- Contextual financial advice
- Preset question templates
- Response history

### 📄 Report Export
- Comprehensive financial report generation
- Markdown format download
- Data completeness indicators
- Executive summary generation

## 🔌 API Integration

### MoneyMate Backend
The dashboard integrates with MoneyMate's LangFlow API for:
- User authentication via phone number
- Real-time financial data fetching
- Natural language processing for chat
- Automated financial insights

### Data Flow
1. **Authentication** - Phone number validation and session creation
2. **Data Fetching** - Goal-based API calls for specific financial data
3. **Processing** - Client-side parsing and visualization
4. **Updates** - Real-time refresh capabilities

## 🛠️ Development

### Available Scripts
```bash
npm run dev          # Start development server
npm run build        # Production build
npm run start        # Start production server
npm run typecheck    # TypeScript validation
npm test            # Run test suite
npm run format.fix  # Format code with Prettier
```

### Development Workflow
1. **Component Development** - Create in `client/components/`
2. **Page Creation** - Add routes in `client/pages/`
3. **Styling** - Use TailwindCSS classes with design tokens
4. **Type Safety** - Ensure TypeScript compliance
5. **Testing** - Add Vitest tests for critical functionality

### Code Standards
- **TypeScript** - Strict type checking enabled
- **ESLint + Prettier** - Consistent code formatting
- **Component Composition** - Reusable, accessible components
- **Custom Hooks** - Logic separation and reusability

## 🚀 Deployment

### Production Build
```bash
npm run build
npm run start
```

### Netlify Deployment (Recommended)
The project is pre-configured for Netlify deployment:
1. Connect your repository to Netlify
2. Set environment variables in Netlify dashboard
3. Deploy automatically on push to main branch

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is private and proprietary. All rights reserved.

## 🆘 Support

For technical support or questions:
- Check the [documentation](./docs/)
- Review existing [issues](https://github.com/your-org/moneymate-dashboard/issues)
- Contact the development team

---

**MoneyMate Dashboard - Ultimate Edition v9**  
*Your complete financial command center* 🏆
