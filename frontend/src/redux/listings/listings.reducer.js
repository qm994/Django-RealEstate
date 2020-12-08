import { ListingsActionTypes } from './listings.types';

const INITIAL_STATE = {
    listingItems: []
}

const listingsReducer = (state = INITIAL_STATE, action) => {
    switch(action.type) {
        case ListingsActionTypes.GET_LISTINGS:
            return {
                ...state,
                listingItems: action.payload
            }
        default:
            return state
    }
}
export default listingsReducer;
