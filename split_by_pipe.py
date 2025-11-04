import os
import re

# Read the input file
with open("datasets.json", "r", encoding="utf-8") as f:
    content = f.read()

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