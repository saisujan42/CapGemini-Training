import React from 'react';

function Footer() {
    return (
        <footer style = {Styles.footer}>
            <p> &copy; 2024 My Website. All Rights Reserved. </p>
        </footer>
    );
}

const Styles = {
    footer: {
        backgroundColor: '#333',
        color: 'white',
        textAlign: 'center',
        padding: '10px',
        position: 'fixed',
        width: '100%',
        bottom: 0
    }
};

export default Footer;