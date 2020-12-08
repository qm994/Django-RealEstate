import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Listing } from '../listing/listing.component';
const Listings = () => {
    const [listings, getListings] = useState([]);

    useEffect(() => {
        axios({
            method: 'get',
            url: 'http://0.0.0.0:8000/listings/get',
            responseType: 'json'
        }).then(
            (res) => { 
                console.log(res.data)
                getListings(res.data)
            },
            error => console.log('erro for access listings url', error)
        )
    }, [getListings])

    return (
        <div>
            {
                listings.map(({ id, ...otherCollectionProps }) => 
                    <Listing key={id} { ...otherCollectionProps } />
                )
            }
        </div>
    )
}

export default Listings;
