from bs4 import BeautifulSoup
import pandas as pd

#Opening the HTML file
with open("index.html", "r", encoding = "utf-8") as file:
    html = file.read()

# Parsing HTML with BeautifulSoup
soup = BeautifulSoup(html, "lxml")

# Finding all property cards
property_cards = soup.find_all("article", class_ = "property-card")

# The list to store data
properties = []

for card in property_cards:
    title = card.find("h2", class_ = "property-title").text.strip()
    price = card.find("p", class_ = "property-price").text.strip()
    location = card.find("p", class_ = "property-location").text.strip()

    details = card.find("section", class_ = "property-details")
    bedrooms = details.find("li", class_ = "bedrooms").text.strip()
    bathrooms = details.find("li", class_ = "bathrooms").text.strip()
    property_type = details.find("li", class_ = "property-type").text.strip()

    meta = card.find("section", class_ = "property-meta")
    agent = meta.find("p", class_ = "agent-name").text.replace("Agent:", "").strip()
    date_posted = meta.find("time", class_ = "date-posted").text.strip()

    #Adding to list
    properties.append({
        "Title": title,
        "Price": price,
        "Location": location,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Type": property_type,
        "Agent": agent,
        "Date Posted": date_posted
    })


# Creating a DataFrame
df = pd.DataFrame(properties)

print(df)

df.to_csv("properties.csv", index=False, encoding = "utf-8-sig")