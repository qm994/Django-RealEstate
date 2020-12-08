import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import { Listing } from '../listing/listing.component';
import { fetchListingsAsync } from '../../redux/listings/listings.actions';

const Listings = ({ listingItems, fetchListingsAsync }) => {
    useEffect(() => {
        fetchListingsAsync()
    }, [fetchListingsAsync])

    return (
        <div>
            {
                listingItems.map(({ id, ...otherCollectionProps }) => 
                    <Listing key={id} { ...otherCollectionProps } />
                )
            }
        </div>
    )
}

const mapStateToProps = (state) => {
    return (
        {
            listingItems: state.listings.listingItems
        }
    )
}

const mapDispatchToProps = (dispatch) => ({
    fetchListingsAsync: () => dispatch(fetchListingsAsync())
})

export default connect(mapStateToProps, mapDispatchToProps)(Listings);
