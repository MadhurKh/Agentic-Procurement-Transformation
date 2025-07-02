def route_approval(document_type):
    if document_type == "contract":
        return "Send to Legal Team"
    elif document_type == "payment":
        return "Send to Finance Team"
    else:
        return "Send to Procurement Lead"

if __name__ == "__main__":
    print(route_approval("contract"))
