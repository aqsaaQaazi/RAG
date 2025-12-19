import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Heading from '@theme/Heading';

export default function AuthorDetails() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={`Authors - ${siteConfig.title}`}
      description="About the authors of the Physical AI & Humanoid Robotics Textbook"
    >
      <main className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset-2">
            <Heading as="h1" className="text--center margin-bottom--lg">
              About the Authors
            </Heading>

            <div className="margin-vert--lg">
              <div className="text--center margin-bottom--lg">
                <img
                  src="/img/author-placeholder.jpg"
                  alt="Author"
                  style={{
                    width: '150px',
                    height: '150px',
                    borderRadius: '50%',
                    objectFit: 'cover',
                  }}
                />
              </div>

              <h2>Dr. [Author Name]</h2>
              <p>
                Dr. [Author Name] is a leading researcher in the field of
                Physical AI and Humanoid Robotics with over [X] years of
                experience. They hold a Ph.D. in [relevant field] from
                [University] and have published extensively on [relevant
                topics].
              </p>

              <h3>Research Interests</h3>
              <ul>
                <li>Physical AI and embodied cognition</li>
                <li>Humanoid robot control and locomotion</li>
                <li>Human-robot interaction and collaboration</li>
                <li>Robot ethics and safety</li>
              </ul>

              <h3>Relevant Publications</h3>
              <ul>
                <li>[Publication Title 1] - [Journal/Conference], [Year]</li>
                <li>[Publication Title 2] - [Journal/Conference], [Year]</li>
                <li>[Publication Title 3] - [Journal/Conference], [Year]</li>
              </ul>
            </div>

            <div className="margin-vert--lg">
              <h2>Educational Purpose Statement</h2>
              <p>
                This textbook aims to provide students, researchers, and
                practitioners with a comprehensive introduction to Physical AI
                and Humanoid Robotics. The content is designed to be accessible
                to readers with basic knowledge of robotics and AI, while
                providing sufficient depth for advanced study and research.
              </p>
            </div>

            <div className="margin-vert--lg">
              <h2>Safety Disclaimer</h2>
              <p>
                The information contained in this textbook is for educational
                purposes only. While every effort has been made to ensure
                accuracy, the authors and publishers are not responsible for any
                damages or injuries resulting from the application of the
                concepts described herein. Always follow appropriate safety
                protocols when working with physical robotic systems.
              </p>
            </div>

            <div className="margin-vert--lg">
              <h2>Content and Code License Terms</h2>
              <p>
                The textual content of this textbook is licensed under the
                Creative Commons Attribution 4.0 International License (CC BY
                4.0). You are free to share and adapt the material for any
                purpose, even commercially, as long as you give appropriate
                credit, provide a link to the license, and indicate if changes
                were made.
              </p>
              <p>
                The code examples provided in this textbook are licensed under
                the MIT License. You are free to use, modify, and distribute the
                code for any purpose, including commercial use, subject to the
                requirements specified in the MIT License.
              </p>
              <p>
                For more details about the CC BY 4.0 license, visit:
                <a href="https://creativecommons.org/licenses/by/4.0/">
                  https://creativecommons.org/licenses/by/4.0/
                </a>
              </p>
              <p>
                For more details about the MIT License, visit:
                <a href="https://opensource.org/licenses/MIT">
                  https://opensource.org/licenses/MIT
                </a>
              </p>
            </div>

            <div className="margin-vert--lg text--center">
              <p>
                <a href="mailto:[author-email]">Contact the Author</a> |
                <a href="[author-website]"> Author's Website</a>
              </p>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
