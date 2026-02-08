import subprocess
import time
import requests
import json

def start_server_and_test():
    # Start the server in a subprocess
    server_process = subprocess.Popen([
        "py", "-3.13", "-m", "uvicorn", "main:app", 
        "--host", "127.0.0.1", "--port", "8002", "--log-level", "info"
    ], cwd=r"D:\amna.riaz\todo-app\todo-app\PhaseII\backend")
    
    # Give the server some time to start
    time.sleep(5)
    
    try:
        print("Testing the API...")
        
        # Test the registration endpoint
        register_data = {
            "email": "test@example.com",
            "name": "Test User",
            "password": "testpassword123"
        }
        
        response = requests.post(
            "http://127.0.0.1:8002/auth/register", 
            json=register_data
        )
        
        print(f"Registration response status: {response.status_code}")
        print(f"Registration response: {response.text}")
        
        if response.status_code == 200:
            print("Registration successful!")
        else:
            print("Registration failed.")
            
    except Exception as e:
        print(f"Error during testing: {e}")
    finally:
        # Terminate the server process
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    start_server_and_test()