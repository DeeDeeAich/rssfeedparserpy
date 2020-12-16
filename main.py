import feedparser

url = feedparser.parse(input("Please enter an rss feed url: "))

for i in range(0, 11):
    try:
        print(url["entries"][i]["title_detail"]["value"])
        print(url["entries"][i]["id"])
        print("Published: " + url["entries"][i]["published"])
        print("\n")
    except KeyError:
        continue
    except IndexError:
        continue
