import React from 'react';
import { Router, Route, hashHistory, IndexRoute} from 'react-router'

import User from './modules/User'
import Feed from './containers/Feed'
import App from './containers/App'
import About from './modules/About'
import ServicePage from './containers/ServicePage'
import Profile from './modules/Profile'
import Base from './components/Base'
import UserPage from './containers/UserPage'


export default <Route path="/webapp/" component={Base}>
      <IndexRoute component={Feed}/>
      <Route path="/webapp/user/:id/" component={User}/>
      <Route path="/webapp/about/" component={About}/>
      <Route path="/webapp/service/:uuid/" component={ServicePage}/>
      <Route path="/webapp/profile/" component={Profile}/>
      <Route path="/webapp/feed/" component={Feed}/>
  <Route path="/webapp/:login/"
         component={UserPage} />
    </Route>
