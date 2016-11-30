import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { loadService } from '../actions'
import User from '../components/User'
import Repo from '../components/Repo'
import Service from '../components/Service'
import List from '../components/List'
import zip from 'lodash/zip'

const loadData = ({ uuid, loadService }) => {
  loadService(uuid)
}

class UserPage extends Component {
  static propTypes = {
    uuid: PropTypes.string.isRequired,
    service: PropTypes.object,
    loadService: PropTypes.func.isRequired
  }

  componentWillMount() {
    loadData(this.props)
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.uuid !== this.props.uuid) {
      loadData(nextProps)
    }
  }

//  handleLoadMoreClick = () => {
//    this.props.loadStarred(this.props.uuid, true)
//  }

//  renderRepo([ repo, owner ]) {
//    return (
//      <Repo
//        repo={repo}
//        owner={owner}
//        key={repo.fullName} />
//    )
//  }

  render() {
    const { service, uuid } = this.props
    if (!service) {
      return <h1><i>Loading {uuid}{"'s service..."}</i></h1>
    }

    const { starredRepos, starredRepoOwners, starredPagination } = this.props
    return (
      <div>
        <Service service={Service} />
        <hr />
//        <List renderItem={this.renderRepo}
//              items={zip(starredRepos, starredRepoOwners)}
//              //onLoadMoreClick={this.handleLoadMoreClick}
//              loadingLabel={`Loading ${uuid}'s starred...`}
//              {...starredPagination} />
      </div>
    )
  }
}

const mapStateToProps = (state, ownProps) => {
  // We need to lower case the login due to the way GitHub's API behaves.
  // Have a look at ../middleware/api.js for more details.
  const uuid = ownProps.params.uuid

  const {
    pagination: { starredByUser },
    entities: { users, repos }
  } = state

  const starredPagination = starredByUser[login] || { ids: [] }
  const starredRepos = starredPagination.ids.map(id => repos[id])
  const starredRepoOwners = starredRepos.map(repo => users[repo.owner])

  return {
    uuid,
    starredRepos,
    starredRepoOwners,
    starredPagination,
    user: users[login]
  }
}

export default connect(mapStateToProps, {
  loadService,
})(ServicePage)
