import React from 'react'
import NavLink from './NavLink'

export default React.createClass({
  render() {
    return (
      <div>
        Service: {this.props.params.id}
        <li><NavLink to="/user/1">Owner</NavLink></li>
      </div>
    )
  }
})
