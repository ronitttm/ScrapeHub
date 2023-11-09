import requests
from flask import Flask, render_template, request, redirect, url_for
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

app = Flask(__name__)

# Initialize the list of URLs
urls = ["https://threatpost.com/cisco-network-breach-google/180385/"]
new_urls = []  # Initialize a list for new URLs
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = None

# Function to fetch and preprocess content from a URL
def fetch_url_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # You can customize how you extract and preprocess text here
    text = " ".join(p.get_text() for p in soup.find_all("p"))
    return text

# Function to calculate TF-IDF scores
def calculate_tfidf_scores(texts):
    tfidf_matrix = tfidf_vectorizer.fit_transform(texts)
    return tfidf_matrix

# Calculate TF-IDF scores for initial URLs
url_contents = [fetch_url_content(url) for url in urls]
tfidf_matrix = calculate_tfidf_scores(url_contents)

# Set a threshold (e.g., 0.4)
threshold = 0.4

# Route for the main page
@app.route('/')
def main_page():
    return render_template('main.html', urls=urls)

# Route for adding new URLs
@app.route('/add_url', methods=['POST'])
def add_url():
    new_url = request.form['new_url']
    urls.append(new_url)
    return redirect(url_for('main_page'))

# Route for processing and displaying relevant URLs
@app.route('/display_relevant', methods=['POST'])
def display_relevant():
    selected_urls = request.form.getlist('scraped_urls')
    
    if not selected_urls:
        return render_template('relevant.html', relevant_urls=[])

    # Fetch and preprocess content for the stored and selected URLs
    all_urls = urls + selected_urls
    url_contents = [fetch_url_content(url) for url in all_urls]

    # Calculate TF-IDF scores
    tfidf_matrix = calculate_tfidf_scores(url_contents)

    # Identify relevant URLs based on TF-IDF scores
    relevant_urls = []
    for i, url in enumerate(all_urls):
        relevant_scores = tfidf_matrix[i, :].toarray()
        if np.max(relevant_scores) > threshold:
            relevant_urls.append(url)

    return render_template('relevant.html', relevant_urls=relevant_urls)

# Route for scraping and adding new URLs
@app.route('/scrape_and_add', methods=['GET', 'POST'])
def scrape_and_add():
    for url in urls:
        # Fetch content from the stored URL
        content = fetch_url_content(url)

        # Calculate the TF-IDF score for the content
        tfidf_score = tfidf_vectorizer.transform([content])

        # Compare the TF-IDF score with the threshold
        if np.max(tfidf_score) > threshold:
            # If the score is above the threshold, add the URL to the new list
            new_urls.append(url)

        # Now, scrape the "href" links from the content and add them to the new URLs list
        soup = BeautifulSoup(content, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None:
                new_urls.append(href)

    # Remove duplicates from the new URLs list
    new_urls = list(set(new_urls))

    return redirect(url_for('main_page'))

if __name__ == '__main__':
    app.run()
