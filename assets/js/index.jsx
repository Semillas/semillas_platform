import React from 'react';
import ReactDom from 'react-dom';
import App from './app';

const dest = document.getElementById('react-app');

ReactDom.render(
        <App/>,
    dest)
