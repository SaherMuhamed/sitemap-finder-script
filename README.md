# Sitemap Scanner
A Python script that crawls through a target website and extracts all the links it can find. It then recursively follows each link to extract more links, creating a spider-like structure. The script is designed to scan websites and display all the discovered links on the console.

## Requirements
Before running the script, make sure you have the following installed:
- Python 3x
- Requests library: You can install it using pip: `pip install requests`

## Usage
To start use the script, follow these steps:
1. Clone or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:
    ```commandline
    python3 sitemap_finder.py <target_url>
    ```
4. Replace <target_url> with the URL of the website you want to scan.

## Key Features
- **URL Crawling:** The spider scanner starts from a specified target URL and recursively follows each link found on the page, building a comprehensive map of the website's link structure.

- **URL Extraction:** The script extracts links from the HTML content of each page using regular expressions. This allows the spider to identify URLs regardless of the page's complexity or structure.

- **URL Normalization:** The scanner uses the urllib.parse.urljoin function to normalize extracted links and ensure they are complete URLs. It handles relative URLs, making sure they are combined with the base URL appropriately.

- **Command-line Interface (CLI):** The scanner provides a CLI for easy usage. Users can specify the target URL using the -u or --url option, making it straightforward to start scanning any website.

- **Graceful Error Handling:** The scanner gracefully handles invalid URLs and connection errors, allowing it to continue scanning other links even if it encounters issues with specific URLs.

## Output
- The script will start scanning the target website and its linked pages. It will display all the discovered links on the console, starting from the provided target URL and recursively following each link found.
- The links will be printed in green to easily distinguish them from other output.

## Screenshots
![](screenshots/Screenshot_2023-07-21_18-34-08.png)

## Notes
- The script utilizes requests library to make HTTP requests and re (regular expressions) to extract links from the HTML content.
- The scanning process is recursive, meaning it will follow each link to discover more links until it exhausts all possibilities or the user interrupts the program using `ctrl + c`.
- If an invalid URL or connection error is encountered for a particular link, the script will gracefully handle the error and continue scanning other links.

## Disclaimer
This script is intended for educational and ethical use only. You should have permission to scan and access the target website. Unauthorized scanning of websites may violate the law and can lead to legal consequences. Use it responsibly and at your own risk.

## Author
The "Website Spider Scanner" script was developed by **Saher Muhamed**.
