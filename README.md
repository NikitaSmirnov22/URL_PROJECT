# CLI Interaction Instruction

**#1** To send a POST request to the **/process_urls** endpoint using curl, follow these steps:

1. Open a terminal window.
2. Type the following command(use input_urls_formatted.txt to fill in a bunch of urls) :

curl -X POST \
  http://localhost:8000/process_urls \
   -H 'Content-Type: application/json' \
   -d '{ 
       "urls": ["https://southdakotamastergardener.com/", "https://southdakotamastergardener.com/contact/", "https://www.sirinakornpaint.com/", "https://kryshtalevypalats.gov.ua/uk/kontakty/", "http://serpuhov.ru/", "https://www.dekorlamba.com/", "https://www.dekorlamba.com/iletisim"]
    }'

- In this command, we are sending a POST request to http://localhost:8000/process_urls endpoint with a JSON payload containing a list of URLs to be processed.
- Press Enter and wait for the response. The program will process the URLs and save the data in the SQLite database. Once the data is saved successfully, you will receive a JSON response containing a message and the data that was saved.

**#2** To send a POST request to the **/domain_statistics** endpoint using curl, follow these steps:

1. Open a terminal window.
2. Type the following command:

curl -X POST \
  http://localhost:8000/domain_statistics \
  -H 'Content-Type: application/json' \
  -d '{
        "domain_name": ["southdakotamastergardener.com", "ingvos.ru", "kryshtalevypalats.gov.ua"]
     }'
     
- In this command, we are sending a POST request to http://localhost:8000/domain_statistics endpoint with a JSON payload containing a list of domain names to get statistics for.
- Press Enter and wait for the response. The program will connect to the SQLite database and extract the data for the given domain names. Once the data is extracted successfully, you will
