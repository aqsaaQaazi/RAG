# Physical AI & Humanoid Robotics Textbook

This is a frontend-only implementation of an interactive textbook on Physical AI & Humanoid Robotics with a focus on clean UI and multilingual support.

## Features

- 10 comprehensive chapters on Physical AI & Humanoid Robotics
- Clean, responsive UI with accessibility features
- Support for 5 languages (English, Urdu, Spanish, French, German)
- "Key Ideas" and "Practical Checklist" sections in each chapter
- Author information page with licensing details

## Tech Stack

- [Docusaurus v3](https://docusaurus.io/) - Static site generator
- [React](https://reactjs.org/) - Component library
- [Node.js](https://nodejs.org/) - Runtime environment

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## Available Scripts

- `npm start` - Starts the development server
- `npm run build` - Builds the static site for production
- `npm run serve` - Serves the built site locally
- `npm run clear` - Clears the Docusaurus cache
- `npm run lint` - Lints the code using ESLint
- `npm run lint:fix` - Automatically fixes linting issues
- `npm run format` - Formats the code using Prettier
- `npm run format:check` - Checks code formatting

## Project Structure

```
frontend/
├── docs/                 # Chapter content files
├── src/
│   ├── components/       # React components
│   ├── pages/            # Page-level components
│   └── css/              # Custom CSS
├── i18n/                 # Internationalization files
├── static/               # Static assets
├── docusaurus.config.js  # Docusaurus configuration
└── sidebars.js           # Navigation sidebar configuration
```

## Internationalization

The textbook is available in 5 languages:
- English (en)
- Urdu (ur)
- Spanish (es)
- French (fr)
- German (de)

Translation files are located in the `i18n/[language-code]/` directories.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add and commit your changes (`git add . && git commit -m "Add amazing feature"`)
5. Push to your branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This textbook content is licensed under Creative Commons Attribution 4.0 International License (CC BY 4.0).
The code examples are licensed under the MIT License.