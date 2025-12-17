import React, { useState } from 'react';

const LanguageSelector = ({ onLanguageChange, currentLanguage = 'en' }) => {
  const [selectedLanguage, setSelectedLanguage] = useState(currentLanguage);
  
  const languages = [
    { code: 'en', name: 'English' },
    { code: 'ur', name: 'Urdu' },
    { code: 'es', name: 'Spanish' },
    { code: 'fr', name: 'French' },
    { code: 'de', name: 'German' }
  ];

  const handleLanguageChange = (event) => {
    const newLanguage = event.target.value;
    setSelectedLanguage(newLanguage);
    if (onLanguageChange) {
      onLanguageChange(newLanguage);
    }
  };

  return (
    <div className="language-selector" style={{ margin: '10px 0' }}>
      <label htmlFor="language-select" style={{ marginRight: '10px' }}>
        Language:
      </label>
      <select
        id="language-select"
        value={selectedLanguage}
        onChange={handleLanguageChange}
        style={{
          padding: '5px 10px',
          borderRadius: '4px',
          border: '1px solid #ccc',
          fontSize: '14px'
        }}
      >
        {languages.map((lang) => (
          <option key={lang.code} value={lang.code}>
            {lang.name}
          </option>
        ))}
      </select>
    </div>
  );
};

export default LanguageSelector;