/**
 * Main Application Entry Point
 * Weather Dashboard - Complete Production Version
 */
import { getCityCoordinates } from './services/geocoding.js';
import { getWeatherData } from './services/weather.js';
import { updateCurrentWeather } from './components/currentWeather.js';
import { updateCharts } from './components/charts.js';
import { ERROR_MESSAGES, DEFAULTS } from './config.js';
import { logger } from './utils/logger.js';

// DOM Elements
const elements = {
  citySearch: document.getElementById('citySearch'),
  searchBtn: document.getElementById('searchBtn'),
  searchError: document.getElementById('searchError'),
  loadingIndicator: document.getElementById('loadingIndicator'),
  currentWeather: document.getElementById('currentWeather'),
  temperatureChart: document.getElementById('temperatureChart'),
  precipitationChart: document.getElementById('precipitationChart'),
  popularCities: document.getElementById('popularCities') // Popular cities container
};

// --- Initialization ---

function init() {
  logger.info('🚀 Weather Dashboard Initialized');
  
  // Bind Search Button Click
  if (elements.searchBtn) {
    elements.searchBtn.addEventListener('click', handleSearch);
  }

  // Bind Enter Key in Search Input
  if (elements.citySearch) {
    elements.citySearch.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        handleSearch();
      }
    });
  }

  // Bind Popular Cities Buttons
  if (elements.popularCities) {
    elements.popularCities.addEventListener('click', handlePopularCityClick);
  }

  // Load default city on startup
  loadDefaultCity();
}

// --- Main Search Logic ---

async function handleSearch() {
  const cityName = elements.citySearch.value.trim();
  
  // Validation
  if (!cityName) {
    showError(ERROR_MESSAGES.invalidInput);
    return;
  }

  // UI: Show loading state
  showLoading(true);
  clearError();

  try {
    // Step 1: Get coordinates from city name
    logger.debug(`🔍 Searching for: ${cityName}`);
    const cityData = await getCityCoordinates(cityName);
    
    // Step 2: Get weather data using coordinates
    logger.debug('🌤️ Fetching weather...');
    const weatherData = await getWeatherData({
      latitude: cityData.latitude,
      longitude: cityData.longitude,
      timezone: cityData.timezone
    });

    // Merge city name into weather data
    weatherData.location.name = cityData.name;
    weatherData.location.country = cityData.country;

    // Step 3: Update UI with weather data
    logger.debug('✅ Updating display...');
    updateCurrentWeather(elements.currentWeather, weatherData);
    updateCharts(elements, weatherData);
    
  } catch (error) {
    logger.error('Error:', error.message);
    showError(error.message || 'Something went wrong');
  } finally {
    showLoading(false);
  }
}

// --- Popular Cities Handler ---

function handlePopularCityClick(event) {
  // Check if a popular city button was clicked
  if (event.target.classList.contains('popular-city-btn')) {
    const cityName = event.target.dataset.city;
    logger.debug(`Popular city clicked: ${cityName}`);
    
    // Set the city name in the search input
    elements.citySearch.value = cityName;
    
    // Trigger search
    handleSearch();
  }
}

// --- Load Default City on Startup ---

function loadDefaultCity() {
  // Set default city in input
  elements.citySearch.value = DEFAULTS.city;

  // Load weather after a short delay to let UI render
  setTimeout(() => {
    handleSearch();
  }, 200);
}

// --- UI Helper Functions ---

function showLoading(isLoading) {
  if (isLoading) {
    elements.loadingIndicator.classList.remove('hidden');
    elements.currentWeather.classList.add('hidden');
    elements.searchBtn.disabled = true;
    elements.searchBtn.textContent = 'Searching...';
  } else {
    elements.loadingIndicator.classList.add('hidden');
    elements.currentWeather.classList.remove('hidden');
    elements.searchBtn.disabled = false;
    elements.searchBtn.textContent = 'Search';
  }
}

function showError(message) {
  if (elements.searchError) {
    elements.searchError.textContent = message;
    elements.searchError.style.display = 'block';
    
    // Auto-hide error after 5 seconds
    setTimeout(() => clearError(), 5000);
  }
}

function clearError() {
  if (elements.searchError) {
    elements.searchError.style.display = 'none';
    elements.searchError.textContent = '';
  }
}

// --- Start App ---

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}