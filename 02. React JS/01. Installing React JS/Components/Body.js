import React from 'react';

function Body() {
    return (
        <main style = {Styles.main}>
            <h2> Welcome to My Website </h2>
            <p> This is a simple React application with a Structured Layout. </p>
        </main>
    );
}

const Styles = {
    main: {
        padding: '20px',
        textAlign: 'center'
    }
};

export default Body;