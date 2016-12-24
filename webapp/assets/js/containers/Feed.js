import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { loadFeed } from '../actions/Feed'
import Service from '../components/Service'
import zip from 'lodash/zip'

const loadData = ({ login, loadFeed }) => {
  loadFeed(filters)
}

class FeedPage extends Component {
  static propTypes = {
    servicePagination: PropTypes.object,
    feed: PropTypes.array.isRequired,
  }

  componentWillMount() {
    loadData(this.props)
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.login !== this.props.login) {
      loadData(nextProps)
    }
  }

  handleLoadMoreClick = () => {
    this.props.loadFeed(this.props.login, true)
  }

  renderService([ service ]) {
    return (
      <Service
        service={service} />
    )
  }

  render() {
    const { FeedServices } = this.props
    if (!FeedServices) {
      return <h1><i>Loading {" services..."}</i></h1>
    }

    return (
      <div>
        <List renderItem={this.renderService}
              items={FeedServices}
              onLoadMoreClick={this.handleLoadMoreClick}
              loadingLabel={'Loading more...'}
              {...feedServicesPagination} />
      </div>
    )
  }
}

const mapStateToProps = (state, ownProps) => {

  const {
    pagination: { feedServicesPagination },
    entities: { services }
  } = state

  const feedServices = feedServicesPagination.uuids.map(id => services[id])

  return {
    feedServices,
    feedServicesPagination,
  }
}

export default connect(mapStateToProps, {
  loadFeed
})(FeedPage)
