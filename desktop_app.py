import sys
import threading
import time
import webbrowser
from urllib.request import urlopen

# Import the Flask app
from app import app

def start_flask():
    """Start the Flask application on a specific port"""
    app.run(host='127.0.0.1', port=5000, debug=True)

def check_server_started(url, timeout=10):
    """Check if the server has started by polling the URL"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = urlopen(url)
            if response.status == 200:
                return True
        except:
            time.sleep(0.1)
    return False

def main():
    """Main function to start the desktop application"""
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # URL of the Flask application
    url = "http://127.0.0.1:5000"
    
    # Wait for the server to start
    if check_server_started(url):
        # Open the default web browser
        webbrowser.open(url)
    else:
        print("Failed to start the server.")
        sys.exit(1)
    
    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
