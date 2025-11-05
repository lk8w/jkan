import os
import re
import requests

# Read the input file
url = "https://katalog.reframe.sk/datasets.json"
response = requests.get(url)
response.raise_for_status()
content = response.text

# Split the content by pipe character
parts = content.split("|")

# Create output directory
os.makedirs("output", exist_ok=True)

# Process each part
for i, part in enumerate(parts):
    # Try to find the "iri" value
    match = re.search(r'"iri"\s*:\s*"([^"]+)"', part)
    if match:
        iri_url = match.group(1)
        filename = iri_url.rstrip("/").split("/")[-1]
    else:
        filename = f"part_{i+1}"

    # Save the part to a file
    with open(f"output/{filename}", "w", encoding="utf-8") as out:

        out.write(part.strip())


