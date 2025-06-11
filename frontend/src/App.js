import React, { useState } from 'react';
import ChatWindow from './components/ChatWindow';
import MessageInput from './components/MessageInput';
import LoginForm from './components/LoginForm';

function App() {
  const [user, setUser] = useState(null);
  const [messages, setMessages] = useState([]);

  if (!user) {
    return <LoginForm onLogin={setUser} />;
  }

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">E-commerce Chatbot</h1>
      <ChatWindow messages={messages} />
      <MessageInput
        onSend={async (text) => {
          const response = await fetch('http://localhost:5000/api/chat', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${user.token}`,
            },
            body: JSON.stringify({ message: text }),
          });
          const data = await response.json();
          setMessages([...messages, { text, from: 'user' }, { text: data.response, from: 'bot' }]);
        }}
      />
    </div>
  );
}

export default App;
