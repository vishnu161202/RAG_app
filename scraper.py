import requests
from bs4 import BeautifulSoup

def scrape_tessell_blogs():
    url = "https://www.tessell.com/blogs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    blogs = [blog.text for blog in soup.find_all('h2')]
    with open("blogs.txt", "w") as f:
        for blog in blogs:
            f.write(blog + "\n")

if __name__ == "__main__":
    scrape_tessell_blogs()
