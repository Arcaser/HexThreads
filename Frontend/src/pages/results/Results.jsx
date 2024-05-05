import React, { useState, useEffect, useRef } from "react";
import Header from "../../components/header/Header";
import styles from "../results/Results.module.css";

const Results = () => 
{
    const [clothes, setClothes] = useState([]);
    const hex = localStorage.getItem('selected-color');
    const hasRun = useRef(false);

    useEffect(() => {
        if(!hasRun.current)
        {
            getClothes();
            hasRun.current = true;
        }
    });

    const getClothes = async () => {
        const url = 'http://127.0.0.1:5000/match';
        const data = {'Hex': hex};

        const response = await fetch(url, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            setClothes(data);
        });
    };

    const generateImageList = () => {
        const images = [];
    
        for (let i = 0; i < clothes.length; i++) 
            {
            var imgData = clothes[i].image_data;
            var altText = `Clothing item ${clothes[i].id}`;
    
            images.push(
                <li key={i} className={styles.resultItem}>
                    <img
                        src={imgData}
                        alt={altText}
                        className={styles.resultImg}
                    />
                </li>
            );
        };
    
        return images;
    };
    
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
                    <hr className="bg-light"/>
                    <h1 className="text-center">Results For</h1>
                    <div className="container-md">
                        <button type="button" className="btn btn-primary"> 
                            <div>Hexcode: {hex}</div>
                        </button>
                        <div className="container-md">
                            <div className="row align-items-center justify-content-between">
                                <div className="col p-5">
                                    <ul className={styles.resultArea}>
                                        {generateImageList()}
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>  
                </body>
            </html>
        </>
    );
};

export default Results;