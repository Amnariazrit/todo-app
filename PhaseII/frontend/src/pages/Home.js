// Home Page Component
import React, { useState, useEffect } from 'react';
import TodoList from '../components/TodoList';

const Home = () => {
  const [userId, setUserId] = useState(null);

  useEffect(() => {
    // Check if user is logged in
    const storedUserId = localStorage.getItem('userId');
    if (storedUserId) {
      setUserId(storedUserId);
    }
  }, []);

  if (!userId) {
    return (
      <div>
        <h1>Welcome to the Todo App</h1>
        <p>Please <a href="/login">login</a> or <a href="/register">register</a> to continue.</p>
      </div>
    );
  }

  return (
    <div>
      <h1>Your Todo List</h1>
      <TodoList userId={userId} />
    </div>
  );
};

export default Home;