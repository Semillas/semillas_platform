import { CALL_SEMILLAS_API, Schemas } from '../middleware/semillas_api'

export const FEED_REQUEST = 'FEED_REQUEST'
export const FEED_SUCCESS = 'FEED_SUCCESS'
export const FEED_FAILURE = 'FEED_FAILURE'

// Fetches the feed from Semillas API.
// Relies on the custom API middleware defined in ../middleware/api.js.
const fetchFeed = (filters, nextPageUrl)=> ({
  [CALL_SEMILLAS_API]: {
    types: [ FEED_REQUEST, FEED_SUCCESS, FEED_FAILURE ],
    endpoint: nextPageUrl,
    schema: Schemas.FEED
  }
})

// Fetches a single feed from Github API unless it is cached.
// Relies on Redux Thunk middleware.
export const loadFeed = (filters, nextPage, requiredFields = []) => (dispatch, getState) => {
  const {
    nextPageUrl = `service/feed`,
    pageCount = 0
  } = getState().pagination.feedServices.feed || {}

  if (pageCount > 0 && !nextPage) {
    return null
  }

  return dispatch(fetchFeed(filters, nextPageUrl))
}
