# Quickstart Guide: Simple Static Documentation Website (No RAG)

## Prerequisites

- Node.js v18 or higher
- npm or yarn package manager
- Git

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install frontend dependencies
```bash
cd frontend
npm install
```

### 3. Run the development server
```bash
npm run start
```

This command starts a local development server and opens the website in your browser at `http://localhost:3000`.

### 4. Build for production
```bash
npm run build
```

This command generates static content in the `build` directory, which can be served using any static hosting service.

## Key Features Configuration

### Homepage Setup
The homepage is configured in `src/pages/index.js`. The "Start Reading" button links to the documentation.

### Simplified Header
The header configuration in `docusaurus.config.js` has been updated to include only essential navigation elements and the book name, without logos or extra elements.

### Theme Switching
Theme switching is handled automatically by Docusaurus. The default theme respects system preferences, but users can toggle manually using the theme switcher in the header. This functionality is preserved in the static site.

### English-Only Documentation
All documentation content is provided in English only. The multilingual support features have been removed to simplify the user experience.

## Development Commands

```bash
# Run development server with hot reload
npm run start

# Build static files for production
npm run build

# Serve the built website locally for testing
npm run serve

# Run tests
npm run test

# Check for linting errors
npm run lint

# Format code
npm run format
```

## Directory Structure Overview

```
frontend/
├── docs/              # English documentation content only
├── src/
│   ├── pages/         # React pages (homepage at index.js)
│   ├── components/    # Reusable React components (no backend components)
│   └── css/           # Custom styles
├── static/            # Static assets
├── package.json       # NPM package configuration (frontend only)
├── docusaurus.config.js   # Main Docusaurus configuration (English-only)
└── sidebars.js        # Navigation sidebar config
```

## Customization Points

### Header Configuration
Header elements are configured in `docusaurus.config.js` under the `themeConfig.navbar` section. Only essential navigation elements and the book name are included.

### Styling
Custom CSS can be added to `src/css/custom.css`. Docusaurus uses Infima CSS framework by default, but you can override styles as needed.

### Documentation Content
To add new documentation:

1. Create a new markdown file in the `docs/` directory
2. Update `sidebars.js` if you want the new content to appear in navigation

Note: No backend functionality is included - this is a static site only.