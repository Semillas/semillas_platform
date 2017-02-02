import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { browserHistory } from 'react-router'
//import Feed from '../components/Feed'
import Explore from '../components/Explore'
import FilterText from '../components/FilterText'
import { resetErrorMessage } from '../actions'
import FeedPage from '../containers/Feed'

class Home extends Component {
  static propTypes = {
    // Injected by React Redux
    errorMessage: PropTypes.string,
    resetErrorMessage: PropTypes.func.isRequired,
    inputValue: PropTypes.string.isRequired,
    // Injected by React Router
    children: PropTypes.node
  }

  handleDismissClick = e => {
    this.props.resetErrorMessage()
    e.preventDefault()
  }

  handleChange = nextValue => {
    browserHistory.push(`/webapp/${nextValue}/`)
  }

  handleChangeSearch = searchValue => {
    //browserHistory.push(`/webapp/about/`)
    browserHistory.push(`/webapp/?search=${searchValue}/`)
  }

  renderErrorMessage() {
    const { errorMessage } = this.props
    if (!errorMessage) {
      return null
    }

    return (
      <p style={{ backgroundColor: '#e99', padding: 10 }}>
        <b>{errorMessage}</b>
        {' '}
        (<a href="#"
            onClick={this.handleDismissClick}>
          Dismiss
        </a>)
      </p>
    )
  }

  render() {
    const { children, inputValue } = this.props
    return (
      <div>
        <FilterText value={inputValue}
                 onChange={this.handleChangeSearch} />
        <hr />

        {this.renderErrorMessage()}
        <FeedPage text='prueba ismael' />
        {children}
      </div>
    )
  }
}

const mapStateToProps = (state, ownProps) => ({
  errorMessage: state.errorMessage,
  inputValue: ownProps.location.pathname.substring(1)
})

export default connect(mapStateToProps, {
  resetErrorMessage
})(Home)
