import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../../components/header/Header";
import styles from '../image-upload/ImageUpload.module.css';

const ImageUpload = () =>
{
    const [background, setBackground] = useState(null);
    const [count, setCount] = useState(0);
    const [palette, setPalette] = useState([]);

    let navigate = useNavigate();

    const handleCount = (e) => {
        setCount(e.target.value);
    }

    const handleClick = () => {
        document.getElementById("fileInput").click();
    };

    const handleImageUpload = (e) => {
        const imageFile = e.target.files[0];
        const reader = new FileReader();
        
        getPalette(e);

        reader.onload = (e) => {
            setBackground(e.target.result);
        };

        if(imageFile)
        {
            reader.readAsDataURL(imageFile);
        }
    };

    const handleColorSelection = (e) => {
        e.preventDefault();
        const hexCode = e.target.style.backgroundColor;
        let path = '/results';
        localStorage.setItem('selected-color', rgbToHex(hexCode));
        
        navigate(path);
    };

    const getPalette = async (e) => {
        e.preventDefault();
        const image = new FormData();
        image.append('file', e.target.files[0]);

        const response = await fetch('http://127.0.0.1:5000/palette/' + count, {
            method: 'POST',
            body: image,
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            setPalette(data);
        });
    };

    const generateColors = () => {
        const elements = [];

        for(let i = 0; i < palette.length; i++)
        {
            elements.push (
                <li className={styles.color} key={i}>
                    <div 
                        className={styles.colorArea} 
                        style={{backgroundColor: palette[i]}}
                        onClick={handleColorSelection}
                    />
                </li>
            );
        }

        return elements;
    };

    function rgbToHex(col)
    {
        if(col.charAt(0)=='r')
        {
            col=col.replace('rgb(','').replace(')','').split(',');
            var r=parseInt(col[0], 10).toString(16);
            var g=parseInt(col[1], 10).toString(16);
            var b=parseInt(col[2], 10).toString(16);
            r=r.length==1?'0'+r:r; g=g.length==1?'0'+g:g; b=b.length==1?'0'+b:b;
            var colHex='#'+r+g+b;
            return colHex;
        }
    }

    return (
        <>
            <Header/>
            <html>
                <head>
                    <meta charSet="UTF-8" />
                    <meta httpEquiv="X-UA-Compatible" content="IE=edge"/>
                    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                    <link
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"
                        rel="stylesheet"
                        integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x"
                        crossOrigin="anonymous"
                    />
                    <link 
                        rel="stylesheet" 
                        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
                    />
                    <title>HexHome</title>
                </head>
                <body>
                    <div id="container" className="bg-dark text-light align-items-center">
                        <h2 className="text-center">Ready To Get Your Perfect Match?</h2>
                        <p className="text-center">
                            All you have to do is drop your picture down below and set the amount of colors you want to find. 
                            That's it then we'll do the rest. 
                        </p>
                        <div className={styles.uploadElements}>
                            <button className="p-2" onClick={handleClick}>Upload</button>
                            <input 
                                type="file" 
                                id="fileInput" 
                                className="text-dark" 
                                style={{display: "none"}} 
                                accept="images/png, images/jpg"
                                onChange={handleImageUpload}
                            />
                            <input
                                type="number"
                                className={styles.paletteCount}
                                onChange={handleCount}
                                min={1}
                                max={6}
                                value={count}
                            />
                        </div>
                        <div className= "container d-flex justify-content-center">
                            <div
                                className="bg-light"
                                id={styles.dropDisplay}
                                style={{backgroundImage: `url(${background})`}}
                            />
                        </div>
                    </div>
                    <div className={styles.paletteArea}>
                        <ul className={styles.colors}>
                            {generateColors()}
                        </ul>
                    </div>
                </body>
            </html>
        </>
    );
};

export default ImageUpload;