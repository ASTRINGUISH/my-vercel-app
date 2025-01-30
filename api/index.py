import json
from http.server import BaseHTTPRequestHandler

# Hardcoded student marks data
student_marks = [
    {"name": "S8bYc", "marks": 82},
    {"name": "xMGNvCBr", "marks": 6},
    {"name": "nlsf", "marks": 55},
    {"name": "QORfpl", "marks": 11},
    {"name": "Qo", "marks": 64},
    {"name": "15kGxIqEV", "marks": 87},
    {"name": "ovle", "marks": 55},
    {"name": "Ny6ephU0l", "marks": 93},
    {"name": "XYY32vaJ", "marks": 71},
    {"name": "ok", "marks": 37},
    {"name": "TFEw622", "marks": 16},
    {"name": "9bkk", "marks": 3},
    {"name": "9peIcvbx", "marks": 53},
    {"name": "1d1W3hXC", "marks": 1},
    {"name": "2aoV9KPix", "marks": 55},
    {"name": "2PvF4u", "marks": 33},
    # Add more names if necessary
]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract query parameters (the 'name' parameters)
        query = self.parse_query(self.path)
        names = query.get('name', [])

        # Find the marks for each name in the query in the correct order
        marks = []
        for name in names:
            # Look for the student's name in the student_marks data
            student = next((s for s in student_marks if s["name"] == name), None)
            if student is None:
                marks.append(None)  # Use `None` for names not found
            else:
                marks.append(student["marks"])

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
