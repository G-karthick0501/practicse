/**
 * Format date and time
 * @param {string} isoString - ISO date string
 * @param {string} timezone - Timezone string
 * @returns {string} - Formatted time
 */
export function formatTime(isoString, timezone = 'UTC') {
  const date = new Date(isoString);
  return new Intl.DateTimeFormat('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    timeZone: timezone,
    hour12: true
  }).format(date);
}

/**
 * Format date for axis labels
 * @param {string} isoString - ISO date string
 * @returns {string} - Short time format
 */
export function formatChartLabel(isoString) {
  const date = new Date(isoString);
  return new Intl.DateTimeFormat('en-US', {
    hour: 'numeric',
    hour12: true
  }).format(date);
}

/**
 * Round numbers
 * @param {number} value 
 * @returns {number}
 */
export function formatNumber(value) {
  return Math.round(value);
}