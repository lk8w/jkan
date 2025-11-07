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
os.makedirs("lkod", exist_ok=True)

d = ''

# Process each part
for i, part in enumerate(parts):
    # Try to find the "iri" value
    match = re.search(r'"iri"\s*:\s*"([^"]+)"', part)
    if match:
        iri_url = match.group(1)
        filename = iri_url.rstrip("/").split("/")[-1]
        d = d + '\"https://katalog.reframe.sk/lkod/' +filename + '\",\n' 
    else:
        filename = f"part_{i+1}"
        d = d + '\"https://katalog.reframe.sk/lkod/' +filename + '\",\n' 

    # Save the part to a file
    with open(f"lkod/{filename}", "w", encoding="utf-8") as out:

        out.write(part.strip())

# delete last comma
d = d[:-2]

lkod1 = '{\n\"@context\": \"https://data.slovensko.sk/dcat3.jsonld\",\n'
lkod1 = lkod1 + '\"iri\": \"https://katalog.reframe.sk/lkod/lkod",\n'
lkod1 = lkod1 + '\"typ\": \"Katalóg\",\n\"názov\": {\n'
lkod1 = lkod1 + '\"sk\": \"Katalóg otvorených dát mesta Ilava\"\n},\n'
lkod1 = lkod1 + '\"popis\": {\n\"sk\": "Katalóg otvorených dát mesta Ilava\"\n},\n'
lkod1 = lkod1 + '\"kontaktný_bod\": {\n\"typ\": \"Organizácia\",\n\"meno\": {\n'
lkod1 = lkod1 + '\"sk\": \"Mesto Ilava\"\n},\n'
lkod1 = lkod1 + '\"e-mail\": \"mailto:opendata@ilava.sk\"\n},\n'
lkod1 = lkod1 + '\"domovská_stránka\": \"https://www.opendata.ilava.sk\",\n'
lkod1 = lkod1 + '\"poskytovateľ\": \"https://data.gov.sk/id/legal-subject/00317331\",\n'
lkod1 = lkod1 + '\"dataset\": [\n'
lkod1 = lkod1 + d
lkod1 = lkod1 + ']\n}'

lkod1 = lkod1.replace("%", "%25")

with open(f"lkod/lkod", "w", encoding="utf-8") as out1:
	out1.write(lkod1)

