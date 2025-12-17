import React, { useState, useRef, useEffect } from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function ChatWithBook() {
  const {siteConfig} = useDocusaurusContext();
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    // Add user message to chat
    const userMessage = { sender: 'user', text: inputValue, timestamp: new Date() };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Call the backend API
      const response = await fetch('/api/v1/chat/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: inputValue,
          language: 'en'
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      // Add bot response to chat
      const botMessage = { 
        sender: 'bot', 
        text: data.answer, 
        citations: data.citations || [],
        timestamp: new Date() 
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error:', error);
      const errorMessage = { 
        sender: 'bot', 
        text: 'Sorry, I encountered an error processing your request. Please try again.', 
        timestamp: new Date() 
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleCitationClick = (citation) => {
    // In a real implementation, this would navigate to the specific section
    console.log('Citation clicked:', citation);
    alert(`Navigating to: ${citation.chapter_title} - ${citation.section_heading}`);
  };

  return (
    <Layout
      title={`Ask the Book - ${siteConfig.title}`}
      description="Chat with the Physical AI & Humanoid Robotics textbook">
      <main className="container margin-vert--lg">
        <div className="row">
          <div className="col col--10 col--offset-1">
            <div className="text--center padding--vert--md">
              <h1>Ask the Book</h1>
              <p>Ask questions about Physical AI & Humanoid Robotics and get answers grounded in the textbook content</p>
            </div>

            <div className="chat-container" style={{ 
              border: '1px solid #ccc', 
              borderRadius: '8px', 
              height: '60vh', 
              display: 'flex', 
              flexDirection: 'column' 
            }}>
              <div className="chat-messages" style={{ 
                flex: 1, 
                overflowY: 'auto', 
                padding: '16px' 
              }}>
                {messages.length === 0 ? (
                  <div className="text--center padding--sm" style={{ color: '#888', fontStyle: 'italic' }}>
                    Ask me anything about Physical AI & Humanoid Robotics!
                  </div>
                ) : (
                  messages.map((msg, index) => (
                    <div 
                      key={index} 
                      className={`message margin--sm ${msg.sender === 'user' ? 'user-message' : 'bot-message'}`}
                      style={{ 
                        textAlign: msg.sender === 'user' ? 'right' : 'left',
                        maxWidth: '80%',
                        marginLeft: msg.sender === 'user' ? 'auto' : '0',
                        marginRight: msg.sender === 'user' ? '0' : 'auto',
                      }}
                    >
                      <div 
                        style={{ 
                          display: 'inline-block', 
                          padding: '10px 15px', 
                          borderRadius: '18px', 
                          backgroundColor: msg.sender === 'user' ? '#007bff' : '#f0f0f0',
                          color: msg.sender === 'user' ? 'white' : 'black',
                        }}
                      >
                        {msg.text}
                      </div>
                      
                      {msg.citations && msg.citations.length > 0 && (
                        <div className="citations margin--sm">
                          <small style={{ display: 'block', marginTop: '5px' }}>
                            Sources:
                          </small>
                          {msg.citations.map((citation, idx) => (
                            <button
                              key={idx}
                              onClick={() => handleCitationClick(citation)}
                              className="button button--sm button--link"
                              style={{ display: 'block', textAlign: 'left', marginTop: '2px' }}
                            >
                              <small>
                                {citation.chapter_title} - {citation.section_heading}
                              </small>
                            </button>
                          ))}
                        </div>
                      )}
                    </div>
                  ))
                )}
                {isLoading && (
                  <div 
                    className="bot-message margin--sm" 
                    style={{ 
                      textAlign: 'left',
                      maxWidth: '80%',
                    }}
                  >
                    <div 
                      style={{ 
                        display: 'inline-block', 
                        padding: '10px 15px', 
                        borderRadius: '18px', 
                        backgroundColor: '#f0f0f0',
                        color: 'black',
                      }}
                    >
                      Thinking...
                    </div>
                  </div>
                )}
                <div ref={messagesEndRef} />
              </div>

              <form onSubmit={handleSubmit} className="chat-input-area padding--sm" style={{ borderTop: '1px solid #ccc' }}>
                <div style={{ display: 'flex' }}>
                  <input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    placeholder="Ask a question about the textbook..."
                    className="form-control"
                    style={{ flex: 1, marginRight: '10px', padding: '8px' }}
                    disabled={isLoading}
                  />
                  <button 
                    type="submit" 
                    className="button button--primary"
                    disabled={isLoading || !inputValue.trim()}
                  >
                    {isLoading ? 'Sending...' : 'Send'}
                  </button>
                </div>
                <div className="margin--sm" style={{ fontSize: '0.8em', color: '#888' }}>
                  Answers are generated from the textbook content. Citations will be provided for referenced material.
                </div>
              </form>
            </div>

            <div className="margin-vert--lg text--center">
              <div className="alert alert--info" style={{ display: 'inline-block' }}>
                <p>Remember: I can only answer questions based on the textbook content. If I say I can't find an answer, it means the information isn't in the book.</p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}