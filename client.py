from dotenv import load_dotenv
import os

load_dotenv()
SERVER_IP_ADDRESS = os.getenv('SERVER_IP_ADDRESS', '127.0.0.1')

def main():
    print(f"Connecting to server at {SERVER_IP_ADDRESS}")

if __name__ == "__main__":
    main()
