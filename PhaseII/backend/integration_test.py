import requests
import time

def test_register_then_login():
    BASE_URL = "http://127.0.0.1:8001"
    
    # Register a user
    print("Step 1: Registering a user...")
    register_data = {
        "email": "integration_test@example.com",
        "name": "Integration Test User",
        "password": "testpassword123"
    }
    
    register_resp = requests.post(f"{BASE_URL}/auth/register", json=register_data)
    print(f"Registration status: {register_resp.status_code}")
    if register_resp.status_code != 200:
        print(f"Registration failed: {register_resp.text}")
        return
    
    print("Registration successful!")
    
    # Wait a moment to ensure data is written
    time.sleep(1)
    
    # Try to login with the same credentials
    print("\nStep 2: Logging in with the registered user...")
    login_resp = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": "integration_test@example.com",
            "password": "testpassword123"
        }
    )
    
    print(f"Login status: {login_resp.status_code}")
    if login_resp.status_code != 200:
        print(f"Login failed: {login_resp.text}")
        return
        
    print("Login successful!")
    token_data = login_resp.json()
    access_token = token_data.get("access_token")
    print(f"Token received: {access_token[:20] if access_token else 'None'}...")
    
    # Now test creating a task with the token
    print("\nStep 3: Creating a task with the token...")
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    task_data = {
        "title": "Integration Test Task",
        "description": "This is a task created during integration test",
        "completed": False
    }
    
    task_resp = requests.post(f"{BASE_URL}/api/v1/tasks", json=task_data, headers=headers)
    print(f"Task creation status: {task_resp.status_code}")
    if task_resp.status_code != 200:
        print(f"Task creation failed: {task_resp.text}")
        return
    
    print("Task creation successful!")
    print("\n✅ All integration tests passed!")
    
if __name__ == "__main__":
    test_register_then_login()