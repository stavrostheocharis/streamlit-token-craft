import React, { useState, useEffect } from 'react';
import { Streamlit, withStreamlitConnection, ComponentProps } from "streamlit-component-lib";
import './TokenTable.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrash } from '@fortawesome/free-solid-svg-icons';

interface EditableCellProps {
  value: string;
  onValueChange: (value: string) => void;
}

const EditableCell: React.FC<EditableCellProps> = ({ value, onValueChange }) => {
  const [editValue, setEditValue] = useState(value);
  const [isEditing, setEditing] = useState(false);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && editValue.length <= 18) {
      onValueChange(editValue);
      setEditing(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newValue = e.target.value;
    if (newValue.length <= 18) {
      setEditValue(newValue);
    }
  };

  useEffect(() => {
    setEditValue(value);
  }, [value]);

  return (
    <td onDoubleClick={() => setEditing(true)}>
      {isEditing ? (
        <input
          type="text"
          value={editValue}
          onChange={handleChange}
          onBlur={() => setEditing(false)}
          onKeyDown={handleKeyDown}
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
  is_active: boolean;
}

interface TokenTableProps extends ComponentProps {
  args: {
    tokens: Token[];
  };
}

const TokenTable: React.FC<TokenTableProps> = ({ args }) => {
  const [pendingDeletion, setPendingDeletion] = useState<string | null>(null);
  const [tokenList, setTokenList] = useState<Token[]>(args.tokens || []);

  useEffect(() => {
    setTokenList(args.tokens || []);
  }, [args.tokens]);

  useEffect(() => {
    Streamlit.setFrameHeight();
  });

  const handleDeleteClick = (key: string) => {
    setPendingDeletion(key);
  };

  const confirmDelete = () => {
    if (pendingDeletion) {
      const updatedTokens = tokenList.map(token =>
        token.key === pendingDeletion ? { ...token, is_active: false } : token
      );
      setTokenList(updatedTokens);
      Streamlit.setComponentValue(updatedTokens);
      setPendingDeletion(null);
    }
  };

  const cancelDelete = () => {
    setPendingDeletion(null);
  };

  const handleValueChange = (key: string, field: keyof Token, value: string) => {
    const updatedTokens = tokenList.map(token =>
      token.key === key ? { ...token, [field]: value } : token
    );
    setTokenList(updatedTokens);
    Streamlit.setComponentValue(updatedTokens);
  };

  return (
    <div className="token-table-container">
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
          {tokenList.map((token, index) => (
            <tr key={index}>
              <EditableCell
                value={token.name}
                onValueChange={(value) => handleValueChange(token.key, 'name', value)}
              />
              <td>{token.key}</td>
              <td>{token.dateCreated}</td>
              <td>{token.lastUsed}</td>
              <td>
                {pendingDeletion === token.key ? (
                  <>
                    <button onClick={confirmDelete} className="confirm-delete-button">
                      Confirm Revoke
                    </button>
                    <button onClick={cancelDelete} className="cancel-button">
                      Cancel
                    </button>
                  </>
                ) : (
                  <button onClick={() => handleDeleteClick(token.key)} className="delete-button">
                    <FontAwesomeIcon icon={faTrash} />
                  </button>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default withStreamlitConnection(TokenTable);
