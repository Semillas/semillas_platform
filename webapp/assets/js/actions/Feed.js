import { CALL_SEMILLAS_API, Schemas } from '../middleware/semillas_api'

export const FEED_REQUEST = 'FEED_REQUEST'
export const FEED_SUCCESS = 'FEED_SUCCESS'
export const FEED_FAILURE = 'FEED_FAILURE'

// Fetches the feed from Semillas API.
// Relies on the custom API middleware defined in ../middleware/api.js.
const fetchFeed = filters=> ({
  [CALL_SEMILLAS_API]: {
    types: [ FEED_REQUEST, FEED_SUCCESS, FEED_FAILURE ],
    endpoint: `service/feed`,
    schema: Schemas.FEED
  }
})

// Fetches a single feed from Github API unless it is cached.
// Relies on Redux Thunk middleware.
export const loadFeed = (filters, requiredFields = []) => (dispatch, getState) => {
  const feed = getState().entities.feed
  if (feed && requiredFields.every(key => feed.hasOwnProperty(key))) {
    return null
  }
  return dispatch(fetchFeed(filters))
}

