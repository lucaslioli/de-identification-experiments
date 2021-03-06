import glob                             # Read files from folder
from bs4 import BeautifulSoup as bs     # Parse XML files
from pprint import pprint               # Prettify the array print

# 2014i2b2 tests
# The patient's condition is currently stable
# Diagnosis:  Left ankle fracture

# MEDDOCAN tests
# Diagnóstico Principal:  tumor paratesticular izquierdo.
# Tratamiento: ciclos de quimioterapia con adriamicina e ifosfamida + MESNA.
# Evolución y comentarios: En estos momentos el paciente es dependiente para funciones básicas ...

DATA = "2014i2b2"
SEED = "condition"

if __name__ == '__main__':

    # Get all XML files from a folder
    files = glob.glob("dataset/{}/**/*.xml".format(DATA), recursive=True)

    docs = 0
    file_names = []

    # Process all files in the folder
    for file in files:
        # Read data file and parse the XML
        with open(file, mode='r', encoding='utf-8-sig') as infile:
            soup = bs(infile, "html.parser")

            # Get the pacient note text
            record = soup.find("text").text

            for w in record.split(" "):
                if(SEED in w.lower()):
                    docs += 1
                    file_names.append(file)
                    break
        
    print("\n> Dataset {}: from {} records, {} contain the term '{}'".format(DATA, len(files), docs, SEED))
    print("> Some file names containing the term:\n")
    pprint(file_names[:10])