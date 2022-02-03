import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/90.0.4430.212 Safari/537.36',
			'Accept-Language': 'en-US, en;q=0.5'})

# user define function
# Scrape the data
def getdata(url):
	r = requests.get(url, headers=HEADERS)
	return r.text


def html_code(url):

	# pass the url
	# into getdata function
	htmldata = getdata(url)
	soup = BeautifulSoup(htmldata, 'html.parser')

	# display html code
	return (soup)

def get_revs_link(url):
    all_revs_link = []
    while len(all_revs_link) == 0:
        soup = html_code(url)
        all_revs_link = soup.find("a",{'data-hook':"see-all-reviews-link-foot"})
        print(all_revs_link)
    return all_revs_link

def get_revs(url, stars):
    reviews = []
    new_ratings = []
    names_text = []
    revs_href = get_revs_link(url)
    print(revs_href)
    try: 
        link = revs_href['href']
    except:
        link = None
    if link is not None:
        print(link)
        root_link = "https://www.amazon.in"+link
        print(root_link)
        for k in range(10):
            final_link = root_link+'&pageNumber='+str(k+1)+'&filterByStar='+stars
            print(final_link)
            soup=html_code(final_link)

            all_revs = soup.findAll("span",{'data-hook':"review-body"})
            if len(all_revs) == 0:
                break
            for i in all_revs:
                reviews.append(i.text)
            
            ratings = soup.findAll("i",{'data-hook':"review-star-rating"})
            for i in ratings:
                new_ratings.append(int(i.text.split()[0].split(".")[0]))
            
            names = soup.findAll("span",{'class':"a-profile-name"})
            for i in names:
                names_text.append(i.text)

            

    return [names_text, new_ratings, reviews]

            # names = soup.findAll("span",{'class':"a-profile-content"})
            # names_text = [name.text.strip() for name in names]
            # ratings = soup.findAll("i",{'data-hook':"review-star-rating"})
            # ratings_text = [rating.text.strip() for rating in ratings]
            