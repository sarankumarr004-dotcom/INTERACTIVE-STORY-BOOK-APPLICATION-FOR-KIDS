from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from stories_data import stories
import os

# ─── Configuration ─────────────────────────────────────────────
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'frontend')

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path='')
CORS(app)

# ─── Demo Users ───────────────────────────────────────────────
USERS = {
    "kid": "magic",
    "admin": "password123"
}

# ─── Serve Frontend Files ─────────────────────────────────────
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'login.html')

# Catch-all to serve any static file from the root
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# ─── API: Login ───────────────────────────────────────────────
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data:
        return jsonify({"success": False, "message": "No data provided"}), 400

    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    if not username or not password:
        return jsonify({"success": False, "message": "Please fill in all fields"}), 400

    if username in USERS and USERS[username] == password:
        return jsonify({"success": True, "message": "Welcome to the magic world!"})
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401

# ─── API: List Stories ────────────────────────────────────────
@app.route('/stories', methods=['GET'])
def get_stories():
    story_list = []
    for key, val in stories.items():
        story_list.append({
            "id": key,
            "title": val["title"],
            "theme_color": val["theme_color"],
            "line_count": len(val["lines"])
        })
    return jsonify(story_list)

# ─── API: Get Single Story ────────────────────────────────────
@app.route('/story/<story_type>', methods=['GET'])
def get_story(story_type):
    if story_type in stories:
        return jsonify(stories[story_type])
    else:
        return jsonify({"error": "Story not found"}), 404

# ─── Run Server ───────────────────────────────────────────────
if __name__ == '__main__':
    print("="*50)
    print("  🌟 Magic Stories Backend is Running!")
    print("  📡 API endpoints: /login, /stories, /story/<type>")
    print("  🌐 Open: http://127.0.0.1:5000")
    print("="*50)
    app.run(debug=True, port=5000)
