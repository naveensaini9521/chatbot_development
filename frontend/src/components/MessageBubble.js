import React from 'react';

function MessageBubble({ message }) {
  const isUser = message.from === 'user';
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div className={`m-1 p-2 rounded-xl ${isUser ? 'bg-blue-400 text-white' : 'bg-gray-200'}`}>
        {message.text}
      </div>
    </div>
  );
}

export default MessageBubble;
