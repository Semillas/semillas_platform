import * as ActionTypes from '../actions/index'
import * as FeedActionTypes from '../actions/Feed'
import merge from 'lodash/merge'
import paginate from './paginate'
import paginate_feed from './paginate'
import { routerReducer as routing } from 'react-router-redux'
import { combineReducers } from 'redux'

// Updates an entity cache in response to any action with response.entities.
const entities = (state = { users: {}, repos: {}, services: {} }, action) => {
  if (action.response && action.response.entities) {
    return merge({}, state, action.response.entities)
  }

  return state
}

// Updates error message to notify about the failed fetches.
const errorMessage = (state = null, action) => {
  const { type, error } = action

  if (type === ActionTypes.RESET_ERROR_MESSAGE) {
    return null
  } else if (error) {
    return action.error
  }

  return state
}

// Updates the pagination data for different actions.
const pagination = combineReducers({
  starredByUser: paginate({
    mapActionToKey: action => action.login,
    types: [
      ActionTypes.STARRED_REQUEST,
      ActionTypes.STARRED_SUCCESS,
      ActionTypes.STARRED_FAILURE
    ]
  }),
  stargazersByRepo: paginate({
    mapActionToKey: action => action.fullName,
    types: [
      ActionTypes.STARGAZERS_REQUEST,
      ActionTypes.STARGAZERS_SUCCESS,
      ActionTypes.STARGAZERS_FAILURE
    ]
  }),
  feedServices: paginate({
    mapActionToKey: action => action.searchFilters,
    types: [
      FeedActionTypes.FEED_REQUEST,
      FeedActionTypes.FEED_SUCCESS,
      FeedActionTypes.FEED_FAILURE
    ]
  })

})

const rootReducer = combineReducers({
  entities,
  pagination,
  errorMessage,
  routing
})

export default rootReducer
