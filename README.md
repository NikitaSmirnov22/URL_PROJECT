# CLI Interaction

To send a POST request to the **/process_urls** endpoint using curl, follow these steps:

1. Open a terminal window.
2. Type the following command(use input_urls_formatted.txt to fill in a bunch of urls) :
curl --header "Content-Type: application/json" --request POST --data '{"urls":["put your url here", "put your url here", ""put your url here"]}' http://localhost:8000/process_urls

- In this command, we are sending a POST request to http://localhost:8000/process_urls endpoint with a JSON payload containing a list of URLs to be processed.
- Press Enter and wait for the response. The program will process the URLs and save the data in the SQLite database. Once the data is saved successfully, you will receive a JSON response containing a message and the data that was saved.

