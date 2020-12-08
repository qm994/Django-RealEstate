import listingsReducer from './listings/listings.reducer';

import { combineReducers } from 'redux';

const rootReducer = combineReducers({
    listings: listingsReducer
})

export default rootReducer;