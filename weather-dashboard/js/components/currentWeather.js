import { getWeatherDescription } from '../services/weather.js';
import { formatTime, formatNumber } from '../utils/formatter.js';

export function updateCurrentWeather(container, weatherData) {
  const current = weatherData.current;
  const location = weatherData.location;
  const units = weatherData.units;
  
  // Get weather icon and description
  const weatherInfo = getWeatherDescription(current.weatherCode, current.isDay);
  
  // Format timezone display (more descriptive)
  const timezoneDisplay = `${location.timezone_abbreviation} (${location.timezone})`;
  
  const html = `
    <div class="weather-main">
      <h2 class="city-name">📍 ${location.name}, ${location.country}</h2>
      <div class="weather-icon">${weatherInfo.icon}</div>
      <div class="temperature-display">
        ${formatNumber(current.temperature)}${units.temperature}
      </div>
      <p class="weather-description">${weatherInfo.description}</p>
      <p class="weather-time">Updated: ${formatTime(current.time, location.timezone)}</p>
    </div>

    <div class="weather-details">
      <div class="weather-detail-item">
        <span class="weather-detail-label">Humidity</span>
        <span class="weather-detail-value">
          ${current.humidity}<span class="weather-detail-unit">%</span>
        </span>
      </div>
      
      <div class="weather-detail-item">
        <span class="weather-detail-label">Wind Speed</span>
        <span class="weather-detail-value">
          ${current.windSpeed}<span class="weather-detail-unit">${units.windSpeed}</span>
        </span>
      </div>

      <div class="weather-detail-item">
        <span class="weather-detail-label">Timezone</span>
        <span class="weather-detail-value" style="font-size: 0.9rem; margin-top: 5px;">
          ${timezoneDisplay}
        </span>
      </div>
    </div>
    
  `;

  container.innerHTML = html;
  container.classList.remove('hidden');
}