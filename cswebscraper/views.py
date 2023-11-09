from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import Article

# Create your views here.
# def index(requests):
#     return HttpResponse("This is index")

def search_news(request):
    keyword = request.GET.get('keyword', '')
    keywords = keyword.split()
    keyword = '%20'.join(keywords)

    search_url = f"https://thehackernews.com/search/label/{keyword}"
    
    try:
        Article.objects.all().delete()
        response = requests.get(search_url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # <a> elements dhundne ke liye
        title_link_elements = soup.find_all('a')


        # titles aur links extract karo
        titles = [element.get_text() for element in title_link_elements]
        links = [element['href'] for element in title_link_elements]

        
        # Check if the request was successful
        if response.status_code == 200:
            # list ko required content ke hisab se sliced
            
            titlesnew = titles[34:]
            linksnew = links[34:]
            # print(titlesnew)

            search_results = []
            
            i = 0
            while i < 24:
                try:
                    split = titlesnew[i].split("\n\n")
                    title = split[3][1:]
                    link = linksnew[i]
                    tags = split[4][14:]
                    tagslist = tags.split(" / ")
                    # Create a new Article object and save it to the database
                    article = Article()
                    article.title = title
                    article.link = link
                    article.tag1 = tagslist[0]
                    article.tag2 = tagslist[1]
                    article.save()
                    # print("data is coming", title, link)
                    search_results.append(article)

                    # print("Title:", title, "\n", "Link--", link, "\n")
                    i += 1
                except:
                    i+=1
        else:
            print("Failed to retrieve search results.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return render(request, "keyword.html", {"articles": search_results})
