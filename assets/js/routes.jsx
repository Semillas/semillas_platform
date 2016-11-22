import React from 'react';
import { Router, Route, hashHistory, IndexRoute} from 'react-router'

import User from './modules/User'
import Feed from './containers/Feed'
import App from './containers/App'
import About from './modules/About'
import Service from './modules/Service'
import Profile from './modules/Profile'
import Base from './modules/App'


export default <Route path="/webapp/" component={Base}>
      <IndexRoute component={App}/>
      <Route path="/user/:id/" component={User}/>
      <Route path="/about/" component={About}/>
      <Route path="/service/:id/" component={Service}/>
      <Route path="/profile/" component={Profile}/>
    </Route>
