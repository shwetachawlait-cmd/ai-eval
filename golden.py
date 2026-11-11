import csv
import pytest

def split(text):
    """'a; b' -> ['a', 'b'] in lowercase."""
    return [x.strip().lower() for x in (text or "").split(";") if x.strip()]

def load_rows(path="golden.csv"):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

#def params():
    #"""Turn each golden row into one pytest case, labelled with its tier."""
    #out = []
   # for row in load_rows():
  #      marks = [pytest.mark.smoke] if row["tier"] == "smoke" else []
 #       out.append(pytest.param(row, marks=marks, id=row["id"]))
#    return out

