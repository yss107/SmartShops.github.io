# SmartShop GitHub Pages

This repository is configured for GitHub Pages deployment, providing a static website showcase of the SmartShop project.

## 🌐 Live Website

Visit the live website at: **https://yss107.github.io/SmartShops.github.io**

## 📁 GitHub Pages Structure

```
├── index.html          # Main homepage
├── demo.html           # Interactive demo page
├── style.css           # Main stylesheet
├── assets/             # Static assets
│   ├── app-screenshot.jpg
│   └── grocery-shop-safely.jpg
├── _config.yml         # Jekyll configuration
└── .gitignore          # Git ignore rules
```

## 🔧 GitHub Pages Configuration

The site is configured to use Jekyll with the following settings:
- **Theme**: Minima (default)
- **Markdown**: Kramdown
- **Highlighter**: Rouge
- **Plugins**: SEO tags, sitemap, feed

## 🚀 Features

### Homepage (`index.html`)
- Project overview and features
- Technology stack showcase
- Installation instructions
- Responsive design

### Demo Page (`demo.html`)
- Interactive interface simulation
- Search functionality with sample data
- Grocery list management
- Export capabilities (CSV, print)

## 📱 Responsive Design

The website is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones

## 🛠️ Development

### Local Testing

To test the site locally:

```bash
# Option 1: Simple HTTP server
python3 -m http.server 8000
# Then visit: http://localhost:8000

# Option 2: Jekyll (if you have it installed)
jekyll serve
# Then visit: http://localhost:4000
```

### Deployment

GitHub Pages automatically deploys from the repository when changes are pushed to the main branch.

## 📚 Related

- **Full Flask Application**: See the `flask_app/` directory for the complete machine learning application
- **Jupyter Notebooks**: Analysis and model development notebooks are in the root directory
- **Documentation**: Comprehensive README.md in the repository root

---

**Note**: This GitHub Pages site showcases the project. For the full interactive application with machine learning capabilities, run the Flask application locally following the instructions in the main README.md.