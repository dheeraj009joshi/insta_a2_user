from instagrapi import Client
import random  



from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query/user/a2', methods=['POST'])
def submit():
    data = request.get_json()

    # Validate input
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    username = data.get("username")
    sessions = data.get("sessions")

    if not username or not isinstance(username, str):
        return jsonify({"error": "Username must be a string"}), 400

    
    cl=Client()
    session_id=random.choice(sessions)
    print(cl.get_settings())
    user=cl.user__info_by_username_a2(username)

    return jsonify({
        "message": "Data received successfully",
        "user": user,
        "sessions":session_id
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
