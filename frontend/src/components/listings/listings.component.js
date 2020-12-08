import React from 'react';
import axios from 'axios';

class Listings extends React.Component {
    state = {
        listings: []
    }
    
    componentDidMount() {
        axios({
            method: 'get',
            url: 'http://0.0.0.0:8000/listings/get',
            responseType: 'json'
        }).then((res) => (console.log(res)))
    }

    render() {
        return (
            <div>
                hello first component
            </div>
        )
    }
}

export default Listings;
