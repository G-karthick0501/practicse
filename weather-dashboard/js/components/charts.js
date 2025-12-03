import { formatChartLabel } from '../utils/formatter.js';
import { UI } from '../config.js';

let tempChartInstance = null;
let precipChartInstance = null;

export function updateCharts(elements, weatherData) {
  const hourly = weatherData.hourly;
  const labels = hourly.time.map(t => formatChartLabel(t));

  // 1. Temperature Chart
  renderTemperatureChart(elements.temperatureChart, labels, hourly.temperature);

  // 2. Precipitation Chart
  renderPrecipitationChart(elements.precipitationChart, labels, hourly.precipitationProbability);
}

function renderTemperatureChart(canvas, labels, data) {
  const ctx = canvas.getContext('2d');

  // Destroy existing chart if it exists to prevent memory leaks
  if (tempChartInstance) {
    tempChartInstance.destroy();
  }

  tempChartInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: 'Temperature (°C)',  // ✅ Added unit in label
        data: data,
        borderColor: UI.chartColors.temperature,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderWidth: 2,
        tension: 0.4,
        fill: true
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: true },  // ✅ Show legend
        title: { display: true, text: '24-Hour Forecast' }
      },
      scales: {
        y: { 
          beginAtZero: false,
          title: { display: true, text: 'Temperature (°C)' }  // ✅ Y-axis label
        }
      }
    }
  });
}

function renderPrecipitationChart(canvas, labels, data) {
  const ctx = canvas.getContext('2d');

  if (precipChartInstance) {
    precipChartInstance.destroy();
  }

  precipChartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Rain Probability (%)',  // ✅ Added unit in label
        data: data,
        backgroundColor: UI.chartColors.precipitation,
        borderWidth: 0
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: true },  // ✅ Show legend
        title: { display: true, text: 'Precipitation Chance' }
      },
      scales: {
        y: { 
          beginAtZero: true,
          max: 100,
          title: { display: true, text: 'Probability (%)' }  // ✅ Y-axis label
        }
      }
    }
  });
}