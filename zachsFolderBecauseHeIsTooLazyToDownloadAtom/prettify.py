import json

with open("metadata_dump.json", 'r') as in_file:
    with open("cleaned_metadata.json", 'w') as out_file:
        parsed = json.load(in_file)
        out_file.write(json.dumps(parsed, indent=4))
