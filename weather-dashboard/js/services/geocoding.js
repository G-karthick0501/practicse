/**
 * Geocoding Service
 * Converts city names to geographic coordinates using Open-Meteo Geocoding API
 */

import { API_ENDPOINTS, ERROR_MESSAGES } from '../config.js';
import { logger } from '../utils/logger.js';

/**
 * Get coordinates for a city name
 * @param {string} cityName - Name of the city to search
 * @returns {Promise<Object|null>} - City data with coordinates or null if not found
 */
export async function getCityCoordinates(cityName) {
  // Validate input
  if (!cityName || typeof cityName !== 'string' || cityName.trim().length === 0) {
    logger.error('Invalid city name provided');
    throw new Error(ERROR_MESSAGES.invalidInput);
  }

  const trimmedCity = cityName.trim();
  
  try {
    logger.debug(`🔍 Searching for city: "${trimmedCity}"`);
    
    // Build API URL
    const url = new URL(API_ENDPOINTS.geocoding);
    url.searchParams.append('name', trimmedCity);
    url.searchParams.append('count', '1');
    url.searchParams.append('language', 'en');
    url.searchParams.append('format', 'json');
    
    logger.debug(`📡 API Request: ${url.toString()}`);
    
    // Make API request
    const response = await fetch(url.toString());
    
    // Check if request was successful
    if (!response.ok) {
      logger.error(`API request failed with status: ${response.status}`);
      throw new Error(ERROR_MESSAGES.networkError);
    }
    
    // Parse JSON response
    const data = await response.json();
    
    logger.debug('📦 API Response:', data);
    
    // Check if results exist
    if (!data.results || data.results.length === 0) {
      logger.warn(`No results found for: "${trimmedCity}"`);
      throw new Error(ERROR_MESSAGES.cityNotFound);
    }
    
    // Extract first result
    const result = data.results[0];
    
    // Validate required fields
    if (!result.latitude || !result.longitude || !result.name) {
      logger.error('Invalid data structure from API');
      throw new Error('Invalid response from geocoding service');
    }
    
    // Build city data object
    const cityData = {
      latitude: result.latitude,
      longitude: result.longitude,
      name: result.name,
      country: result.country || 'Unknown',
      admin1: result.admin1 || '',
      timezone: result.timezone || 'UTC'
    };
    
    logger.success('City found:', cityData.name, cityData.country);
    
    return cityData;
    
  } catch (error) {
    // Handle different error types
    if (error.message === ERROR_MESSAGES.cityNotFound || 
        error.message === ERROR_MESSAGES.invalidInput) {
      throw error;
    } else if (error.name === 'TypeError' || error.message.includes('fetch')) {
      logger.error('Network error:', error);
      throw new Error(ERROR_MESSAGES.networkError);
    } else {
      logger.error('Unexpected error in geocoding:', error);
      throw new Error('Failed to get city coordinates');
    }
  }
}

/**
 * Search multiple cities (for autocomplete feature)
 * @param {string} searchTerm - Search term
 * @param {number} count - Number of results to return (default: 5)
 * @returns {Promise<Array>} - Array of city objects
 */
export async function searchCities(searchTerm, count = 5) {
  if (!searchTerm || searchTerm.trim().length < 2) {
    return [];
  }
  
  try {
    const url = new URL(API_ENDPOINTS.geocoding);
    url.searchParams.append('name', searchTerm.trim());
    url.searchParams.append('count', count.toString());
    url.searchParams.append('language', 'en');
    url.searchParams.append('format', 'json');
    
    const response = await fetch(url.toString());
    
    if (!response.ok) {
      return [];
    }
    
    const data = await response.json();
    
    if (!data.results) {
      return [];
    }
    
    return data.results.map(result => ({
      latitude: result.latitude,
      longitude: result.longitude,
      name: result.name,
      country: result.country || 'Unknown',
      admin1: result.admin1 || ''
    }));
    
  } catch (error) {
    logger.error('Error searching cities:', error);
    return [];
  }
}