import requests
import time
import uuid

def final_test():
    BASE_URL = "http://127.0.0.1:8001"  # Using port 8001
    
    # Generate a unique email
    unique_email = f"test_{uuid.uuid4()}@example.com"
    
    print(f"Using unique email: {unique_email}")
    
    # Step 1: Register a new user
    print("\n1. Registering a new user...")
    register_data = {
        "email": unique_email,
        "name": "Final Test User",
        "password": "testpassword123"
    }
    
    register_resp = requests.post(f"{BASE_URL}/auth/register", json=register_data)
    print(f"Registration status: {register_resp.status_code}")
    if register_resp.status_code != 200:
        print(f"Registration failed: {register_resp.text}")
        return False
    
    user_data = register_resp.json()
    print(f"Registered user: {user_data['email']}")
    
    # Step 2: Login to get a token
    print("\n2. Logging in to get a token...")
    login_resp = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": unique_email,
            "password": "testpassword123"
        }
    )
    
    print(f"Login status: {login_resp.status_code}")
    if login_resp.status_code != 200:
        print(f"Login failed: {login_resp.text}")
        return False
    
    token_data = login_resp.json()
    access_token = token_data.get("access_token")
    print(f"Access token received: {access_token[:20]}..." if access_token else "No token received")
    
    # Step 3: Create a task using the token
    print("\n3. Creating a task...")
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    task_data = {
        "title": "Final Test Task",
        "description": "This is a final test task",
        "completed": False
    }
    
    task_resp = requests.post(f"{BASE_URL}/api/v1/tasks", json=task_data, headers=headers)
    print(f"Create task status: {task_resp.status_code}")
    if task_resp.status_code != 200:
        print(f"Create task failed: {task_resp.text}")
        return False
    
    created_task = task_resp.json()
    print(f"Created task: {created_task['title']}")
    
    # Step 4: Get all tasks
    print("\n4. Getting all tasks...")
    get_tasks_resp = requests.get(f"{BASE_URL}/api/v1/tasks", headers=headers)
    print(f"Get tasks status: {get_tasks_resp.status_code}")
    if get_tasks_resp.status_code != 200:
        print(f"Get tasks failed: {get_tasks_resp.text}")
        return False
    
    tasks = get_tasks_resp.json()
    print(f"Retrieved {len(tasks)} tasks")
    
    # Step 5: Update the task
    if tasks:
        task_id = tasks[0]['id']
        print(f"\n5. Updating task {task_id}...")
        
        update_data = {
            "title": "Updated Final Test Task",
            "completed": True
        }
        
        update_resp = requests.put(
            f"{BASE_URL}/api/v1/tasks/{task_id}",
            json=update_data,
            headers=headers
        )
        print(f"Update task status: {update_resp.status_code}")
        if update_resp.status_code != 200:
            print(f"Update task failed: {update_resp.text}")
            return False
        
        updated_task = update_resp.json()
        print(f"Updated task: {updated_task['title']}, completed: {updated_task['completed']}")
    
    print("\nAll tests passed! The API is working correctly.")
    return True

if __name__ == "__main__":
    success = final_test()
    if success:
        print("\nAPI is fully functional!")
    else:
        print("\n❌ Some tests failed.")