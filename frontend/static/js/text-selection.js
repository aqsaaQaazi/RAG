// Text selection functionality
// This script enables the "Select text → Ask AI" feature

// Initialize the text selection functionality
function initTextSelection() {
  let selectedText = null;
  
  // Listen for text selection
  document.addEventListener('mouseup', function() {
    const selection = window.getSelection();
    if (selection.toString().trim() !== '') {
      selectedText = selection.toString();
    } else {
      selectedText = null;
    }
  });
  
  // Add a context menu or button when text is selected
  document.addEventListener('selectionchange', function() {
    const selection = window.getSelection();
    if (selection.toString().trim() !== '' && selection.anchorOffset !== selection.focusOffset) {
      // Show "Ask AI" button near the selection
      showAskButton(selection);
    } else {
      // Hide the button if no text is selected
      hideAskButton();
    }
  });
  
  // Function to show the "Ask AI" button
  function showAskButton(selection) {
    // Remove any existing button
    hideAskButton();
    
    // Get the position of the selection
    const range = selection.getRangeAt(0);
    const rect = range.getBoundingClientRect();
    
    // Create the button element
    const button = document.createElement('button');
    button.id = 'ask-ai-button';
    button.textContent = 'Ask AI';
    button.style.position = 'absolute';
    button.style.top = (rect.top + window.scrollY - 40) + 'px';
    button.style.left = (rect.left + window.scrollX) + 'px';
    button.style.zIndex = '9999';
    button.style.backgroundColor = '#007bff';
    button.style.color = 'white';
    button.style.border = 'none';
    button.style.borderRadius = '4px';
    button.style.padding = '5px 10px';
    button.style.cursor = 'pointer';
    button.style.fontSize = '14px';
    button.onclick = function() {
      // Hide the button
      hideAskButton();
      
      // Open the chat interface with the selected text as context
      openChatWithSelectedText(selectedText);
    };
    
    // Add the button to the document
    document.body.appendChild(button);
  }
  
  // Function to hide the "Ask AI" button
  function hideAskButton() {
    const existingButton = document.getElementById('ask-ai-button');
    if (existingButton) {
      existingButton.remove();
    }
  }
  
  // Function to open the chat interface with selected text
  function openChatWithSelectedText(selectedText) {
    // In a Docusaurus environment, we can trigger a custom event
    // or use React state to pass the selected text to the chat component
    const event = new CustomEvent('selectedTextForAI', { detail: { text: selectedText } });
    document.dispatchEvent(event);
    
    // Optionally, scroll to the chat section
    const chatSection = document.querySelector('#chat-section') || document.querySelector('.chat-container');
    if (chatSection) {
      chatSection.scrollIntoView({ behavior: 'smooth' });
    } else {
      // If no specific chat section, open in a new tab or redirect
      // This would depend on the specific page structure
      console.log('Selected text for AI:', selectedText);
    }
  }
}

// Initialize the text selection functionality when the DOM is loaded
document.addEventListener('DOMContentLoaded', initTextSelection);

// Export for use in other modules if needed
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { initTextSelection };
}