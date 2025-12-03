/**
 * Weather Service
 * Fetches weather data from Open-Meteo Weather API
 */

import { API_ENDPOINTS, WEATHER_PARAMS, ERROR_MESSAGES } from '../config.js';
import { logger } from '../utils/logger.js';

/**
 * Get weather data for given coordinates
 * @param {Object} coords - Coordinates object
 * @param {number} coords.latitude - Latitude
 * @param {number} coords.longitude - Longitude
 * @param {string} coords.timezone - Timezone (optional, default: 'auto')
 * @returns {Promise<Object>} - Weather data object
 */
export async function getWeatherData(coords) {
  // Validate input
  if (!coords || typeof coords !== 'object') {
    logger.error('Invalid coordinates object');
    throw new Error('Invalid coordinates provided');
  }

  const { latitude, longitude, timezone = 'auto' } = coords;

  // Validate latitude and longitude
  if (typeof latitude !== 'number' || typeof longitude !== 'number') {
    logger.error('Invalid latitude or longitude');
    throw new Error('Latitude and longitude must be numbers');
  }

  if (latitude < -90 || latitude > 90) {
    logger.error('Latitude out of range');
    throw new Error('Latitude must be between -90 and 90');
  }

  if (longitude < -180 || longitude > 180) {
    logger.error('Longitude out of range');
    throw new Error('Longitude must be between -180 and 180');
  }

  try {
    logger.debug(`🌤️ Fetching weather for coordinates: ${latitude}, ${longitude}`);

    // Build API URL
    const url = new URL(API_ENDPOINTS.weather);
    
    // Add coordinates
    url.searchParams.append('latitude', latitude.toString());
    url.searchParams.append('longitude', longitude.toString());
    
    // Add timezone
    url.searchParams.append('timezone', timezone);
    
    // Add current weather parameters
    url.searchParams.append('current', WEATHER_PARAMS.current.join(','));
    
    // Add hourly weather parameters
    url.searchParams.append('hourly', WEATHER_PARAMS.hourly.join(','));
    
    // Add forecast configuration
    url.searchParams.append('forecast_days', '2');
    url.searchParams.append('forecast_hours', '24');
    
    logger.debug(`📡 API Request: ${url.toString()}`);

    // Make API request
    const response = await fetch(url.toString());

    // Check if request was successful
    if (!response.ok) {
      logger.error(`API request failed with status: ${response.status}`);
      throw new Error(ERROR_MESSAGES.weatherFetchFailed);
    }

    // Parse JSON response
    const data = await response.json();

    logger.debug('📦 Raw API Response:', data);

    // Validate response structure
    if (!data.current || !data.hourly) {
      logger.error('Invalid response structure from API');
      throw new Error('Invalid weather data received');
    }

    // Process and structure the weather data
    const weatherData = {
      location: {
        latitude: data.latitude,
        longitude: data.longitude,
        elevation: data.elevation,
        timezone: data.timezone,
        timezone_abbreviation: data.timezone_abbreviation
      },
      current: {
        temperature: data.current.temperature_2m,
        humidity: data.current.relative_humidity_2m,
        windSpeed: data.current.wind_speed_10m,
        weatherCode: data.current.weather_code,
        isDay: data.current.is_day,
        time: data.current.time
      },
      hourly: {
        time: data.hourly.time.slice(0, 24),
        temperature: data.hourly.temperature_2m.slice(0, 24),
        precipitationProbability: data.hourly.precipitation_probability.slice(0, 24),
        weatherCode: data.hourly.weather_code.slice(0, 24)
      },
      units: {
        temperature: data.current_units?.temperature_2m || '°C',
        humidity: '%',
        windSpeed: data.current_units?.wind_speed_10m || 'km/h',
        precipitation: '%'
      }
    };

    logger.success('Weather data processed successfully');

    return weatherData;

  } catch (error) {
    // Handle different error types
    if (error.message === ERROR_MESSAGES.weatherFetchFailed) {
      throw error;
    } else if (error.name === 'TypeError' || error.message.includes('fetch')) {
      logger.error('Network error:', error);
      throw new Error(ERROR_MESSAGES.networkError);
    } else {
      logger.error('Unexpected error fetching weather:', error);
      throw new Error('Failed to fetch weather data');
    }
  }
}

/**
 * Get weather description from WMO weather code
 * Based on WMO Weather interpretation codes
 * @param {number} code - WMO weather code
 * @param {number} isDay - 1 for day, 0 for night
 * @returns {Object} - Weather description and icon
 */
export function getWeatherDescription(code, isDay = 1) {
  const weatherCodes = {
    0: { description: 'Clear sky', icon: isDay ? '☀️' : '🌙' },
    1: { description: 'Mainly clear', icon: isDay ? '🌤️' : '🌙' },
    2: { description: 'Partly cloudy', icon: '⛅' },
    3: { description: 'Overcast', icon: '☁️' },
    45: { description: 'Foggy', icon: '🌫️' },
    48: { description: 'Depositing rime fog', icon: '🌫️' },
    51: { description: 'Light drizzle', icon: '🌦️' },
    53: { description: 'Moderate drizzle', icon: '🌦️' },
    55: { description: 'Dense drizzle', icon: '🌧️' },
    56: { description: 'Light freezing drizzle', icon: '🌧️' },
    57: { description: 'Dense freezing drizzle', icon: '🌧️' },
    61: { description: 'Slight rain', icon: '🌧️' },
    63: { description: 'Moderate rain', icon: '🌧️' },
    65: { description: 'Heavy rain', icon: '🌧️' },
    66: { description: 'Light freezing rain', icon: '🌧️' },
    67: { description: 'Heavy freezing rain', icon: '🌧️' },
    71: { description: 'Slight snow', icon: '🌨️' },
    73: { description: 'Moderate snow', icon: '🌨️' },
    75: { description: 'Heavy snow', icon: '❄️' },
    77: { description: 'Snow grains', icon: '🌨️' },
    80: { description: 'Slight rain showers', icon: '🌦️' },
    81: { description: 'Moderate rain showers', icon: '🌧️' },
    82: { description: 'Violent rain showers', icon: '⛈️' },
    85: { description: 'Slight snow showers', icon: '🌨️' },
    86: { description: 'Heavy snow showers', icon: '❄️' },
    95: { description: 'Thunderstorm', icon: '⛈️' },
    96: { description: 'Thunderstorm with slight hail', icon: '⛈️' },
    99: { description: 'Thunderstorm with heavy hail', icon: '⛈️' }
  };

  return weatherCodes[code] || { 
    description: 'Unknown', 
    icon: '❓' 
  };
}
