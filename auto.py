from datetime import datetime
import os, re

def process(file_d, datasetn, datasetp, dataseto):
    if not os.path.isfile(file_d): 
         s1 = f"{file_d[11:]}.md"
         s = re.compile(rf"^\d{{4}}-\d{{2}}-\d{{2}}_{re.escape(s1)}$")
         for filename in os.listdir("_datasets"):
             if s.match(filename): 
                 v = filename[:-3]
    file_d = v
    file_p = os.path.join("_datasets", file_d + ".md")
    with open(file_p, "r", encoding="utf-8") as f:
         lines = f.readlines()
         today = datetime.today() 
         daymonthyear = today.strftime("%d%m%Y") 

         now = datetime.now() 
         month = now.strftime("%m") 
         day = now.strftime("%d") 
         year = now.strftime("%Y")
         
         datasetn_f = (
             datasetn.replace("%m", month) 
                 .replace("%d", day) 
                 .replace("%y", year) 
         )
         datasetp_f = (
             datasetp.replace("%m", month) 
                 .replace("%d", day) 
                 .replace("%y", year) 
         )
         dataseto_f = (
             dataseto.replace("%m", month) 
                 .replace("%d", day) 
                 .replace("%y", year) 
         )
         c = False
         if ";" in dataseto_f:
             l = dataseto_f.split(";") 
             c = True
             
         new_filename = os.path.join("_datasets", year + "-" + month + "-" + day + "_" + result =  datasetn_f.lower().replace(" ", "-") + "a" + daymonthyear + ".md")
         with open(new_filename, "w", encoding="utf-8") as f:
             for line in lines: 
                 if line.startswith("title:"):
                     f.write(f"title: {datasetn_f}\n")  
                 elif line.startswith("notes:"):
                     f.write(f"notes: {datasetp_f}\n") 
                 elif line.startswith("  - url:"):
                     if c is True:
                         dataseto_f = l.pop(0)
                     f.write(f"  - url: {dataseto_f}\n")  
                 elif line.startswith("    url:"):
                     if c is True:
                         dataseto_f = l.pop(0)
                     f.write(f"    url: {dataseto_f}\n")  
                 else:
                     f.write(line)


folder = "_auto"

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)

    if not os.path.isfile(path):
        continue

    frekvencia = None
    den = None
    file_d = None
    datasetn = None
    datasetp = None
    dataseto = None

    # Read file line by line
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("frekvencia:"):
                frekvencia = line.split(":", 1)[1].strip()
            elif line.startswith("den:"):
                den = line.split(":", 1)[1].strip()
            elif line.startswith("dataset:"):
                file_d = line.split(":", 1)[1].strip()
            elif line.startswith("datasetn:"):
                datasetn = line.split(":", 1)[1].strip()
            elif line.startswith("datasetp:"):
                datasetp = line.split(":", 1)[1].strip()
            elif line.startswith("dataseto:"):
                dataseto = line.split(":", 1)[1].strip()
            elif line.startswith("stav:"):
                enabled = line.split(":", 1)[1].strip()

    print(f"Processing {filename}")
    print(f"  frekvencia = {frekvencia}")
    print(f"  den = {den}")
    print(f"  subor = {file_d}")
    print(f"  datasetn = {datasetn}")
    print(f"  datasetp = {datasetp}")
    print(f"  dataseto = {dataseto}")
    print(f"  enabled = {enabled}")

    # Logic based on frekvencia
    if frekvencia == "denne" and enabled == "zapnuté":
        print("- Run job")
        process(file_d, datasetn, datasetp, dataseto)

    elif frekvencia == "týždenne" and enabled == "zapnuté":
        today = datetime.today().weekday() + 1
        if today == int(den):
            print("- Run job")
            process(file_d, datasetn, datasetp, dataseto)

    elif frekvencia == "mesačne" and enabled == "zapnuté":
        today = datetime.today().day
        if today == int(den):
            print("- Run job")
            process(file_d, datasetn, datasetp, dataseto)
 
    elif frekvencia == "ročne" and enabled == "zapnuté":
        today = datetime.today().timetuple().tm_yday
        if today == int(den):
            print("- Run job")
            process(file_d, datasetn, datasetp, dataseto)

    else:
        print("Neznáma frekvencia alebo vypnutá auto")



















