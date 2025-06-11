import React from 'react';
import MessageBubble from './MessageBubble';

function ChatWindow({ messages }) {
  return (
    <div className="h-96 overflow-y-auto border rounded p-2 mb-4 bg-white">
      {messages.map((msg, index) => (
        <MessageBubble key={index} message={msg} />
      ))}
    </div>
  );
}

export default ChatWindow;
