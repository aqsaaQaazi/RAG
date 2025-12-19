# Data Model: Simple Static Documentation Website (No RAG)

## Entities

### Homepage
- **Description**: The main landing page accessible at the root URL
- **Fields**:
  - id: string (unique identifier)
  - title: string (page title)
  - content: string (main content in markdown/html)
  - language: string (language code, 'en' only)
  - theme: string ('light' or 'dark', defaults to system preference)
  - navigationItems: array of NavigationItem objects
- **Relationships**: None

### NavigationItem
- **Description**: Item in the website navigation
- **Fields**:
  - id: string (unique identifier)
  - label: string (display text)
  - url: string (target URL)
  - type: string ('internal' or 'external')
- **Relationships**: Part of Homepage

### Header Component
- **Description**: Contains book name and navigation elements only (no logos)
- **Fields**:
  - id: string (unique identifier)
  - bookName: string (book title)
  - theme: string ('light' or 'dark')
  - navigationItems: array of NavigationItem objects
- **Relationships**: Associated with all pages

### Footer Component
- **Description**: Contains important links
- **Fields**:
  - id: string (unique identifier)
  - links: array of FooterLink objects
  - copyrightText: string
- **Relationships**: Associated with all pages

#### FooterLink
- **Description**: Individual link in the footer
- **Fields**:
  - id: string (unique identifier)
  - text: string (display text)
  - href: string (target URL)
- **Relationships**: Part of Footer Component

### Theme Manager
- **Description**: Handles theme switching and system preference detection
- **Fields**:
  - id: string (unique identifier)
  - currentTheme: string ('light' or 'dark')
  - systemTheme: string ('light' or 'dark')
  - userPreference: string ('light' or 'dark', null if following system)
- **Relationships**: Associated with all pages

### Documentation Content
- **Description**: Static documentation content in English only
- **Fields**:
  - id: string (unique identifier)
  - title: string (content title)
  - content: string (content in markdown/html)
  - language: string (language code, 'en' only)
  - filePath: string (relative path to the documentation file)
  - seoMetadata: SEO metadata object
  - accessibilityTags: array of string (semantic HTML tags used)
  - order: integer (order in documentation sequence)
- **Relationships**: None (English-only static content)

### SEO metadata
- **Description**: Search engine optimization metadata
- **Fields**:
  - id: string (unique identifier for the content)
  - title: string (SEO title)
  - description: string (meta description)
  - keywords: array of string
  - author: string
  - lastModified: date
- **Relationships**: Associated with Documentation Content