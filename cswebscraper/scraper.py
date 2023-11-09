import requests
from bs4 import BeautifulSoup

def search_news():
    keyword = 'social engineering'
    keywords = keyword.split()
    keyword = '%20'.join(keywords)

    search_url = f"https://thehackernews.com/search/label/{keyword}"
    
    try:
        response = requests.get(search_url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # print(html_content)
        # <a> elements dhundne ke liye
        title_link_elements = soup.find_all('a')

        # titles aur links extract karo
        titles = [element.get_text() for element in title_link_elements]
        links = [element['href'] for element in title_link_elements]



        
        # Check if the request was successful
        if response.status_code == 200:
            # list ko required content ke hisab se sliced
            
            titlesnew = titles[34:45]
            linksnew = links[34:45]
            #print(titlesnew)
            
            i = 0
            while i < 11:
                try:
                    split = titlesnew[i].split("\n\n")
                    title = split[3][1:]
                    link = linksnew[i]
                    tags = split[4][14:]

                    print("Title:", title, "\n", "Link--", link, "\n","Topic:",tags,"\n")
                    # print("Title:",split[3][1:],"\n","Topic:",split[4][20:],"\n")
                    i += 1
                except:
                    i+=1
        else:
            print("Failed to retrieve search results.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # keyword = "cybersecurity"  # Keyword koi bhi daalo
    
    search_news()
