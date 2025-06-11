import React, { useState } from 'react';

function MessageInput({ onSend }) {
  const [text, setText] = useState('');

  const handleSend = () => {
    if (text.trim()) {
      onSend(text);
      setText('');
    }
  };

  return (
    <div className="flex gap-2">
      <input
        type="text"
        className="border w-full p-2 rounded"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type a message..."
      />
      <button onClick={handleSend} className="bg-blue-500 text-white p-2 rounded">
        Send
      </button>
    </div>
  );
}

export default MessageInput;
