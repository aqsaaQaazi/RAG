// Theme Manager Service
// Handles theme switching and preference persistence

class ThemeManager {
  constructor() {
    this.currentTheme = this.getStoredTheme() || this.getSystemTheme();
    this.applyTheme(this.currentTheme);
  }

  // Get the theme stored in localStorage
  getStoredTheme() {
    try {
      return localStorage.getItem('theme');
    } catch (e) {
      console.warn('Could not access localStorage for theme preference');
      return null;
    }
  }

  // Get the user's system theme preference
  getSystemTheme() {
    if (typeof window !== 'undefined' && window.matchMedia) {
      try {
        const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        return systemPrefersDark ? 'dark' : 'light';
      } catch (e) {
        console.warn('Could not detect system theme preference, defaulting to light theme');
        return 'light';
      }
    }
    return 'light'; // default fallback
  }

  // Apply the theme to the document
  applyTheme(theme) {
    if (typeof document !== 'undefined') {
      try {
        document.documentElement.setAttribute('data-theme', theme);
      } catch (e) {
        console.error('Could not apply theme to document element', e);
      }
    }
    this.currentTheme = theme;
  }

  // Toggle between light and dark themes
  toggleTheme() {
    const newTheme = this.currentTheme === 'light' ? 'dark' : 'light';
    this.setTheme(newTheme);
    return newTheme;
  }

  // Explicitly set a theme
  setTheme(theme) {
    if (theme !== 'light' && theme !== 'dark') {
      console.warn(`Invalid theme: ${theme}. Using 'light' or 'dark'.`);
      return;
    }
    
    this.currentTheme = theme;
    this.applyTheme(theme);
    
    // Store preference in localStorage
    try {
      localStorage.setItem('theme', theme);
    } catch (e) {
      console.warn('Could not save theme preference to localStorage');
    }
  }

  // Get the current theme
  getCurrentTheme() {
    return this.currentTheme;
  }

  // Check if the current theme is dark
  isDarkTheme() {
    return this.currentTheme === 'dark';
  }

  // Check if the current theme is light
  isLightTheme() {
    return this.currentTheme === 'light';
  }
}

// Create a singleton instance
const themeManager = new ThemeManager();

// Export both the class and instance
export { ThemeManager };
export default themeManager;