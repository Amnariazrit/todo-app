import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("Testing the Todo API...")
    
    # Step 1: Register a new user
    print("\n1. Registering a new user...")
    register_data = {
        "email": "test@example.com",
        "name": "Test User",
        "password": "testpassword123"
    }
    
    try:
        register_response = requests.post(f"{BASE_URL}/auth/register", json=register_data)
        print(f"Registration status: {register_response.status_code}")
        if register_response.status_code == 200:
            user_data = register_response.json()
            print(f"Registered user: {user_data}")
        else:
            print(f"Registration failed: {register_response.text}")
    except Exception as e:
        print(f"Error during registration: {e}")
    
    # Step 2: Login to get a token
    print("\n2. Logging in to get a token...")
    try:
        # Using requests with data parameter to send form data
        login_response = requests.post(
            f"{BASE_URL}/auth/login",
            data={
                "username": "test@example.com",
                "password": "testpassword123"
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )
        print(f"Login status: {login_response.status_code}")
        
        if login_response.status_code == 200:
            token_data = login_response.json()
            access_token = token_data.get("access_token")
            print(f"Access token received: {access_token[:20]}..." if access_token else "No token received")
            
            # Step 3: Create a task using the token
            print("\n3. Creating a task...")
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }
            
            task_data = {
                "title": "Sample Task",
                "description": "This is a sample task",
                "completed": False
            }
            
            try:
                create_task_response = requests.post(
                    f"{BASE_URL}/api/v1/tasks",
                    json=task_data,
                    headers=headers
                )
                print(f"Create task status: {create_task_response.status_code}")
                
                if create_task_response.status_code == 200:
                    created_task = create_task_response.json()
                    print(f"Created task: {created_task}")
                    
                    # Step 4: Get all tasks
                    print("\n4. Getting all tasks...")
                    get_tasks_response = requests.get(
                        f"{BASE_URL}/api/v1/tasks",
                        headers=headers
                    )
                    print(f"Get tasks status: {get_tasks_response.status_code}")
                    
                    if get_tasks_response.status_code == 200:
                        tasks = get_tasks_response.json()
                        print(f"Tasks retrieved: {tasks}")
                        
                        # Step 5: Update a task
                        if tasks:
                            task_id = tasks[0]['id']
                            print(f"\n5. Updating task {task_id}...")
                            
                            update_data = {
                                "title": "Updated Sample Task",
                                "completed": True
                            }
                            
                            update_response = requests.put(
                                f"{BASE_URL}/api/v1/tasks/{task_id}",
                                json=update_data,
                                headers=headers
                            )
                            print(f"Update task status: {update_response.status_code}")
                            
                            if update_response.status_code == 200:
                                updated_task = update_response.json()
                                print(f"Updated task: {updated_task}")
                                
                                # Step 6: Toggle task completion
                                print(f"\n6. Toggling completion for task {task_id}...")
                                toggle_response = requests.patch(
                                    f"{BASE_URL}/api/v1/tasks/{task_id}/complete",
                                    headers=headers
                                )
                                print(f"Toggle completion status: {toggle_response.status_code}")
                                
                                if toggle_response.status_code == 200:
                                    toggle_result = toggle_response.json()
                                    print(f"Toggle result: {toggle_result}")
                                
                                # Step 7: Delete the task
                                print(f"\n7. Deleting task {task_id}...")
                                delete_response = requests.delete(
                                    f"{BASE_URL}/api/v1/tasks/{task_id}",
                                    headers=headers
                                )
                                print(f"Delete task status: {delete_response.status_code}")
                                
                                if delete_response.status_code == 200:
                                    delete_result = delete_response.json()
                                    print(f"Delete result: {delete_result}")
                    else:
                        print(f"Failed to get tasks: {get_tasks_response.text}")
                else:
                    print(f"Failed to create task: {create_task_response.text}")
            except Exception as e:
                print(f"Error during task operations: {e}")
        else:
            print(f"Login failed: {login_response.text}")
    except Exception as e:
        print(f"Error during login: {e}")

if __name__ == "__main__":
    test_api()