import React from 'react';
import { Router, Route, hashHistory, IndexRoute} from 'react-router'

import User from './modules/User'
import Home from './containers/Home'
import App from './containers/App'
import About from './modules/About'
import ServicePage from './containers/ServicePage'
import Profile from './modules/Profile'
import Base from './components/Base'
import UserPage from './containers/UserPage'
import FeedPage from './containers/Feed'


export default <Route path="/webapp/" component={Base}>
      <IndexRoute component={Home}/>
      <Route path="/webapp/user/:id/" component={User}/>
      <Route path="/webapp/about/" component={About}/>
      <Route path="/webapp/service/:uuid/" component={ServicePage}/>
      <Route path="/webapp/profile/" component={Profile}/>
      <Route path="/webapp/github/" component={App}/>
      <Route path="/webapp/feed/" component={FeedPage}/>
      <Route path="/webapp/userpage/:login/"
         component={UserPage} />
    </Route>
