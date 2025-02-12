def greet():
    print("Hello, World!")

def display_servers():
    servers = [
        "lme-mandc-app-frontend",
        "lme-crd-app-frontend",
        "lme-mandc-app-server",
        "lme-mandc-app-sse-express"
    ]
    print("Here are the server addresses and applications:")
    for server in servers:
        print(f"- {server}")

if __name__ == "__main__":
    greet()
    display_servers()
