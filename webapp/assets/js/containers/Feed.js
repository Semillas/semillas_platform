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
    const { services } = this.props
    if (!services) {
      return <h1><i>Loading {" services..."}</i></h1>
    }

    return (
      <div>
        <User user={user} />
        <hr />
        <List renderItem={this.renderService}
              items={services}
              onLoadMoreClick={this.handleLoadMoreClick}
              loadingLabel={'Loading more...'}
              {...starredPagination} />
      </div>
    )
  }
}

const mapStateToProps = (state, ownProps) => {
  // We need to lower case the login due to the way GitHub's API behaves.
  // Have a look at ../middleware/api.js for more details.

  const {
    pagination: { feedServicesPagination },
    entities: { services }
  } = state

  const starredPagination = starredByUser[login] || { ids: [] }
  const starredRepos = starredPagination.ids.map(id => repos[id])
  const starredRepoOwners = starredRepos.map(repo => users[repo.owner])

  return {
    login,
    user: users[login]
  }
}

export default connect(mapStateToProps, {
  loadUser,
  loadStarred
})(UserPage)
