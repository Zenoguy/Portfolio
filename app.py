from flask import Flask, request, render_template, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Route for the landing page
@app.route("/")
def home():
    return render_template("index.html")
    app.config['TEMPLATES_AUTO_RELOAD'] = True

# Route to handle contact form submission
@app.route("/send_message", methods=["POST"])
def send_message():
    # Get form data
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    
    # Prepare the message data
    message_data = {"name": name, "email": email, "message": message}
    
    # Check if the 'messages.json' file exists; if not, create it
    if not os.path.exists("messages.json"):
        with open("messages.json", "w") as f:
            json.dump([], f)
    
    # Open the file, load existing messages, and append the new message
    with open("messages.json", "r+") as f:
        messages = json.load(f)
        messages.append(message_data)
        f.seek(0)  # Go back to the beginning of the file to overwrite
        json.dump(messages, f, indent=4)
    
    # Return a JSON response (success message) to the front-end
    response = {
        "status": "success",
        "message": "Your message has been sent successfully!",
        "data": message_data
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

