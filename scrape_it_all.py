from bs4 import BeautifulSoup
import requests

# Add header and  url
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
url = "https://projecteuclid.org/journals/bayesian-analysis/volume-{}/issue-{}"

years_published = range(2006, 2023)
issue_count = range(1,5)
volume = 1

for year in years_published:
    for issue in issue_count:
        r = requests.get(url.format(volume, issue))
        # Initiate beautiful soup
        soup = BeautifulSoup(r.content, "html.parser")
        abstracts = soup.find_all("div",class_="anchorrel")
        for abstract in abstracts:
            for string in abstract.strings:
                with open("out.csv", "a", encoding="utf-8") as out_file:
                    try:
                        out_file.write(string)
                    except UnicodeEncodeError:
                        out_file.write(string.encode("utf-8"))
                    out_file.close()
    # after this year's publication has been scrapped
    volume = volume + 1

