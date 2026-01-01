## Real Estate Listings - HTML for Web Scraping Practice

### Project Overview
This project is a static HTML real-estate listings page built to simulate the structure of real-world property listing websites.
It is intentionally designed to be **easy to scrape** using tools like **BeautifulSoup**, making it a foundation for data collection and analysis projects.

The focus is not styling, but **clean, semantic HTML structure** that mirrors how data appears on actual property platforms.

### Data Available on the Page
Each property listing contains the following structured data:
* Property title
* Price
* Location
* Property type
* Number of bedrooms
* Number of bathrooms
* Agent name
* Date Posted

Each listing uses a **consistent HTML structure** to enable reliable scraping.

### HTML Design Choices
* Each property is wrapped in an `<article>` tag
* Semantic elements (`header, main, section, footer`) are used throughout
* Class names are consistent across listings to support automated extractions
* Dates are stored using the <`time`> tag with a `datetime` attribute

These choices closely reflect how real websites structure data.

### Intended Use
This project serves as:
* A learning exercise for understanding HTML DOM structure
* A preparation step for web scraping with BeautifulSoup
* A base for future data science projects such as:
    * Property price analysis
    * Location-based price comparison
    * Feature vs price modeling

### Next Steps
* Scrape the HTML page using BeautifulSoup
* Convert extracted data into a pandas DataFrame
* Perform exploratory data analysis (EDA)
* Extend the scraper to real property listing websites