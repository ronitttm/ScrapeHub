# keyword = 'social '
# keywords = keyword.split()
# keyword = '%20'.join(keywords)
# print(keyword)
import spacy
import requests
from bs4 import BeautifulSoup

def search_news():
    keyword = 'social engineering'
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(keyword)

    # Tokenization
    tokens = [token.text for token in doc]
    print("Tokens:", tokens)
#     keywords = keyword.split()
#     keyword = '%20'.join(keywords)

#     search_url = f"https://thehackernews.com/search/label/{keyword}"
#     # search_url = f"https://thehackernews.com/"
    
#     try:
#         response = requests.get(search_url)
#         html_content = response.text
#         soup = BeautifulSoup(html_content, 'html.parser')
#         # <a> elements dhundne ke liye
#         title_link_elements = soup.find_all('a')

#         # titles aur links extract karo
#         titles = [element.get_text() for element in title_link_elements]
#         links = [element['href'] for element in title_link_elements]



        
#         # Check if the request was successful
#         if response.status_code == 200:
#             # list ko required content ke hisab se sliced
            
#             titlesnew = titles[34:]
#             linksnew = links[34:]
#             print(titlesnew)
#             i = 0
#             while i < 24:
#                 try:
#                     split = titlesnew[i].split("\n\n")
#                     title = split[3][1:]
#                     link = linksnew[i]

#                     print("Title:", title, "\n", "Link--", link, "\n")
#                     i += 1
#                 except:
#                     i+=1
#         else:
#             print("Failed to retrieve search results.", search_url)
            
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # keyword = "cybersecurity"  # Keyword koi bhi daalo
    
    search_news()