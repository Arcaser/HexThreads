import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../../components/header/Header";
import styles from '../image-upload/ImageUpload.module.css';

const ImageUpload = () =>
{
    const [background, setBackground] = useState(null);
    const [count, setCount] = useState(0);
    const [color, setColor] = useState('');
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

        let path = '/color-picker';

        localStorage.setItem('selected-color', rgbToHex(hexCode));
        navigate(path);
    };

    const getColor = async (e) => {
        e.preventDefault();
        const image = new FormData();
        image.append('file', e.target.files[0]);

        const response = await fetch('http://127.0.0.1:5000/color', {
            method: 'POST',
            body: image,
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            setColor(data);
        });
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
    async function fetchMatchingClothes(hexCode) {
        const url = 'http://127.0.0.1:5000/match';  // Endpoint for the POST request
        const data = {
            Hex: hexCode  // Prepare the JSON payload with the hex code
        };
    
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)  // Convert the JavaScript object to a JSON string
            });
    
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
    
            const matches = await response.json();  // Parse the JSON response
            displayImages(matches);  // Call to display images
        } catch (error) {
            console.error('Error fetching matching clothes:', error);
            displayImages([]);  // Ensure clear display if error occurs
        }
    }
    
    
    function displayImages(imageData) {
        const container = document.getElementById('imagesContainer');
        container.innerHTML = '';  // Clear previous images
    
        imageData.forEach(image => {
            const img = document.createElement('img');
            img.src = image.filePath.replace(/\\/g, '/'); // Correct the file path
            img.alt = `Clothing item ${image.id}`;
            container.appendChild(img);
        });
    }
    
    function fetchAndDisplay(hexCode) {
        fetchMatchingClothes(hexCode).then(matches => {
            console.log('Matching clothes:', matches);
        }).catch(error => {
            console.error('Failed to fetch matches:', error);
        });
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
                    <link rel="stylesheet" 
                    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
                    <title>HexHome</title>
                </head>
                <body>
                    <div id="container" className="bg-dark text-light align-items-center">
                        <h2 className="text-center">Ready To Get Your Perfect Match?</h2>
                        <p className="text-center">
                            All you have to do is drop your picture down below. That's it then we'll do the rest. 
                        </p>
                        <div className={styles.uploadElements}>
                            <button className="p-2" onClick={handleClick}>Drop Picture Here</button>
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