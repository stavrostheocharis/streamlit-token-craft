import React from 'react';
import TokenTable from './TokenTable.tsx';

const App: React.FC = () => {
    return (
        <div className="App">
            <h1>Token Management</h1>
            <TokenTable />
        </div>
    );
}

export default App;
