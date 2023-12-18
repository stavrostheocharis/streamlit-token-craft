import React, { useState } from 'react';
import './TokenTable.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrash } from '@fortawesome/free-solid-svg-icons';

const EditableCell = ({ value, onValueChange }) => {
  const [isEditing, setEditing] = useState(false);

  return (
    <td onDoubleClick={() => setEditing(true)}>
      {isEditing ? (
        <input
          type="text"
          value={value}
          onChange={(e) => onValueChange(e.target.value)}
          onBlur={() => setEditing(false)}
          autoFocus
        />
      ) : (
        value
      )}
    </td>
  );
};

const TokenTable = () => {
  const [tokens, setTokens] = useState([
    { key: '1', name: 'Token 1', dateCreated: '2023-01-01', lastUsed: 'Never' },
    // ... other tokens as needed
  ]);

  const handleDelete = (key) => {
    setTokens(tokens.filter(token => token.key !== key));
  };

  const handleAddToken = () => {
    const newToken = {
      key: `key-${Date.now()}`, // Generate a unique key
      name: 'New Token',
      dateCreated: new Date().toISOString().split('T')[0], // ISO format date
      lastUsed: 'Never'
    };
    setTokens([...tokens, newToken]);
  };

  const handleValueChange = (key, field, value) => {
    setTokens(
      tokens.map(token =>
        token.key === key ? { ...token, [field]: value } : token
      )
    );
  };

  return (
    <div className="token-table-container">
      <button onClick={handleAddToken} className="add-button">+ Create new secret key</button>
      <table className="token-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Key</th>
            <th>Date Created</th>
            <th>Last Used</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {tokens.map(token => (
            <tr key={token.key}>
              <EditableCell
                value={token.name}
                onValueChange={(value) => handleValueChange(token.key, 'name', value)}
              />
              <td>{token.key}</td>
              <td>{token.dateCreated}</td>
              <td>{token.lastUsed}</td>
              <td>
                <button onClick={() => handleDelete(token.key)} className="delete-button">
                  <FontAwesomeIcon icon={faTrash} />
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TokenTable;
