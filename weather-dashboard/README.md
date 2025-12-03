# Weather Dashboard

> Real-time weather information dashboard built as part of Aeron Systems AI Prototyping Intern Assignment

![Weather Dashboard](https://img.shields.io/badge/Status-Complete-success)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow)
![HTML5](https://img.shields.io/badge/HTML5-CSS3-blue)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [AI Tools & Methodology](#ai-tools--methodology)
- [Manual Changes](#manual-changes)
- [Development Process](#development-process)
- [API Documentation](#api-documentation)
- [Browser Compatibility](#browser-compatibility)
- [Known Issues](#known-issues)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 🌟 Overview

Weather Dashboard is a responsive web application that provides real-time weather information for any city worldwide. Built using modern JavaScript ES6+ modules, the application fetches data from Open-Meteo's free weather API and displays current conditions along with 24-hour forecasts through interactive charts.

### What This Program Does

1. **City Search**: Search for any city worldwide by name
2. **Real-time Weather**: Display current temperature, humidity, and wind speed
3. **Weather Icons**: Visual representation of weather conditions with emojis
4. **24-Hour Forecast**: Interactive temperature trend chart
5. **Precipitation Probability**: Bar chart showing rain chances
6. **Quick Access**: Popular cities buttons for instant weather lookup
7. **Auto-load**: Automatically loads default city on page load
8. **Error Handling**: User-friendly error messages with auto-dismiss
9. **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

---

## ✨ Features

### Core Features
- ✅ **City Search with Geocoding** - Search any city using Open-Meteo Geocoding API
- ✅ **Current Weather Display** - Temperature, humidity, wind speed, weather description
- ✅ **Weather Icons** - Dynamic weather icons based on WMO weather codes
- ✅ **24-Hour Temperature Chart** - Line chart showing temperature trends
- ✅ **Precipitation Probability Chart** - Bar chart showing rain chances
- ✅ **Popular Cities Quick Access** - One-click buttons for major cities
- ✅ **Auto-load Default City** - Loads London by default on startup
- ✅ **Loading States** - Visual feedback during data fetching
- ✅ **Error Handling** - Clear error messages with auto-dismiss after 5 seconds
- ✅ **Responsive Design** - Mobile-first, works on all screen sizes

### Technical Features
- ✅ **Modular Architecture** - Clean separation of concerns (services, components, utils)
- ✅ **Logger Utility** - Configurable logging system with DEV_MODE toggle
- ✅ **ES6 Modules** - Modern JavaScript with import/export
- ✅ **Async/Await** - Clean asynchronous code
- ✅ **Chart.js Integration** - Professional data visualization
- ✅ **CSS Variables** - Consistent theming and easy customization
- ✅ **No Backend Required** - Pure frontend, runs directly in browser


## 📸 Screenshots


### Desktop View

![Screenshot 1](screenshots/1.png)
![Screenshot 2](screenshots/2.png)


## 🚀 Installation

### Prerequisites

- **Web Browser**: Modern browser with JavaScript enabled
  - Chrome 90+
  - Firefox 88+
  - Safari 14+
  - Edge 90+
- **Internet Connection**: Required for API calls
- **Local Web Server** (optional but recommended):
  - Python: `python -m http.server 8000`
  - Node.js: `npx http-server`
  - VS Code: Live Server extension

### Quick Start

#### Option 1: Direct File Opening
```bash
# 1. Clone the repository
git clone https://github.com/G-karthick0501/aeron-assignment.git
cd aeron-assignment/weather-dashboard

# 2. Open in browser
# Double-click index.html
# OR right-click → Open with → Your Browser
```

#### Option 2: Using Local Server (Recommended)
```bash
# Using Python
cd weather-dashboard
python -m http.server 8000
# Open http://localhost:8000 in browser

# Using Node.js
npx http-server weather-dashboard
# Open http://localhost:8080 in browser

# Using VS Code Live Server
# Right-click index.html → Open with Live Server
```

### No Dependencies to Install!
This project runs entirely in the browser with no build process or npm packages required. All dependencies (Chart.js) are loaded via CDN.

---

## 📖 Usage

### Basic Usage

1. **Launch the Application**
   - Open `index.html` in your web browser
   - The app will automatically load weather for London

2. **Search for a City**
   - Type a city name in the search box
   - Press Enter or click "Search" button
   - Weather data will load automatically

3. **Use Popular Cities**
   - Click any city button (London, New York, Tokyo, etc.)
   - Weather loads instantly without typing

4. **View Weather Data**
   - Current conditions displayed at the top
   - Temperature trend shown in line chart
   - Rain probability shown in bar chart

### Keyboard Shortcuts
- **Enter** - Submit search when input is focused
- **Tab** - Navigate between elements

### Troubleshooting

**"City not found" error:**
- Check spelling
- Try adding country name (e.g., "Paris, France")
- Use major city names

**Charts not displaying:**
- Check internet connection (Chart.js loads from CDN)
- Clear browser cache
- Check browser console (F12) for errors

**No data loading:**
- Verify internet connection
- Check if Open-Meteo API is accessible
- Check browser console for network errors

---

## 📁 Project Structure

```
weather-dashboard/
├── index.html                 # Main HTML file
├── README.md                  # This file
├── css/
│   ├── variables.css          # CSS variables (colors, spacing, fonts)
│   ├── layout.css             # Layout styles (grid, responsive)
│   └── components.css         # Component styles (buttons, cards)
├── js/
│   ├── app.js                 # Main application entry point
│   ├── config.js              # Configuration (API endpoints, constants)
│   ├── utils/
│   │   ├── formatter.js       # Data formatting utilities
│   │   └── logger.js          # Logging utility with DEV_MODE toggle
│   ├── services/
│   │   ├── geocoding.js       # Geocoding API service
│   │   └── weather.js         # Weather API service
│   └── components/
│       ├── currentWeather.js  # Current weather display component
│       └── charts.js          # Chart rendering component
└── .gitignore                 # Git ignore file
```

### Architecture Overview

```
┌─────────────────────────────────────────────┐
│                  app.js                     │
│         (Application Orchestrator)          │
└──────────────────┬──────────────────────────┘
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
   ┌────────┐ ┌────────┐ ┌────────┐
   │Services│ │Components│ │Utils  │
   └────────┘ └────────┘ └────────┘
        │          │          │
        ▼          ▼          ▼
   Geocoding  Current     Formatter
   Weather    Weather     Logger
              Charts
```

---

## 🛠️ Technologies Used

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with Grid and Flexbox
- **JavaScript ES6+** - Modern JavaScript with modules
- **Chart.js 4.4.0** - Data visualization library (CDN)

### APIs
- **Open-Meteo Geocoding API** - City name to coordinates conversion
  - https://geocoding-api.open-meteo.com/v1/search
  - No API key required
  - Rate limit: Generous free tier

- **Open-Meteo Weather API** - Weather data
  - https://api.open-meteo.com/v1/forecast
  - No API key required
  - Updates: Hourly
  - Data: Temperature, humidity, wind, precipitation

### Development Tools
- **Git** - Version control
- **GitHub** - Repository hosting
- **VS Code** - Code editor
- **Chrome DevTools** - Debugging

---

## 🤖 AI Tools & Methodology

### AI Tools Used

**Primary Tool: Claude AI (Anthropic)**
- Model: Claude 3.5 Sonnet
- Usage: Code generation, architecture planning, debugging assistance
- Access: Free tier via Claude.ai

**Workflow:**
1. Discussed requirements and architecture with AI
2. AI generated base code for each module
3. Tested and debugged with AI assistance
4. Made manual refinements where needed
5. AI helped with documentation and optimization

### Key AI Prompts Used

#### Initial Setup
```
"Create a weather dashboard project structure with HTML, CSS, and JavaScript. 
Use modular ES6 architecture with services, components, and utilities folders. 
No build process, pure vanilla JavaScript."
```

#### Geocoding Service
```
"Create a geocoding service for Open-Meteo API that converts city names to 
coordinates. Include error handling for invalid cities and network errors. 
Export as ES6 module."
```

#### Weather Service
```
"Create a weather service that fetches weather data from Open-Meteo API. 
Include current weather and 24-hour forecast. Parse the response and return 
structured data with temperature, humidity, wind speed, and weather codes."
```

#### Chart Integration
```
"Create a charts component using Chart.js to display temperature line chart 
and precipitation bar chart. Destroy existing charts before creating new ones 
to prevent memory leaks."
```

#### Logger Utility
```
"Create a logger utility with debug, info, success, warn, and error methods. 
Include a DEV_MODE flag to toggle verbose logging. Debug logs only show in 
development mode, errors always show."
```

#### CSS Styling
```
"Create CSS with design tokens (variables) for colors, spacing, and typography. 
Include responsive layout using CSS Grid, and component styles for buttons, 
cards, and loading states. Add dark mode support."
```

---

## ✍️ Manual Changes & Refinements

### What AI Generated vs. What I Changed

#### 1. **Chart Sizing Issue** ✅
**AI Generated:** Charts kept growing on resize
**Manual Fix:** Added fixed height wrapper
```css
.chart-wrapper {
  position: relative;
  height: 300px;
  width: 100%;
  overflow: hidden;
}
```

#### 2. **Popular Cities Feature** ✅
**AI Generated:** Basic city search only
**Manual Addition:** Added popular cities quick access buttons with event delegation

#### 3. **Logger Integration** ✅
**AI Generated:** Used console.log directly
**Manual Refactoring:** Created logger utility and replaced all console.log calls with logger.debug()

#### 4. **Error Auto-Dismiss** ✅
**AI Generated:** Errors stayed visible
**Manual Addition:** Added 5-second auto-dismiss timer

#### 5. **Default City Loading** ✅
**AI Generated:** Empty state on load
**Manual Addition:** Auto-loads London on startup

#### 6. **Weather Icon Logic** ✅
**AI Generated:** Basic icon mapping
**Manual Enhancement:** Added day/night icons based on isDay parameter

#### 7. **CSS Variables Organization** ✅
**AI Generated:** Mixed CSS
**Manual Refactoring:** Separated into variables.css, layout.css, components.css

#### 8. **Loading State Management** ✅
**AI Generated:** Basic loading indicator
**Manual Enhancement:** Added button state changes and text updates

---

## 🔄 Development Process

### Phase 1: Planning & Setup (30 mins)
- Discussed requirements with AI
- Designed modular architecture
- Created project structure
- Set up HTML skeleton

### Phase 2: API Integration (1 hour)
- Implemented geocoding service
- Implemented weather service
- Tested API endpoints
- Added error handling

### Phase 3: UI Components (1.5 hours)
- Created current weather display
- Integrated Chart.js
- Implemented temperature chart
- Implemented precipitation chart
- Fixed chart sizing issues

### Phase 4: Features & Polish (1 hour)
- Added popular cities
- Implemented logger utility
- Added loading states
- Implemented error handling
- Added default city auto-load

### Phase 5: Styling & Responsive (1 hour)
- Created CSS variables
- Implemented responsive layout
- Added component styles
- Tested on mobile devices

### Phase 6: Testing & Documentation (30 mins)
- Cross-browser testing
- Created README
- Documented AI usage
- Recorded demo video

**Total Development Time:** ~5-6 hours

---

## 📚 API Documentation

### Open-Meteo Geocoding API

**Endpoint:** `https://geocoding-api.open-meteo.com/v1/search`

**Parameters:**
- `name` (required): City name to search
- `count` (optional): Number of results (default: 1)
- `language` (optional): Response language (default: en)
- `format` (optional): Response format (json)

**Example Request:**
```javascript
fetch('https://geocoding-api.open-meteo.com/v1/search?name=London&count=1&language=en&format=json')
```

**Example Response:**
```json
{
  "results": [{
    "latitude": 51.5074,
    "longitude": -0.1278,
    "name": "London",
    "country": "United Kingdom",
    "timezone": "Europe/London"
  }]
}
```

### Open-Meteo Weather API

**Endpoint:** `https://api.open-meteo.com/v1/forecast`

**Parameters:**
- `latitude` (required): Latitude coordinate
- `longitude` (required): Longitude coordinate
- `current` (optional): Current weather variables
- `hourly` (optional): Hourly forecast variables
- `timezone` (optional): Timezone (auto, UTC, or specific)

**Example Request:**
```javascript
fetch('https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&hourly=temperature_2m,precipitation_probability&timezone=auto')
```

---

## 🌐 Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 90+ | ✅ Fully Supported |
| Firefox | 88+ | ✅ Fully Supported |
| Safari | 14+ | ✅ Fully Supported |
| Edge | 90+ | ✅ Fully Supported |
| Opera | 76+ | ✅ Fully Supported |
| Mobile Chrome | Latest | ✅ Fully Supported |
| Mobile Safari | Latest | ✅ Fully Supported |

**Requirements:**
- ES6 Modules support
- Fetch API support
- CSS Grid support
- CSS Variables support

---

## ⚠️ Known Issues

1. **CORS in File Protocol**
   - Opening `index.html` directly (file://) may cause CORS issues
   - **Solution:** Use a local web server

2. **Chart.js CDN Dependency**
   - Requires internet connection to load Chart.js
   - **Solution:** Charts won't display if offline

3. **API Rate Limiting**
   - Open-Meteo has rate limits (though generous)
   - **Solution:** Normal usage won't hit limits

4. **Browser Console Logs**
   - Debug logs visible when DEV_MODE = true
   - **Solution:** Set DEV_MODE = false in logger.js for production

---

## 🚀 Future Enhancements

### Planned Features
- [ ] **Geolocation** - Detect user's location automatically
- [ ] **Search History** - Remember recently searched cities
- [ ] **Favorites** - Save favorite cities
- [ ] **Unit Toggle** - Switch between Celsius/Fahrenheit
- [ ] **Dark Mode** - Toggle dark/light theme
- [ ] **5-Day Forecast** - Extended forecast view
- [ ] **Weather Alerts** - Display severe weather warnings
- [ ] **PWA Support** - Make it installable as an app
- [ ] **Offline Mode** - Cache last viewed weather
- [ ] **Share Feature** - Share weather via social media

### Technical Improvements
- [ ] Add service worker for offline support
- [ ] Implement localStorage for caching
- [ ] Add unit tests
- [ ] Add end-to-end tests
- [ ] Optimize bundle size
- [ ] Add TypeScript types
- [ ] Implement autocomplete suggestions
- [ ] Add loading skeletons

---

## 📄 License

This project was created as part of the Aeron Systems AI Prototyping Intern Assignment.

**Assignment Purpose:** Educational and evaluation purposes only.

**APIs Used:**
- Open-Meteo API: [CC BY 4.0 License](https://open-meteo.com/en/license)
- Chart.js: [MIT License](https://github.com/chartjs/Chart.js/blob/master/LICENSE.md)

---

## 👤 Author

**Karthick G**
- GitHub: [@G-karthick0501](https://github.com/G-karthick0501)
- Assignment: Aeron Systems AI Prototyping Intern
- Date: November 2024

---

## 🙏 Acknowledgments

- **Open-Meteo** - For providing free weather API
- **Chart.js** - For excellent charting library
- **Claude AI** - For AI-assisted development
- **Aeron Systems** - For the opportunity

---

## 📞 Support

For questions or issues with this assignment submission:
- Create an issue on GitHub
- Contact: [Your Email]
- Assignment Reference: Aeron Systems AI Intern - Part 1

---

**Made with ❤️ using AI-assisted development**

*This project demonstrates the effective use of AI tools for rapid prototyping while maintaining code quality and understanding.*