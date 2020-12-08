import React from 'react';

export const Listing = ({ address, bathrooms }) => {
    return (
        <div>
            <span>{`The address is ${address}`}</span>
            <span>{`It has ${bathrooms} bathroom(s)`}</span>
        </div>
    )
}