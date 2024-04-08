import React from "react";
import { Link } from "react-router-dom";
import styles from '../header/Header.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const Header = () =>
{
    function menuToggle()
    {
        var links = document.getElementById(styles.myLinks);

        if(links.style.display === "block")
        {
            links.style.display = "none";
        }
        else
        {
            links.style.display = "block";
        }
    }

    return (
        <div className={styles.topnav}>
            <Link to="/">Logo</Link>
            <div id={styles.myLinks}>
                <Link to="/">Home</Link>
                <Link to="/image-upload">Shop by Picture</Link>
                <Link to="/color-picker">Shop by Color</Link>
                <Link to="/about">About</Link>
            </div>
            <a href={void(0)} className={styles.icon} onClick={menuToggle}>
                <FontAwesomeIcon icon={["far", "bars"]} size="6x" inverse/>
            </a>
        </div>
    );
};

export default Header;