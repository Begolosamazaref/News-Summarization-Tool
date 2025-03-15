# News-Summarization-Tool

## Objective
News-Summarization-Tool is a command-line application that fetches news articles from NewsAPI and generates concise summaries based on user preferences. It uses LangChain for AI-powered text processing, vector embeddings for search, and a simple CLI for user interaction.

## Features
- Fetch news articles on specific topics using NewsAPI.
- Generate short (1-2 sentences) or detailed (paragraph) summaries.
- Store and track user topic preferences.
- Provide AI-powered vector embeddings for improved search.
- Maintain user search history.
- Simple command-line interface.

## Requirements
- **Python 3.8+**
- **NewsAPI Key** (Sign up at [NewsAPI](https://newsapi.org/register))
- **Dependencies** (LangChain, OpenAI embeddings, FAISS or ChromaDB)

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/Begolosamazaref/News-Summarization-Tool.git
cd News-Summarization-Tool

### 2. Install Dependencies
```sh
pip install -r requirements.txt

### 3. Configure API Key
Open config.py and add your NewsAPI key:
NEWS_API_KEY = "your_news_api_key_here"

## Usage
Run the Application
sh
python main.py
Available Commands:
Search for news by topic.
Choose summary type (short or detailed).
Save topics of interest for future searches.
View search history to track past queries.
Project Structure
news_retriever.py - Fetches news articles using NewsAPI.
embedding_engine.py - Generates and stores vector embeddings.
summarizer.py - Implements LangChain summarization.
user_manager.py - Tracks user preferences and search history.
main.py - The main interface for the application.
Deliverables
Full Python code with documentation.
A working demo of the application.
