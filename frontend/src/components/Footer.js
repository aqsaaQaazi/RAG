import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

const FooterLink = ({ to, label, isExternal = false }) => {
  if (isExternal) {
    return (
      <a href={to} target="_blank" rel="noopener noreferrer" className="footer-link">
        {label}
      </a>
    );
  }
  
  return (
    <Link to={to} className="footer-link">
      {label}
    </Link>
  );
};

const Footer = () => {
  const { siteConfig } = useDocusaurusContext();
  
  const currentYear = new Date().getFullYear();
  
  const footerLinks = [
    { to: '/docs/intro', label: 'Documentation' },
    { to: '/docs/intro', label: 'Getting Started' },
    { to: '/authors', label: 'Authors' },
    { to: 'https://github.com/aqsaaQaazi/RAG', label: 'GitHub', isExternal: true },
    { to: '/privacy', label: 'Privacy Policy' },
    { to: '/terms', label: 'Terms of Service' },
  ];

  return (
    <footer className="footer-component">
      <div className="footer-content container">
        <div className="footer-top">
          <div className="footer-links">
            {footerLinks.map((link, index) => (
              <FooterLink key={index} to={link.to} label={link.label} isExternal={link.isExternal} />
            ))}
          </div>
        </div>
        
        <div className="footer-bottom">
          <div className="footer-copyright">
            &copy; {currentYear} {siteConfig.title}. All rights reserved.
          </div>
          <div className="footer-credits">
            Built with <a href="https://docusaurus.io" target="_blank" rel="noopener noreferrer">Docusaurus</a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;