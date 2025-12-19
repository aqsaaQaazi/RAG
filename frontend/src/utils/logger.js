// Logging utility for the Physical AI & Humanoid Robotics Textbook

// Define log levels
const LOG_LEVELS = {
  DEBUG: 0,
  INFO: 1,
  WARN: 2,
  ERROR: 3
};

// Current log level (can be adjusted based on environment)
let currentLogLevel = LOG_LEVELS.INFO;

// Set log level based on environment
if (process.env.NODE_ENV === 'development') {
  currentLogLevel = LOG_LEVELS.DEBUG;
} else if (process.env.REACT_APP_LOG_LEVEL) {
  currentLogLevel = LOG_LEVELS[process.env.REACT_APP_LOG_LEVEL.toUpperCase()];
}

// Format log messages
const formatMessage = (level, message, ...optionalParams) => {
  const timestamp = new Date().toISOString();
  const logMessage = `${timestamp} [${level}] ${message}`;
  
  if (optionalParams.length > 0) {
    return [logMessage, ...optionalParams];
  }
  
  return logMessage;
};

// Logging functions
export const logger = {
  debug: (message, ...optionalParams) => {
    if (currentLogLevel <= LOG_LEVELS.DEBUG) {
      console.debug(...formatMessage('DEBUG', message, ...optionalParams));
    }
  },
  
  info: (message, ...optionalParams) => {
    if (currentLogLevel <= LOG_LEVELS.INFO) {
      console.info(...formatMessage('INFO', message, ...optionalParams));
    }
  },
  
  warn: (message, ...optionalParams) => {
    if (currentLogLevel <= LOG_LEVELS.WARN) {
      console.warn(...formatMessage('WARN', message, ...optionalParams));
    }
  },
  
  error: (message, ...optionalParams) => {
    if (currentLogLevel <= LOG_LEVELS.ERROR) {
      console.error(...formatMessage('ERROR', message, ...optionalParams));
    }
  }
};

export default logger;