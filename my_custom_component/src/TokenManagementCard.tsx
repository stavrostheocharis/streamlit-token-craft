// src/TokenManagementCard.tsx
import React from 'react';
import { Streamlit, StreamlitComponentBase, withStreamlitConnection } from 'streamlit-component-lib';

interface TokenManagementCardProps {
  args: {
    tokens: string[];
  };
}

class TokenManagementCard extends StreamlitComponentBase<TokenManagementCardProps> {
  public render = (): React.ReactNode => {
    // Extract 'tokens' from this.props.args
    const { tokens } = this.props.args;

    // Your rendering logic
    return (
      <div>
        {tokens.map((token: string, index: number) => (
          <div key={index}>{token}</div>
        ))}
      </div>
    );
  };
}

Streamlit.setComponentReady();

export default TokenManagementCard;
