import React from 'react';
import ReactDOM from 'react-dom';
import TokenTable from './TokenTable.tsx';
import { Streamlit } from "streamlit-component-lib";

ReactDOM.render(
  <React.StrictMode>
    <TokenTable />
  </React.StrictMode>,
  document.getElementById('root')
);

Streamlit.setComponentReady();

