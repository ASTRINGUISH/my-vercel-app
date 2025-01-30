import json
from http.server import BaseHTTPRequestHandler

# Hardcoded student marks data
student_marks = [
    {"name":"S8bYc","marks":82},{"name":"xMGNvCBr","marks":6},{"name":"nlsf","marks":55},{"name":"QORfpl","marks":11},{"name":"Qo","marks":64},{"name":"15kGxIqEV","marks":87},{"name":"ovle","marks":55},{"name":"Ny6ephU0l","marks":93},{"name":"XYY32vaJ","marks":71},{"name":"ok","marks":37},{"name":"TFEw622","marks":16},{"name":"9bkk","marks":3},{"name":"9peIcvbx","marks":53},{"name":"1d1W3hXC","marks":1},{"name":"2aoV9KPix","marks":55},{"name":"2PvF4u","marks":33},{"name":"bB3XSaW","marks":6},{"name":"YNxl3S","marks":11},{"name":"QI","marks":58},{"name":"ya06","marks":19},{"name":"DIzxqWKon","marks":35},{"name":"OwWWt","marks":25},{"name":"PWMrX2JVxA","marks":62},{"name":"fFyeD","marks":47},{"name":"oHl6","marks":94},{"name":"EuEYs","marks":53},{"name":"7OFVD","marks":15},{"name":"EWMGLgGbz","marks":15},{"name":"xfo","marks":59},{"name":"umvqZiN69d","marks":97},{"name":"mPngwS610T","marks":85},{"name":"lonB2","marks":89},{"name":"2voSA","marks":37},{"name":"nyT","marks":48},{"name":"scAd","marks":37},{"name":"xw","marks":58},{"name":"RlEc","marks":99},{"name":"nB2m","marks":99},{"name":"hfr","marks":22},{"name":"cIt","marks":29},{"name":"j","marks":43},{"name":"dbu","marks":0},{"name":"cOhSD","marks":24},{"name":"OHzs","marks":69},{"name":"1vLw","marks":17},{"name":"7njqX","marks":71},{"name":"evpSrNztx","marks":25},{"name":"UHLgR2p36B","marks":54},{"name":"a3CZoF","marks":68},{"name":"EEdA","marks":57},{"name":"XGyEq4kqIZ","marks":6},{"name":"s","marks":63},{"name":"2WEi","marks":11},{"name":"HVTkwFn","marks":55},{"name":"G0J","marks":85},{"name":"h5AE3q3","marks":92},{"name":"73s9bl","marks":24},{"name":"GFqA","marks":97},{"name":"lTOwepbVq","marks":15},{"name":"z5PVg6","marks":36},{"name":"b","marks":85},{"name":"6D4aHQBF","marks":82},{"name":"C8kYLOiy0c","marks":20},{"name":"XyNmqM","marks":31},{"name":"eQZeZJyf","marks":43},{"name":"J1","marks":82},{"name":"3QHmyds","marks":82},{"name":"xJDXJ1t","marks":64},{"name":"AXL","marks":97},{"name":"3","marks":72},{"name":"mhvExkqt1i","marks":57},{"name":"L","marks":50},{"name":"9lYazJmHpb","marks":58},{"name":"FyaxGrVn0p","marks":13},{"name":"EEoJqWwmy","marks":5},{"name":"Im","marks":22},{"name":"WCMVv4c","marks":71},{"name":"MB9","marks":24},{"name":"2pT9bz9O","marks":3},{"name":"1H","marks":17},{"name":"YE1qE","marks":76},{"name":"9","marks":3},{"name":"l8Zx","marks":10},{"name":"AVgpX4qN6","marks":51},{"name":"9l8G78X","marks":1},{"name":"ZqjRAX","marks":22},{"name":"9QC","marks":67},{"name":"lzXYK","marks":85},{"name":"k4H32","marks":57},{"name":"RMP","marks":93},{"name":"ZSIeAT","marks":46},{"name":"yaeqe","marks":64},{"name":"B6Q","marks":73},{"name":"QBfipPJFX","marks":21},{"name":"72mQpi","marks":7},{"name":"l","marks":57},{"name":"3B","marks":96},{"name":"8jTZ6","marks":84},{"name":"erH12IKe","marks":94},{"name":"6","marks":45}
]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract query parameters (the 'name' parameters)
        query = self.parse_query(self.path)
        names = query.get('name', [])

        # Find the marks for each name
        marks = []
        for name in names:
            # Look for the student's name in the student_marks data
            student = next((s for s in student_marks if s["name"] == name), None)
            if student is None:
                marks.append("Name not found")  # Or use a default value like 0
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
