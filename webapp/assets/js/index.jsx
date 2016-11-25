import React from 'react';
import { render } from 'react-dom';
import { Router, Route, hashHistory, IndexRoute} from 'react-router'
import { syncHistoryWithStore } from 'react-router-redux'
import Root from './containers/Root'
import configureStore from './store/configureStore'
import { browserHistory } from 'react-router'

const store = configureStore()
const history = syncHistoryWithStore(browserHistory, store)

const dest = document.getElementById('react-app');

render(
  <Root store={store} history={history} />,
  dest)
