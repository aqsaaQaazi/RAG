// Language Manager Service
// Handles language switching and content presentation

class LanguageManager {
  constructor() {
    // Define supported languages based on the project requirements
    this.supportedLanguages = ['en', 'ur'];
    this.currentLanguage = this.getStoredLanguage() || this.getBrowserLanguage() || 'en';
    this.languageContent = {}; // To store content by language
  }

  // Get the language stored in localStorage
  getStoredLanguage() {
    try {
      return localStorage.getItem('language');
    } catch (e) {
      console.warn('Could not access localStorage for language preference');
      return null;
    }
  }

  // Get the user's browser language preference
  getBrowserLanguage() {
    try {
      if (typeof navigator !== 'undefined' && navigator.language) {
        const browserLang = navigator.language.split('-')[0].toLowerCase();
        if (this.supportedLanguages.includes(browserLang)) {
          return browserLang;
        }
      }
    } catch (e) {
      console.warn('Could not detect browser language preference');
    }
    return null;
  }

  // Set the current language
  setLanguage(languageCode) {
    if (!languageCode) {
      console.error('Language code is required');
      return false;
    }

    if (!this.supportedLanguages.includes(languageCode)) {
      console.warn(`Language ${languageCode} is not supported. Available: ${this.supportedLanguages.join(', ')}`);
      return false;
    }

    this.currentLanguage = languageCode;

    // Store preference in localStorage
    try {
      localStorage.setItem('language', languageCode);
    } catch (e) {
      console.warn('Could not save language preference to localStorage');
    }

    try {
      // Apply language changes to the UI (this would trigger re-renders in a React context)
      this.applyLanguageChanges(languageCode);
    } catch (e) {
      console.error('Could not apply language changes to UI', e);
    }

    return true;
  }

  // Get the current language
  getCurrentLanguage() {
    return this.currentLanguage;
  }

  // Get supported languages
  getSupportedLanguages() {
    return [...this.supportedLanguages]; // Return a copy
  }

  // Check if a language is supported
  isLanguageSupported(languageCode) {
    return this.supportedLanguages.includes(languageCode);
  }

  // Add content for a specific language
  addContent(languageCode, key, content) {
    if (!this.languageContent[languageCode]) {
      this.languageContent[languageCode] = {};
    }
    this.languageContent[languageCode][key] = content;
  }

  // Get content for the current language
  getContent(key) {
    const content = this.languageContent[this.currentLanguage]?.[key];
    
    // Fallback to English if content not available in current language
    if (!content && this.currentLanguage !== 'en') {
      return this.languageContent['en']?.[key] || null;
    }
    
    return content || null;
  }

  // Get content for a specific language
  getContentByLanguage(languageCode, key) {
    if (!this.isLanguageSupported(languageCode)) {
      return null;
    }
    return this.languageContent[languageCode]?.[key] || null;
  }

  // Apply language changes to the UI
  applyLanguageChanges(languageCode) {
    // In a Docusaurus context, this would likely trigger a re-render
    // For now, we'll just update the HTML lang attribute
    if (typeof document !== 'undefined') {
      try {
        document.documentElement.setAttribute('lang', languageCode);

        // Apply RTL direction for languages that need it
        if (this.getLanguageDirection(languageCode) === 'rtl') {
          document.documentElement.setAttribute('dir', 'rtl');
        } else {
          document.documentElement.removeAttribute('dir'); // defaults to ltr
        }
      } catch (e) {
        console.error('Could not apply language attributes to document element', e);
      }
    }
  }

  // Get directionality (for RTL languages like Urdu)
  getLanguageDirection(languageCode = this.currentLanguage) {
    // Urdu is right-to-left, English is left-to-right
    if (languageCode === 'ur') {
      return 'rtl';
    }
    return 'ltr';
  }
}

// Create a singleton instance
const languageManager = new LanguageManager();

// Export both the class and instance
export { LanguageManager };
export default languageManager;