// @ts-check
// `@type` JSDoc annotations allow TypeScript to verify code is working correctly.

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'فزیکل AI اور ہیومنوائڈ روبوٹکس کا ٹیکسٹ بک',
  tagline: 'فزیکل AI اور ہیومنوائڈ روبوٹکس پر ایک تعاملی ٹیکسٹ بک',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://your-username.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  organizationName: 'your-organization', // Usually your GitHub org/user name.
  projectName: 'textbook-ui', // Updated for textbook-only project

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'ur',
    locales: ['en', 'ur', 'es', 'fr', 'de'], // Support for 5 major languages including Urdu
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: false, // Disable blog functionality
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'فزیکل AI اور روبوٹکس',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'ٹیکسٹ بک',
          },
          { to: '/authors', label: 'مصنفین', position: 'left' }, // Removed 'Ask the Book' link
          {
            type: 'localeDropdown',
            position: 'right',
          },
          {
            href: 'https://github.com/your-username/your-repo',
            label: 'گیتھب',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'مواد',
            items: [
              {
                label: 'ٹیکسٹ بک',
                to: '/docs/intro',
              },
              // Removed 'Ask the Book' from footer
            ],
          },
          {
            title: 'کمیونٹی',
            items: [
              {
                label: 'اسٹیک اوور فلو',
                href: 'https://stackoverflow.com/questions/tagged/docusaurus',
              },
              {
                label: 'ڈسکورڈ',
                href: 'https://discordapp.com/invite/docusaurus',
              },
              {
                label: 'ٹویٹر',
                href: 'https://twitter.com/docusaurus',
              },
              {
                label: 'گیتھب',
                href: 'https://github.com/facebook/docusaurus',
              },
            ],
          },
        ],
        copyright: `کاپی رائٹ © ${new Date().getFullYear()} فزیکل AI اور ہیومنوائڈ روبوٹکس ٹیکسٹ بک. ڈوکوسورس کے ساتھ تعمیر کیا گیا ہے.`,
      },
      prism: {
        theme: require('prism-react-renderer').themes.github,
        darkTheme: require('prism-react-renderer').themes.dracula,
      },
    }),
};

module.exports = config;