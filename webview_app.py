import threading
import webview
import sys
import os
import time
from urllib.request import urlopen

# Import the Flask app
from app import app

def start_flask():
    """Start the Flask application on a specific port"""
    app.run(host='127.0.0.1', port=5000, debug=False)

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
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # URL of the Flask application
    url = "http://127.0.0.1:5000"
    
    # Wait for the server to start
    if check_server_started(url):
        # Create a window with the web view
        webview.create_window("To-Do List App", url, width=800, height=600, resizable=True)
        webview.start()
    else:
        print("Failed to start the server.")
        sys.exit(1)

if __name__ == "__main__":
    main()
