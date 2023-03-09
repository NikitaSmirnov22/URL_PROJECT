
#importing necessary libraries
from urllib.parse import urlparse
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import sqlite3
import concurrent.futures
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

app = Flask(__name__)


""" ENDPOINT #1 """

#route for processing URLs and saving them in a webpage.db
@app.route('/process_urls', methods=['POST'])
def process_urls():
    urls = request.json.get("urls")
    result = []

    #splitting URLs for batch processing 
    url_batches = [urls[i:i+10] for i in range(0, len(urls), 10)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for batch in url_batches:
            futures = [executor.submit(process_url, url) for url in batch]
            for future in concurrent.futures.as_completed(futures):
                data = future.result()
                result.append(data)
                save_data(data['url'], data['status_code'], data['final_url'], data['final_status_code'], data['title'], data['domain_name'])
    
    return jsonify({"message": "Data saved successfully!", "data": result})

#function to process urls and get url, status_code, final_url, final_status_code, title, domain_name
def process_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title is not None else ""
        domain_name = urlparse(url).netloc
        final_url = response.url if response.history else url
        final_status_code = response.status_code if response.history else None
        status_code = response.status_code
        data = {
            "url": url,
            "final_url": final_url,
            "final_status_code": final_status_code,
            "status_code": status_code,
            "title": title,
            "domain_name": domain_name
        }
        return data
    except requests.exceptions.RequestException as ex:
        print("An error occurred:", ex)
        data = {
            "url": url,
            "final_url": None,
            "final_status_code": None,
            "status_code": None,
            "title": None,
            "domain_name": None
        }
        return data

#function to create table, connect to db and save the data to SQLite
def save_data(url, status_code, final_url, final_status_code, title, domain_name):
    with sqlite3.connect('webpage.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS webpage_data 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                url TEXT NOT NULL, 
                status_code INTEGER, 
                final_url TEXT, 
                final_status_code INTEGER, 
                title TEXT, 
                domain_name TEXT)
                ''')
            cursor.execute('''
                INSERT INTO webpage_data (url, status_code, final_url, final_status_code, title, domain_name) 
                VALUES (?, ?, ?, ?, ?, ?) 
                ''', (url, status_code, final_url, final_status_code, title, domain_name))
            conn.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        finally:
            cursor.close()


""" ENDPOINT #2 """

#route for getting statistics of domain_name, active_page_count, total_page_count and url_list
@app.route('/domain_statistics', methods=['POST'])
def domain_statistics():
    domain_names = request.json.get("domain_name")

    #checking for domain_name parameter presence
    if not domain_names:
        return jsonify({"error": "domain_name parameter is missing"}), 400

    # Connecting to db and extract data for the given domain_name
    with sqlite3.connect('webpage.db') as conn:
        cursor = conn.cursor()
        data = []
        for domain_name in domain_names:
            cursor.execute("SELECT url, status_code FROM webpage_data WHERE domain_name=?", (domain_name,))
            domain_data = cursor.fetchall()
            active_page_count = sum([1 for url, status_code in domain_data if status_code == 200])
            total_page_count = len(domain_data)
            url_list = [url for url, status_code in domain_data]
            data.append({"domain_name": domain_name, "active_page_count": active_page_count,
                         "total_page_count": total_page_count, "url_list": url_list})
        
        return {"data": data}




