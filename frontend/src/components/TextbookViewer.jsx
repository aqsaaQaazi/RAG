import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';
import LanguageSelector from './LanguageSelector';
import './TextbookViewer.css'; // Import custom styles

export default function TextbookViewer() {
  const {siteConfig} = useDocusaurusContext();
  const [language, setLanguage] = React.useState('en');

  const handleLanguageChange = (newLanguage) => {
    setLanguage(newLanguage);
  };

  return (
    <Layout
      title={`Textbook - ${siteConfig.title}`}
      description="Physical AI & Humanoid Robotics Textbook">
      <main className="container margin-vert--lg textbook-viewer">
        <div className="row">
          <div className="col col--10 col--offset-1">
            <div className="textbook-header text--center margin-bottom--lg">
              <Heading as="h1" className="textbook-title">
                Physical AI & Humanoid Robotics Textbook
              </Heading>

              <div className="margin-bottom--md">
                <LanguageSelector onLanguageChange={handleLanguageChange} />
              </div>

              <p className="hero__subtitle textbook-subtitle">
                An interactive textbook with RAG-powered chatbot for enhanced learning
              </p>
            </div>

            <div className="textbook-content-card margin-vert--lg">
              <h2 className="textbook-section-title">Table of Contents</h2>
              <div className="chapters-grid">
                <div className="chapter-card">
                  <Link to="/docs/01-introduction" className="chapter-link">
                    <div className="chapter-icon">1</div>
                    <h3>Introduction to Physical AI & Humanoid Robotics</h3>
                  </Link>
                </div>
                <div className="chapter-card">
                  <Link to="/docs/02-foundations-of-physical-ai" className="chapter-link">
                    <div className="chapter-icon">2</div>
                    <h3>Foundations of Physical AI</h3>
                  </Link>
                </div>
                <div className="chapter-card">
                  <Link to="/docs/03-humanoid-robot-design" className="chapter-link">
                    <div className="chapter-icon">3</div>
                    <h3>Humanoid Robot Design</h3>
                  </Link>
                </div>
                <div className="chapter-card">
                  <Link to="/docs/04-locomotion-and-control" className="chapter-link">
                    <div className="chapter-icon">4</div>
                    <h3>Locomotion and Control</h3>
                  </Link>
                </div>
                <div className="chapter-card">
                  <Link to="/docs/05-sensing-and-perception" className="chapter-link">
                    <div className="chapter-icon">5</div>
                    <h3>Sensing and Perception</h3>
                  </Link>
                </div>
                <div className="chapter-card">
                  <Link to="/docs/06-learning-algorithms" className="chapter-link">
                    <div className="chapter-icon">6</div>
                    <h3>Learning Algorithms</h3>
                  </Link>
                </div>
                <div className="chapter-card">
                  <Link to="/docs/07-hardware-integration" className="chapter-link">
                    <div className="chapter-icon">7</div>
                    <h3>Hardware Integration</h3>
                  </Link>
                </div>
                <div className="chapter-card">
                  <Link to="/docs/08-ethics-and-safety" className="chapter-link">
                    <div className="chapter-icon">8</div>
                    <h3>Ethics and Safety</h3>
                  </Link>
                </div>
                <div className="chapter-card">
                  <Link to="/docs/09-future-directions" className="chapter-link">
                    <div className="chapter-icon">9</div>
                    <h3>Future Directions</h3>
                  </Link>
                </div>
                <div className="chapter-card">
                  <Link to="/docs/10-conclusion" className="chapter-link">
                    <div className="chapter-icon">10</div>
                    <h3>Conclusion</h3>
                  </Link>
                </div>
              </div>
            </div>

            <div className="learning-features margin-vert--lg">
              <h2 className="textbook-section-title">Learning Features</h2>
              <div className="row">
                <div className="col col--6">
                  <div className="feature-card">
                    <h3>Key Ideas</h3>
                    <p>Each chapter concludes with key concepts to reinforce your learning.</p>
                  </div>
                </div>
                <div className="col col--6">
                  <div className="feature-card">
                    <h3>Practical Checklist</h3>
                    <p>Actionable items to help you apply the concepts.</p>
                  </div>
                </div>
              </div>
            </div>

            <div className="margin-vert--lg text--center">
              <Link
                className="button button--primary button--lg textbook-cta-button"
                to="/ask-book">
                Ask the Book Chatbot
              </Link>
            </div>

            <div className="textbook-footer margin-vert--lg text--center">
              <p className="text--center">
                © {new Date().getFullYear()} Physical AI & Humanoid Robotics Textbook. All rights reserved.
              </p>
              <p>
                <Link to="/authors">About the Authors</Link> |
                <Link to="/docs/01-introduction">Introduction</Link> |
                <Link to="/ask-book">Ask the Book</Link>
              </p>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}