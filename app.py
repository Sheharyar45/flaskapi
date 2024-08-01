from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app, resources={r"/submit-comment": {"origins": "*"}})
  # Enable CORS for all domains on all routes

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'sheharyarmeghani@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'ayof ihjr weli jkxn')
app.config['MAIL_DEFAULT_SENDER'] = 'sheharyarmeghani@gmail.com'

mail = Mail(app)

@app.route('/submit-comment', methods=['POST'])
def submit_comment():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        comment = data.get('comment')

        msg = Message('New Comment Submitted', recipients=['sheharyarmeghani@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nComment: {comment}"
        mail.send(msg)
    except Exception as e:
        # Log the error and return a 500 response
        print(f"An error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

    return jsonify({'message': 'Comment submitted successfully!'}), 200
        
    

if __name__ == '__main__':
    app.run(debug=True)
