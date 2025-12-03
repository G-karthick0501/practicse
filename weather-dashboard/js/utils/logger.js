/**
 * Logging Utility
 * Control console logs in one place
 * Set DEV_MODE to false before submission to hide verbose logs
 */

const DEV_MODE = true; // Change to false for production

export const logger = {
  debug: (...args) => {
    if (DEV_MODE) {
      console.log(...args);
    }
  },

  info: (...args) => {
    if (DEV_MODE) {
      console.log('ℹ️', ...args);
    }
  },

  success: (...args) => {
    if (DEV_MODE) {
      console.log('✅', ...args);
    }
  },

  warn: (...args) => {
    console.warn('⚠️', ...args);
  },

  error: (...args) => {
    console.error('❌', ...args);
  }
};