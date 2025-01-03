# Import required libraries
from flask import Flask, request  # Flask is a lightweight framework for web applications

# Initialize a Flask application
app = Flask(__name__)

# Define a route to handle incoming POST requests
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """
    This function handles incoming POST requests to the /webhook endpoint.
    The data is logged into a file for educational purposes.
    """
    # Extract the JSON data sent in the request
    data = request.get_json()
    print("Received data:", data)  # Print the data for debugging purposes

    # Write the received data to a log file (simulated data only)
    with open("webhook_data.log", "a") as log_file:
        log_file.write(str(data) + "\n")

    # Return a success response
    return {"status": "success"}

# Run the Flask application on localhost at port 5000
if __name__ == '__main__':
    app.run(port=5000)
