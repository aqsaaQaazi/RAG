import React, { useState, useEffect } from 'react';

const SelectionPopup = ({ onSelect, onCancel }) => {
  const [showPopup, setShowPopup] = useState(false);
  const [selectionData, setSelectionData] = useState(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const handleSelection = () => {
      const selection = window.getSelection();
      if (selection.toString().trim() && selection.anchorOffset !== selection.focusOffset) {
        const range = selection.getRangeAt(0);
        const rect = range.getBoundingClientRect();
        
        setSelectionData({
          text: selection.toString(),
          range: range
        });
        
        setPosition({
          x: rect.left + window.scrollX,
          y: rect.top + window.scrollY - 40  // Position above the selection
        });
        
        setShowPopup(true);
      } else {
        setShowPopup(false);
      }
    };

    const handleClick = () => {
      const selection = window.getSelection();
      if (!selection.toString().trim()) {
        setShowPopup(false);
      }
    };

    document.addEventListener('mouseup', handleSelection);
    document.addEventListener('click', handleClick);

    return () => {
      document.removeEventListener('mouseup', handleSelection);
      document.removeEventListener('click', handleClick);
    };
  }, []);

  const handleAskClick = () => {
    if (selectionData) {
      onSelect(selectionData.text);
      setShowPopup(false);
    }
  };

  const handleCancelClick = () => {
    onCancel && onCancel();
    setShowPopup(false);
  };

  if (!showPopup) return null;

  return (
    <div 
      style={{
        position: 'absolute',
        top: position.y,
        left: position.x,
        backgroundColor: '#fff',
        border: '1px solid #ccc',
        borderRadius: '4px',
        boxShadow: '0 2px 10px rgba(0,0,0,0.2)',
        zIndex: 1000,
        display: 'flex',
        gap: '5px',
        padding: '5px'
      }}
    >
      <button 
        onClick={handleAskClick}
        style={{
          background: '#007bff',
          color: 'white',
          border: 'none',
          padding: '5px 10px',
          borderRadius: '3px',
          cursor: 'pointer',
          fontSize: '14px'
        }}
      >
        Ask AI
      </button>
      <button 
        onClick={handleCancelClick}
        style={{
          background: '#6c757d',
          color: 'white',
          border: 'none',
          padding: '5px 10px',
          borderRadius: '3px',
          cursor: 'pointer',
          fontSize: '14px'
        }}
      >
        Cancel
      </button>
    </div>
  );
};

export default SelectionPopup;