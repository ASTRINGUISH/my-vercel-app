import json
from http.server import BaseHTTPRequestHandler

# Example student marks
student_marks = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78,
    "David": 92,
    "Eva": 88,
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract query parameters
        query = self.parse_query(self.path)
        names = query.get('name', [])

        # Prepare response
        marks = [student_marks.get(name, None) for name in names]
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
