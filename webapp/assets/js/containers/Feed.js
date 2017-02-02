import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { loadFeed } from '../actions/Feed'
import Service from '../components/Service'
import zip from 'lodash/zip'
import List from '../components/List'

const loadData = ({ params, loadFeed }) => {
  loadFeed(location.search)
}

class FeedPage extends Component {
  static propTypes = {
    servicePagination: PropTypes.object,
    text: PropTypes.string.isRequired
  }

  componentWillMount() {
    loadData(this.props)
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.filters !== this.props.filters) {
      loadData(nextProps)
    }
  }

  handleLoadMoreClick = () => {
    this.props.loadFeed('', true)
  }

  renderService([ service ]) {
    return (
      <Service
        service={service}
        key={service.uuid}
      />
    )
  }

  render() {
    const { feedServicesPaginated, feedServicesPagination } = this.props
    // TODO: Control the case no service is returned.
    if (!feedServicesPaginated) {
      return <h1><i>Loading {" services..."}</i></h1>
    }

    return (
      <div>
      {this.props.text}
        <List renderItem={this.renderService}
              items={zip(feedServicesPaginated)}
              onLoadMoreClick={this.handleLoadMoreClick}
              loadingLabel={'Loading more...'}
              {...feedServicesPagination} />
      </div>
    )
  }
}

const mapStateToProps = (state, ownProps) => {

  const {
    pagination: { feedServices },
    entities: { services }
  } = state

  const feedServicesPagination = feedServices.feed || { ids: [] }
  const feedServicesPaginated = feedServicesPagination.ids.map(id => services[id])

  return {
    feedServicesPaginated,
    feedServicesPagination,
  }
}

export default connect(mapStateToProps, {
  loadFeed
})(FeedPage)
