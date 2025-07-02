import random

def suggest_terms(supplier_info):
    options = ["Net 30", "Net 45 with 2% discount", "Net 60"]
    selected = random.choice(options)
    return f"Suggested Terms for {supplier_info['name']}: {selected}"

if __name__ == "__main__":
    supplier = {"name": "Acme Ltd"}
    print(suggest_terms(supplier))
