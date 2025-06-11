import React, { useState } from 'react';
import axios from 'axios';

function LoginForm({ onLogin }) {
  const [form, setForm] = useState({ username: '', password: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://localhost:5000/api/auth/login', form);
    onLogin({ token: res.data.access_token });
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-sm mx-auto mt-20 p-6 shadow rounded bg-white">
      <h2 className="text-xl font-semibold mb-4">Login</h2>
      <input
        className="w-full mb-2 p-2 border rounded"
        type="text"
        placeholder="Username"
        value={form.username}
        onChange={(e) => setForm({ ...form, username: e.target.value })}
      />
      <input
        className="w-full mb-2 p-2 border rounded"
        type="password"
        placeholder="Password"
        value={form.password}
        onChange={(e) => setForm({ ...form, password: e.target.value })}
      />
      <button type="submit" className="w-full bg-blue-500 text-white py-2 rounded">
        Log In
      </button>
    </form>
  );
}

export default LoginForm;
