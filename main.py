import json
import requests

key = "AIzaSyB3O7rrXNzMCbD1dK3Kmme_yCx3PruCVwk"

with open('metadata_dump.json', 'r') as handle:
    parsed = json.load(handle)
    print(json.dumps(parsed, indent=4))
