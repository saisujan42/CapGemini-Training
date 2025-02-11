import React from 'react';

function Header() {
    return (
        <header style={Styles.header}>
            <h1> My React App </h1>
            <nav>
                <ul style = {Styles.navList}> 
                    <li style = {Styles.navListItem}><a href="#">Home</a></li>
                    <li style = {Styles.navListItem}><a href="#">About</a></li>
                    <li style = {Styles.navListItem}><a href="#">Login</a></li>
                </ul>
            </nav>
        </header>
    )
}

const Styles = {
    header: {
        backgroundColor: '#333',
        color: 'white',
        padding: '10px',
        textAlign: 'center'
    },

    navList: {
        listStyleType: 'none',
        padding: 0,
        display: 'flex',
        justifyContent: 'center'
    },

    navListItem: {
        marginRight: '20px'
    }
}

export default Header;