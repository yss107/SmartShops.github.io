# SmartShop: Personalized Grocery Item Recommendation System

A machine learning-powered web application that provides personalized grocery recommendations using Natural Language Processing (NLP) and collaborative filtering techniques.

## 🎯 Project Overview

SmartShop is an intelligent grocery recommendation system that helps users discover products based on their preferences and shopping patterns. The system combines multiple machine learning approaches to provide accurate and diverse product suggestions.

![SmartShop Application Interface](https://github.com/user-attachments/assets/e877cc52-99a9-4c49-932f-0190e18acd62)

*The SmartShop web interface featuring natural language search and interactive grocery list management*

## ✨ Features

### 🔍 Natural Language Product Search
- **Text-based Search**: Enter natural language queries to find products
- **Semantic Matching**: Uses NLP techniques with stemming and TF-IDF vectorization
- **Intelligent Results**: Returns the most relevant products based on product descriptions

### 🎯 Collaborative Filtering Recommendations  
- **SVD Algorithm**: Implements Singular Value Decomposition for user-item recommendations
- **Interactive Rating**: Rate products to get personalized recommendations
- **Diversity Control**: Adjustable diversity index to balance popular vs. niche recommendations
- **Aisle-specific Filtering**: Get recommendations within specific product categories

### 🛒 Interactive Grocery List
- **Smart List Building**: Add recommended products to your grocery list
- **Custom Items**: Add your own products manually
- **Export Options**: Download as Excel or print your grocery list
- **Real-time Updates**: Dynamic list management with quantity tracking

![SmartShop Grocery List Features](https://github.com/user-attachments/assets/31a35c66-fc71-4c2b-80c4-bb7b90005b11)

*Interactive grocery list with export and management features*

### 📊 Market Basket Analysis
- **Product Associations**: Discover frequently bought together items
- **Clustering Analysis**: User segmentation based on purchasing patterns
- **Data-driven Insights**: Leverage transaction patterns for better recommendations

## 🏗️ Project Structure

```
SmartShops.github.io/
├── flask_app/                          # Main web application
│   ├── app.py                         # Flask application routes
│   ├── user_functions.py              # ML recommendation functions
│   ├── templates/                     # HTML templates
│   │   ├── index.html                # Landing page
│   │   └── nlp.html                  # Main recommendation interface
│   └── static/                       # CSS, images, and static files
├── Capstone_Project.ipynb            # Main analysis and EDA notebook
├── Clustering_and_NLP.ipynb          # User clustering and NLP implementation
├── Market_Basket_Analysis.ipynb      # Association rules and market basket analysis
├── Pickle/                           # Serialized ML models and preprocessed data
├── grocery.db                        # SQLite database with product data
├── new_df.csv                       # Processed dataset
└── archive (24)/                    # Additional datasets (aisles.csv, departments.csv)
```

## 🛠️ Technology Stack

### Backend
- **Python 3.12+**
- **Flask** - Web framework
- **Pandas & NumPy** - Data manipulation and analysis
- **Scikit-learn** - Machine learning algorithms
- **Surprise** - Collaborative filtering library
- **NLTK** - Natural language processing

### Frontend
- **HTML5 & CSS3**
- **Tailwind CSS** - Styling framework
- **JavaScript/jQuery** - Interactive functionality
- **Font Awesome** - Icons

### Machine Learning
- **TF-IDF Vectorization** - Text feature extraction
- **Cosine Similarity** - Product matching
- **SVD (Singular Value Decomposition)** - Collaborative filtering
- **Snowball Stemmer** - Text preprocessing
- **K-Means Clustering** - User segmentation

## 🚀 Getting Started

### Prerequisites
- Python 3.12 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yss107/SmartShops.github.io.git
   cd SmartShops.github.io
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```
   
   **Note**: If you encounter issues with `scikit-surprise`, use conda instead:
   ```bash
   conda install -c conda-forge scikit-surprise
   ```

3. **Download NLTK data** (required for NLP features)
   ```python
   python -c "import nltk; nltk.download('punkt')"
   ```

4. **Run the application**
   ```bash
   cd flask_app
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## 💡 Quick Start Example

Here's how to get personalized grocery recommendations in just a few steps:

1. **Natural Language Search**: Type "organic fruits for breakfast" in the search box
2. **Browse Results**: View AI-recommended products matching your query
3. **Build Your List**: Click products to add them to your grocery list
4. **Customize**: Add custom items like "2 dozen eggs" manually
5. **Export**: Download your complete grocery list as Excel or print it

### Sample Search Queries
- `"healthy snacks for kids"`
- `"ingredients for pasta dinner"`
- `"organic vegetables"`
- `"gluten-free bread alternatives"`
- `"fresh fruits in season"`

## 📖 Usage Guide

### Natural Language Search
1. Navigate to the main interface
2. Enter product keywords in the search box (e.g., "organic apples", "whole grain bread")
3. Click "Get Recommendations" to see relevant products
4. Select products from the dropdown to add to your grocery list

### Collaborative Filtering
1. Go to the SVD recommendation section
2. Choose the number of products to rate
3. Select product categories (aisles) for rating and recommendations
4. Set the diversity index (0.0 = popular items, 1.0 = diverse items)
5. Rate the presented products
6. Receive personalized recommendations based on your ratings

### Grocery List Management
- **Add Items**: Use recommendations or add custom products
- **Manage Quantities**: Adjust item quantities in your list
- **Export**: Download as Excel file or print your list
- **Save**: Store your list locally in browser storage

## 🧠 Machine Learning Models

### 1. Natural Language Processing Pipeline
- **Text Preprocessing**: Tokenization and stemming using NLTK
- **Feature Extraction**: TF-IDF vectorization of product descriptions
- **Similarity Matching**: Cosine similarity for product recommendations

### 2. Collaborative Filtering (SVD)
- **Algorithm**: Singular Value Decomposition with 20 factors
- **Training**: 10 epochs with learning rate 0.005
- **Regularization**: 0.4 to prevent overfitting
- **Cold Start**: Handles new users through product rating interface

### 3. Market Basket Analysis
- **Association Rules**: Frequent itemset mining
- **Support & Confidence**: Statistical measures for product associations
- **User Clustering**: K-means segmentation based on purchase patterns

## 📊 Data Sources

The system uses grocery transaction data including:
- **Products**: 49,000+ unique grocery items
- **Aisles**: 134 product categories
- **Departments**: 21 major department classifications
- **User Ratings**: Synthetic and collected rating data
- **Transactions**: Historical purchase patterns

## 🎨 Features in Detail

### Recommendation Diversity
The system implements a diversity control mechanism that balances:
- **Popular Items** (short head): Frequently purchased products
- **Niche Items** (long tail): Less common but potentially relevant products
- **User Control**: Adjustable diversity percentage via slider

### Real-time Interactivity
- **AJAX Integration**: Seamless product search without page reloads
- **Dynamic Updates**: Real-time grocery list modifications
- **Responsive Design**: Mobile-friendly interface

### Data Persistence
- **Pickle Files**: Serialized models and preprocessed data for fast loading
- **SQLite Database**: Product information storage
- **Session Management**: User preferences and cart persistence

## 🔧 Configuration

### Model Parameters
Key parameters can be adjusted in `user_functions.py`:
- **SVD Factors**: `n_factors = 20`
- **Learning Rate**: `lr_all = 0.005`
- **Regularization**: `reg_all = 0.4`
- **Epochs**: `n_epochs = 10`

### Search Parameters
- **Max Results**: Up to 10 products per search
- **Similarity Threshold**: Cosine similarity > 0
- **Stemming Language**: English (configurable)

## 🐛 Troubleshooting

### Common Issues

**1. Module Import Errors**
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt
```

**2. NLTK Data Missing**
```python
import nltk
nltk.download('punkt')
```

**3. Pickle File Errors**
- The application requires pre-trained models in the `Pickle/` directory
- Ensure all `.p` files are present and accessible
- Run the Jupyter notebooks to regenerate models if needed

**4. Flask Application Won't Start**
```bash
# Check if you're in the right directory
cd flask_app
python app.py
```

**5. Static Files Not Loading**
- Ensure the `static/` directory contains all CSS and image files
- Check file permissions and paths in templates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is available for educational and research purposes. Please respect the data sources and usage guidelines.

## 👥 Authors

- **yss107** - Project Lead and Developer

## 🙏 Acknowledgments

- Instacart Market Basket Analysis dataset inspiration
- Scikit-learn and Surprise library communities
- Flask framework developers
- NLTK contributors

---

## 📞 Contact

For questions, suggestions, or collaboration opportunities, please open an issue on GitHub.

**Happy Shopping with SmartShop! 🛍️**