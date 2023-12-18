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
    if (e.key === 'Enter') {
      onValueChange(editValue);
      setEditing(false);
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
          onChange={(e) => setEditValue(e.target.value)}
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
  is_active: boolean; // This should be added if you are tracking active status
}

interface TokenTableProps extends ComponentProps {
  args: {
    tokens: Token[];
    columnHelpText?: { [key: string]: string }; // Optional help text for columns
  };
}

const TokenTable: React.FC<TokenTableProps> = ({ args }) => {
  const [tokenList, setTokenList] = useState<Token[]>(args.tokens || []);
  const { columnHelpText } = args; // Destructure the optional columnHelpText

  useEffect(() => {
    setTokenList(args.tokens || []);
  }, [args.tokens]);

  useEffect(() => {
    Streamlit.setFrameHeight();
  });

  const handleDelete = (key: string) => {
    // Logic here needs to match with your backend deletion logic
    // This is just a placeholder for the actual delete functionality
    const updatedTokens = tokenList.map(token =>
      token.key === key ? { ...token, is_active: false } : token
    );
    setTokenList(updatedTokens);
    Streamlit.setComponentValue(updatedTokens);
  };

  const handleValueChange = (key: string, field: keyof Token, value: string) => {
    const updatedTokens = tokenList.map(token =>
      token.key === key ? { ...token, [field]: value } : token
    );
    setTokenList(updatedTokens);
    Streamlit.setComponentValue(updatedTokens);
  };

  // Helper function to render a table header with an optional tooltip
  const renderTableHeader = (columnName: string, displayText: string) => (
    <th>
      {displayText}
      {columnHelpText && columnHelpText[columnName] && (
        <span title={columnHelpText[columnName]} className="header-help-icon">
          ℹ️
        </span>
      )}
    </th>
  );

  return (
    <div className="token-table-container">
      <table className="token-table">
        <thead>
          <tr>
            {renderTableHeader("name", "Name")}
            {renderTableHeader("key", "Key")}
            {renderTableHeader("dateCreated", "Date Created")}
            {renderTableHeader("lastUsed", "Last Used")}
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {tokenList.map(token => (
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

export default withStreamlitConnection(TokenTable);
