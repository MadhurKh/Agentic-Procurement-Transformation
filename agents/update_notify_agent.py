def update_dashboard(status):
    print(f"Dashboard updated with status: {status}")

def send_email(recipient, message):
    print(f"Email sent to {recipient}: {message}")

if __name__ == "__main__":
    update_dashboard("Supplier Onboarding Complete")
    send_email("procurement@company.com", "New supplier added: Acme Ltd")
