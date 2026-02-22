import json
import os

class BaseManager:
    def __init__(self, filename):
        self.filename = filename

    def _load(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError) as e:

            print(f"Error: Invalid data in {self.filename}. {e}")
            return []

    def _save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)