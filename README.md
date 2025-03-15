# News-Summarization-Tool

## Objective
News-Summarization-Tool is a command-line application that fetches news articles from NewsAPI and generates concise summaries based on user preferences. It uses LangChain for AI-powered text processing, vector embeddings for search, and a simple CLI for user interaction.

## Features
- Fetch news articles on specific topics using NewsAPI.
- Generate short (1-2 sentences) or detailed (paragraph) summaries.
- Store and track user topic preferences.
- Provide AI-powered vector embeddings for improved search.
- Show user search history.
- Simple command-line interface.

## Requirements
- **Python 3.8+**
- **NewsAPI Key** (Sign up at [NewsAPI](https://newsapi.org/register))
- **Dependencies** (LangChain, OpenAI embeddings, FAISS-CPU, Transformers, Sentence-Transformers, Requests, LangChain-Community)

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/Begolosamazaref/News-Summarization-Tool.git
cd News-Summarization-Tool
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Configure API Key
Open `config.py` and add your NewsAPI key:
```python
NEWS_API_KEY = "your_news_api_key_here"
```

## Usage
### Run the Application
```sh
python main.py
```

### Available Commands
- Search for news by topic.
- Choose summary type (short or detailed).
- Save topics of interest for future searches.
- View search history to track past queries.

## Demo
Watch the demo here: [News-Summarization-Tool Demo](https://drive.google.com/file/d/1s2UtDsDHOAajt__xErq1IIO5JhnDQPRi/view?usp=drive_link)

## Project Structure
```
config.py             # Stores configuration settings like API keys and global variables.  
embedding_engine.py   # Generates vector embeddings for news articles and stores them in FAISS.  
main.py               # Entry point of the application, coordinating different modules.  
news_retriever.py     # Fetches news articles from NewsAPI based on user queries.  
requirements.txt      # Lists dependencies required to run the project.  
summarizer.py         # Implements LangChain-based text summarization using Hugging Face models.  
user_data.json        # Stores user preferences and search history in JSON format.  
user_manager.py       # Manages user preferences and search history, saving data in JSON.  
```
