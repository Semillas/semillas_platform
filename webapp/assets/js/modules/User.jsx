import React from 'react'

export default React.createClass({
  render() {
    return (
      <div>
        User: {this.props.params.id}
      </div>
    )
  }
})
