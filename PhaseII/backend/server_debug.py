import subprocess
import time
import threading
import requests

def run_server_with_output():
    # Start the server in a subprocess
    server_process = subprocess.Popen([
        "py", "-3.13", "-m", "uvicorn", "main:app", 
        "--host", "127.0.0.1", "--port", "8003", "--log-level", "info"
    ], 
    cwd=r"D:\amna.riaz\todo-app\todo-app\PhaseII\backend",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)
    
    # Wait a bit for the server to start
    time.sleep(3)
    
    # Capture the output in a separate thread
    def read_output():
        for line in iter(server_process.stderr.readline, ''):
            print(f"SERVER: {line.strip()}")
    
    output_thread = threading.Thread(target=read_output)
    output_thread.daemon = True
    output_thread.start()
    
    try:
        print("Testing login...")
        # Test login
        response = requests.post(
            "http://127.0.0.1:8003/auth/login",
            data={
                "username": "test2@example.com",
                "password": "testpassword123"
            }
        )
        
        print(f"Login response status: {response.status_code}")
        print(f"Login response: {response.text}")
        
    except Exception as e:
        print(f"Error during testing: {e}")
    finally:
        # Terminate the server process after a delay
        time.sleep(2)
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    run_server_with_output()