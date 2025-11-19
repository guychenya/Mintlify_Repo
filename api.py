from flask import Flask, request, jsonify
from flask_cors import CORS
import resend
import os

app = Flask(__name__)
CORS(app)

resend.api_key = os.getenv('RESEND_API_KEY')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    
    params = {
        "from": "onboarding@resend.dev",
        "to": ["info@reliatrak.org"],
        "subject": f"New Contact Form Submission from {data['name']}",
        "html": f"""
        <h2>New Contact Form Submission</h2>
        <p><strong>Name:</strong> {data['name']}</p>
        <p><strong>Email:</strong> {data['email']}</p>
        <p><strong>Company:</strong> {data.get('company', 'N/A')}</p>
        <p><strong>Message:</strong></p>
        <p>{data['message']}</p>
        """
    }
    
    try:
        resend.Emails.send(params)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
