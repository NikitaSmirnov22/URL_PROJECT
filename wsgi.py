
#script to run flask app

from app import app

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000, threaded=True, processes=4, timeout=300)