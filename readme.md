# 1) Data Cleaning and Refining Notebook

This Jupyter notebook is designed for exploring, filtering, and cleaning product review data for cosmetics brands. It focuses primarily on the Nykaa Cosmetics and Kay Beauty brands, with a particular emphasis on lipstick products.

## Contents:

1. **Dataset Exploration** - Initial loading and examination of the dataset to understand the structure and main features.
2. **Filtering & Cleaning Lipsticks from Nykaa Brand** - Specific steps to filter and clean the data related to Nykaa Cosmetics, focusing on lipstick products. Includes extracting reviews, review dates, ratings, product titles, and buyer status.
3. **Filtering & Cleaning Lipsticks from Kay Beauty Brand** - Similar to the Nykaa section, but specific to Kay Beauty.

## Usage:

- Ensure you have pandas installed (`pip install pandas`).
- The notebook is structured to be run cell by cell, from top to bottom.

## Purpose:

The notebook serves as a practical example of handling real-world data cleaning tasks in the cosmetics industry. It can be used as a template or guide for similar data cleaning processes in other contexts.

## Requirements:

- Python 3.x
- Pandas library

# 2) Nykaa LDA Topic Modeling Notebook

This Jupyter notebook demonstrates the application of LDA (Latent Dirichlet Allocation) for topic modeling on product reviews from Nykaa, a popular e-commerce platform for cosmetics. The notebook guides users through the process of data pre-processing, LDA model training, and topic visualization.

## Contents:

1. **Introduction** - A brief overview of the motivation behind using topic modeling and LDA.
2. **Necessary Libraries** - Details all Python libraries needed, such as matplotlib for graphing and Gensim for LDA modeling.
3. **Pre-processing** - Procedures to clean and prepare the text data for topic analysis.
4. **LDA Model Experiments** - Describes the experimentation with different configurations of the LDA model to determine the optimal setup.

## Usage:

- Ensure you have the necessary libraries installed (matplotlib, pyLDAvis, etc.).
- The notebook is intended to be run sequentially from top to bottom.

## Purpose:

The notebook serves as an educational tool for understanding and applying topic modeling to real-world text data, specifically in the context of product reviews on e-commerce platforms.

## Requirements:

- Python 3.x
- Libraries: nltk, gensim, pyLDAvis, matplotlib, pandas, contractions, wordcloud, re, warnings

# 3) Kay Beauty LDA Topic Modeling Notebook

This Jupyter notebook demonstrates the application of LDA (Latent Dirichlet Allocation) for topic modeling on product reviews from Kay Beauty, a notable brand within the cosmetics industry. The notebook includes detailed steps for data pre-processing, training the LDA model, and visualizing the topics.

## Contents:

1. **Introduction** - A brief overview of the motivation behind using topic modeling and LDA.
2. **Necessary Libraries** - Details all Python libraries needed, such as matplotlib for graphing and Gensim for LDA modeling.
3. **Pre-processing** - Procedures to clean and prepare the text data for topic analysis.
4. **LDA Model Experiments** - Describes the experimentation with different configurations of the LDA model to determine the optimal setup.

## Usage:

- Ensure you have the necessary libraries installed (matplotlib, pyLDAvis, etc.).
- The notebook is intended to be run sequentially from top to bottom.

## Purpose:

The notebook is designed to provide insights into the various topics prevalent in customer reviews, allowing businesses to better understand consumer feedback and preferences.

## Requirements:

- Python 3.x
- Libraries: nltk, gensim, pyLDAvis, matplotlib, pandas, contractions, wordcloud, re, warnings

# 4) Nykaa and Kay Sentiment Analysis Notebooks

This Jupyter notebook is designed for performing sentiment analysis on product reviews from Nykaa. It employs three different sentiment analysis tools: VADER, TextBlob, and RoBERTa, from the transformers library. The notebook details the process from data loading, applying each method, to analysis and visualization of sentiment scores across reviews.

## Contents:

1. **Introduction** - Overview of sentiment analysis, discussing its importance in gauging customer feedback.
2. **Necessary Libraries** - Lists all Python libraries required for running the notebook.
3. **Data Loading and Preparation** - Steps to load and prepare the data for sentiment analysis.
4. **Sentiment Analysis Methods** -
   - **VADER Analysis**
   - **TextBlob Analysis**
   - **RoBERTa Analysis** - Using a pre-trained model from the transformers library.
5. **Comparison and Visualization of Results** - Visualizes the sentiment scores obtained by each method to compare their performance and insights.

## Usage:

- Ensure all necessary libraries are installed.
- The notebook is designed to be executed sequentially from start to finish.

## Purpose:

The notebook offers a multi-faceted approach to sentiment analysis, providing insights into different methods and their applicability to real-world customer review data.

## Requirements:

- Python 3.x
- Libraries: pandas, nltk, matplotlib, seaborn, transformers, textblob, sklearn, numpy, scipy, tqdm

# Note:

#### The original dataset that is needed to run the first notebook is uploaded as:

nyka_top_brands_cosmetics_product_reviews.csv

#### The two smaller filtered subsets for Nykaa Cosmetics and Kay Beauty are outputted as a result of running the first notebook:

kay_filtered_lip_products.csv
nykaa_filtered_lip_products.csv

#### The labelled datasets are as a result of running the second and the third notebooks (LDA topic Modelling):

nykaa_labeled.csv
kay_labeled.csv

#### The datasets with sentiments provided are a result of running the fourth and fifth notebooks:

nykaa_sentiment.csv
kay_sentiment.csv

#### The two manually annotated subsets were 150 reviews each that was manually extracted and annotated for evaluation purposes to be used in the fourth and fifth notebooks:

nykaa_manually_annotated.csv
kay_manually_annotated.csv

Feel free to fork or clone this repository to adapt the processes to your own data cleaning needs.
