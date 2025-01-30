import json
from http.server import BaseHTTPRequestHandler

# Load student marks from the JSON file
def load_student_marks():
    try:
        with open("q-vercel-python.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Load student marks from the JSON file
        student_marks = load_student_marks()

        # Extract query parameters (the 'name' parameters)
        query = self.parse_query(self.path)
        names = query.get('name', [])

        # Check if names exist in the student_marks dictionary
        marks = []
        for name in names:
            mark = student_marks.get(name)
            if mark is None:
                marks.append("Name not found")  # Or use a default value like 0
            else:
                marks.append(mark)

        # Prepare response
        response = {"marks": marks}

        # Return JSON response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow CORS
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def parse_query(self, path):
        """Helper function to parse query parameters from URL."""
        query = {}
        if '?' in path:
            path = path.split('?')[1]
            for param in path.split('&'):
                key, value = param.split('=')
                query.setdefault(key, []).append(value)
        return query
