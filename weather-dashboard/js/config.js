/**
 * Configuration file for Weather Dashboard
 * All constants, API endpoints, and default values
 */

// API Endpoints
export const API_ENDPOINTS = {
  geocoding: 'https://geocoding-api.open-meteo.com/v1/search',
  weather: 'https://api.open-meteo.com/v1/forecast'
};

// Weather parameters to fetch from Open-Meteo API
export const WEATHER_PARAMS = {
  current: [
    'temperature_2m',
    'relative_humidity_2m',
    'wind_speed_10m',
    'weather_code',
    'is_day'
  ],
  hourly: [
    'temperature_2m',
    'precipitation_probability',
    'weather_code'
  ]
};

// Default values
export const DEFAULTS = {
  city: 'London',
  forecastHours: 24,
  timezone: 'auto'
};

// UI Constants
export const UI = {
  searchDebounceMs: 500,
  loadingDelay: 300,
  chartColors: {
    temperature: 'rgb(255, 99, 132)',
    precipitation: 'rgb(54, 162, 235)'
  }
};

// Error messages
export const ERROR_MESSAGES = {
  cityNotFound: 'City not found. Please try another search.',
  weatherFetchFailed: 'Unable to fetch weather data. Please try again.',
  networkError: 'Network error. Please check your connection.',
  invalidInput: 'Please enter a valid city name.'
};