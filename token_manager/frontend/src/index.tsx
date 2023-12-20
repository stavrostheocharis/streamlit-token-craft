import React from 'react';
import ReactDOM from 'react-dom/client'; 
import TokenTable from './TokenTable'; 
import { Streamlit } from "streamlit-component-lib";

// Create a root element for the React app
const container = document.getElementById('root');
if (container) {
    const root = ReactDOM.createRoot(container);

    root.render(
        <React.StrictMode>
            <TokenTable />
        </React.StrictMode>
    );

    // Only call setComponentReady when the environment is not development
    if (process.env.NODE_ENV !== "development") {
        Streamlit.setComponentReady();
    }
} else {
    console.error('Failed to find the root element');
}


