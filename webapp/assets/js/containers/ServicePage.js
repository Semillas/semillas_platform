import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { loadService } from '../actions'
import Service from '../components/Service'
import zip from 'lodash/zip'

const loadData = ({ uuid, loadService }) => {
  loadService(uuid)
}

class ServicePage extends Component {
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


  render() {
    const { service, uuid } = this.props
    if (!service) {
      return <h1><i>Loading {uuid}{"'s service..."}</i></h1>
    }

    //const { starredRepos, starredRepoOwners, starredPagination } = this.props
    return (
      <div>
        <Service service={Service} />
        <hr />
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
    entities: { services }
  } = state

//  const starredPagination = starredByUser[login] || { ids: [] }
//  const starredRepos = starredPagination.ids.map(id => repos[id])
//  const starredRepoOwners = starredRepos.map(repo => users[repo.owner])

  return {
    uuid,
//    starredRepos,
//    starredRepoOwners,
//    starredPagination,
    services: services[uuid]
  }
}

export default connect(mapStateToProps, {
  loadService,
})(ServicePage)
