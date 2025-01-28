# ReviewAnalyzer: Sentiment and Keyword Extraction Tool

## Overview
**ReviewAnalyzer** is a web application designed to classify Amazon product reviews into **positive**, **neutral**, and **negative** sentiments. It also extracts **key keywords** from the reviews to provide users with actionable insights. This project leverages the **Django** framework for backend development, **React** for frontend, and **spaCy** for pre-built NLP functionalities.

## Features
- **Sentiment Analysis**: Classifies reviews into positive, neutral, and negative sentiments.
- **Keyword Extraction**: Extracts relevant keywords from Amazon product reviews.
- **User-Friendly Interface**: Interactive and intuitive dashboard built with React.
- **Efficient Backend**: Powered by Django Rest Framework and MySQL for robust data management.

## Tech Stack
- **Backend**: Python, Django, Django Rest Framework
- **Frontend**: React
- **Database**: MySQL
- **NLP**: spaCy (Pre-built NLP)

## Domain
- AI
- Frontend
- Backend
- Cloud

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/TechPertz/ReviewAnalyzer.git
   cd ReviewAnalyzer
   ```

2. **Set Up the Backend**
   - Navigate to the backend directory.
   - Create a virtual environment and activate it:
     ```bash
     python -m venv env
     source env/bin/activate  # Linux/Mac
     env\Scripts\activate  # Windows
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run database migrations:
     ```bash
     python manage.py migrate
     ```
   - Start the Django server:
     ```bash
     python manage.py runserver
     ```

3. **Set Up the Frontend**
   - Navigate to the frontend directory.
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the React development server:
     ```bash
     npm start
     ```

## Usage
1. Access the application via the browser at `http://localhost:3000`.
2. Paste Amazon product link into the provided text field.
3. View the sentiment classification and extracted keywords in real-time.

## Future Improvements
- Enhance keyword extraction with user-defined filters.
- Implement review summaries using additional NLP libraries.
- Deploy the application on a cloud platform for public access.
