import React from 'react'
import NavLink from '../containers/NavLink'

export default React.createClass({
  render() {
    return (
      <div>
        <h1>Semillas</h1>
        <ul role="nav">
          <li><NavLink to="/webapp/" onlyActiveOnIndex={true}>Home</NavLink></li>
          <li><NavLink to="/webapp/about/">About</NavLink></li>
          <li><NavLink to="/webapp/profile/">Profile</NavLink></li>
          <li><NavLink to="/webapp/service/1/">Service</NavLink></li>
        </ul>
        {this.props.children}
      </div>
    )
  }
})
