# URL_PROJECT 
 This project is a Flask web application that processes a list of URLs, extracts relevant data, and saves it to a SQLite database. It also provides an endpoint for retrieving statistics about the URLs based on their domain name. The repository includes the code for the Flask app and a sample SQLite database.

The script imports several necessary libraries including:

**urlparse from urllib.parse:** a library that provides functionality to parse URLs into their various components.

**Flask, request, and jsonify from flask:** a lightweight web framework for building web applications, and utilities for working with HTTP requests and JSON data.

**requests:** a library for making HTTP requests and handling responses.

**BeautifulSoup from bs4:** a library for parsing HTML and XML documents.

**The code defines two endpoints for the web application:**

1)**process_urls:** this endpoint processes a list of URLs passed in the request payload, and saves data for each URL to a SQLite database. The function splits the URLs into batches of 10 for parallel processing using concurrent.futures.ThreadPoolExecutor(). The process_url function is executed in parallel for each URL in the batch using the executor.submit method. The save_data function is called to store the data returned from process_url in a SQLite database. The function returns a JSON response indicating whether the data was saved successfully, and the data for each URL.

2)**domain_statistics:** this endpoint retrieves statistics for a given list of domain names from the data stored in the SQLite database. The function accepts a list of domain names as a request payload, and queries the database to get the data for each domain name. It then calculates the total number of pages and active pages for each domain name and returns a JSON response with the statistics and a list of URLs for each domain name.

The code also defines **three helper functions**:

a) **process_url:** this function takes a URL as input and returns a dictionary containing the URL, the final URL after redirection (if any), the HTTP status code, the final HTTP status code (if any), the title of the web page (if available), and the domain name.

b) **save_data:** this function takes the processed data for a URL as input and saves it to a SQLite database.

c) **warnings.filterwarnings:** this line filters UserWarnings generated by BeautifulSoup.

The code connects to a SQLite database named webpage.db using the sqlite3 library. The webpage_data table is created (if it doesn't exist) with the following columns:

**id:** an auto-incrementing primary key

**url:** the URL of the web page

**status_code:** the HTTP status code of the web page

**final_url:** the final URL after redirection (if any)

**final_status_code:** the final HTTP status code (if any)

**title:** the title of the web page (if available)

**domain_name:** the domain name of the web page

When the web application is run, it listens for incoming HTTP requests on the default Flask port 8000.
