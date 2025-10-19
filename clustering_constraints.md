# Clustering Constraints and Parameters

## Overview
This document defines the constraints and parameters used in the clustering implementations for the SmartShop recommendation system.

## KMeans Clustering Constraints

### Data Constraints
- **Input Data**: Scaled user feature vectors
- **Feature Dimensions**: 134 aisle features + additional user metrics
- **Sample Size**: All unique users in the dataset
- **Preprocessing**: StandardScaler applied to normalize features

### Algorithm Parameters
- **Algorithm**: K-Means with Elkan variant
- **Number of Clusters (K)**: Tested range from 10 to 20
  - Optimal K selected: 20 (based on Calinski-Harabasz and WCSS scores)
- **Random State**: 12 (for reproducibility)
- **Initialization**: k-means++ (default)
- **Max Iterations**: 300 (default)

### Evaluation Metrics
- **Calinski-Harabasz Score**: Measures cluster separation
- **Within-Cluster Sum of Squares (WCSS)**: Measures cluster compactness
- **Silhouette Score**: Measures cluster quality

### Business Constraints
- **Minimum Cluster Size**: Clusters should represent at least 1% of user base
- **Maximum Clusters**: Limited to 20 for interpretability
- **Feature Importance**: Aisle purchases weighted equally

## HNSW Clustering Constraints

### Data Constraints
- **Input Data**: Same scaled user feature vectors as KMeans
- **Distance Metric**: Euclidean distance (L2)
- **Dimensionality**: 134+ dimensions

### HNSW Index Parameters
- **Space**: 'l2' (Euclidean distance)
- **Maximum Elements**: Number of users in dataset
- **M Parameter**: 16 (number of bi-directional links per element)
  - Higher M = better recall, more memory usage
  - Typical range: 5-48
- **ef_construction**: 200 (size of dynamic candidate list during construction)
  - Higher ef_construction = better quality index, slower construction
  - Typical range: 100-500
- **ef**: 50 (size of dynamic candidate list during search)
  - Higher ef = better recall, slower search
  - Typical range: 10-500

### Clustering Strategy with HNSW
Since HNSW is primarily for nearest neighbor search, clustering is achieved by:
1. Building HNSW index with all user vectors
2. For each user, finding K nearest neighbors
3. Applying community detection or density-based grouping
4. Assigning cluster labels based on neighbor similarity

### Performance Constraints
- **Build Time**: Should complete within reasonable time (<5 minutes)
- **Query Time**: Per-user neighbor search should be <1ms
- **Memory Usage**: Index should fit in available RAM

### Quality Constraints
- **Recall**: Aim for >95% recall compared to exact nearest neighbors
- **Cluster Coherence**: Clusters should have similar purchasing patterns
- **Cluster Balance**: Avoid creating too many singleton clusters

## Comparison Constraints

### Evaluation Criteria
- **Clustering Quality**: Compare CH scores, silhouette scores
- **Computational Efficiency**: Compare runtime and memory usage
- **Scalability**: Test performance with increasing data size
- **Interpretability**: Ensure clusters have clear business meaning

### Validation Requirements
- **Internal Validation**: Silhouette score, CH index, Davies-Bouldin index
- **External Validation**: Business KPIs (conversion rate, recommendation relevance)
- **Stability**: Results should be reproducible with same random seed

## Data Quality Constraints

### Missing Values
- **Handling**: Impute missing values before clustering
- **Threshold**: Features with >50% missing values should be dropped

### Outliers
- **Detection**: Use IQR or Z-score methods
- **Treatment**: Cap outliers at 99th percentile or remove if <1% of data

### Feature Scaling
- **Method**: StandardScaler (zero mean, unit variance)
- **Application**: Apply to all numerical features before clustering

## Visualization Constraints

### Dimensionality Reduction
- **Method**: t-SNE with 3 components
- **Perplexity**: 10-50 (based on sample size)
- **Purpose**: Visualize high-dimensional clusters in 3D space

### Plot Requirements
- **Cluster Colors**: Distinct colors for each cluster
- **Axes**: Clearly labeled with reduced dimensions
- **Sample Size**: May need to sample for visualization if >10,000 points

## Update History
- **2025-10-19**: Initial document creation with KMeans and HNSW constraints
