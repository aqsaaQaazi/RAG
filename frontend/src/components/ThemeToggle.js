import React, { useState, useEffect } from 'react';
import themeManager from '@site/src/services/ThemeManager';

const ThemeToggle = () => {
  const [currentTheme, setCurrentTheme] = useState(themeManager.getCurrentTheme());

  useEffect(() => {
    // Update state when theme changes from elsewhere
    const handleThemeChange = () => {
      setCurrentTheme(themeManager.getCurrentTheme());
    };

    // Listen for theme changes if we have a mechanism for that
    // For now, we'll just set up the initial theme
    setCurrentTheme(themeManager.getCurrentTheme());
  }, []);

  const toggleTheme = () => {
    const newTheme = themeManager.toggleTheme();
    setCurrentTheme(newTheme);
  };

  return (
    <button 
      onClick={toggleTheme}
      className={`theme-toggle ${currentTheme}`}
      aria-label={`Switch to ${currentTheme === 'light' ? 'dark' : 'light'} mode`}
      title={`Switch to ${currentTheme === 'light' ? 'dark' : 'light'} mode`}
    >
      {currentTheme === 'light' ? (
        <span role="img" aria-label="moon">🌙</span>
      ) : (
        <span role="img" aria-label="sun">☀️</span>
      )}
    </button>
  );
};

export default ThemeToggle;