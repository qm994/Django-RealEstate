import { ListingsActionTypes } from './listings.types';
import axios from 'axios';

export const getAllListings = (listings) => ({
    type: ListingsActionTypes.GET_LISTINGS,
    payload: listings
})

export const fetchListingsAsync = () => {
    return dispatch => {
        axios({
            method: 'get',
            url: 'http://0.0.0.0:8000/listings/get',
            responseType: 'json'
        }).then(
            res => { console.log(res.data); dispatch(getAllListings(res.data)) },
            error => console.log('erro for access listings url', error)
        )
    }
}