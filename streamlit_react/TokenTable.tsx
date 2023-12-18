import React, { useState, useEffect } from 'react';
import './TokenTable.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrash } from '@fortawesome/free-solid-svg-icons';
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";

interface EditableCellProps {
  value: string;
  onValueChange: (value: string) => void;
}

const EditableCell: React.FC<EditableCellProps> = ({ value, onValueChange }) => {
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

interface Token {
  key: string;
  name: string;
  dateCreated: string;
  lastUsed: string;
}

const TokenTable: React.FC = () => {
  const [tokens, setTokens] = useState<Token[]>([
    { key: '1', name: 'Token 1', dateCreated: '2023-01-01', lastUsed: 'Never' },
    // ... other tokens as needed
  ]);

  useEffect(() => {
    Streamlit.setComponentValue(tokens);
  }, [tokens]);

  const handleDelete = (key: string) => {
    const newTokens = tokens.filter(token => token.key !== key);
    setTokens(newTokens);
  };

  const handleAddToken = () => {
    const newToken: Token = {
      key: `key-${Date.now()}`,
      name: 'New Token',
      dateCreated: new Date().toISOString().split('T')[0],
      lastUsed: 'Never'
    };
    setTokens([...tokens, newToken]);
  };

  const handleValueChange = (key: string, field: keyof Token, value: string) => {
    const updatedTokens = tokens.map(token =>
      token.key === key ? { ...token, [field]: value } : token
    );
    setTokens(updatedTokens);
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

const TokenTableWithStreamlit = withStreamlitConnection(TokenTable);

export default process.env.NODE_ENV === "development" ? TokenTable : TokenTableWithStreamlit;
