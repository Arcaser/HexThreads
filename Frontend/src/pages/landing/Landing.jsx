import React, {Container, Component, Fragment} from "react";
import Header from "../../components/header/Header";
import styles from '../landing/Landing.module.css';
import headerPic from 'C:/Users/savag/Desktop/HexThreads/HexThreads/Frontend/src/assets/headerPic.jpg';
import dragAndDrop from 'C:/Users/savag/Desktop/HexThreads/HexThreads/Frontend/src/assets/dragDrop.png';
import colorPal from 'C:/Users/savag/Desktop/HexThreads/HexThreads/Frontend/src/assets/colorPal.jpg';

const Landing = () =>
{
    return(
        <Fragment>
            <Header/>
            <html>
                <head>
                    <meta charset="UTF-8" />
                    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
                    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                    <link
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"
                        rel="stylesheet"
                        integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x"
                        crossorigin="anonymous"
                    />
                    <link rel="stylesheet" 
                    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
                    <link rel="stylesheet" href="./CSS/Landing.css"/>
                    <title>HexHome</title>
                </head>
                <body>
                    <section>
                        <div id="headerHome" class="p-5">
                            <div class="p-20 bg-light">
                            <img id={styles.headImage} src = {headerPic} 
                                height="500" width="630"/>
                                <div class="container bg-light">
                                    <h1 className={styles.header}>HexThreads</h1>
                                    <p className={styles.headerText}>
                                        HexThreads is designed to discover your ideal match for your requirements. 
                                        Our expertise lies in ensuring you with optimal suggestions from our extensive client database, 
                                        ensuring a perfect pairing for your preferred colorway. 
                                    </p>
                                </div>
                            </div>
                        </div>
                    </section>
                    <div class="p-2 bg-light"></div>
                    <section id="fileDrop" class="p-5 bg-dark">
                        <h2 class="text-light text-center">Shop By Picture</h2>
                        <div class="container-md">
                            <div class="row align-items-center justify-content-between">
                                <div class="col p-5">
                                    <p class="text-light">
                                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Obcaecati error corrupti itaque omnis possimus quidem molestias, placeat explicabo voluptatem fugit praesentium expedita laborum vero vitae maxime enim, ea culpa nobis?
                                    </p>
                                    <a href="C:\Users\User\OneDrive\Documents\HexThread\HexThreads\client\HexHtml\HexFileDrop.html" class="btn btn-primary">Read More</a>
                                </div>
                                <div class="col-sm">
                                    <img src={dragAndDrop} class="img-fluid"/>
                                </div>
                            </div>
                        </div>
                    </section>
                    <div class="p-2 bg-light"></div>
                    <section id="fileDrop" class="p-5 bg-light">
                    <h2 class="text-dark text-center">Shop By Color</h2>
                        <div class="container-md">
                            <div class="row align-items-center justify-content-between">
                                <div class="col-sm">
                                    <img src="C:\Users\User\OneDrive\Documents\HexThreads\client\images\colorPal.jpg" class="img-fluid" alt="" />
                                </div>
                                <div class = "col p-5">
                                    <p class = "text-dark">
                                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Obcaecati error corrupti itaque omnis possimus quidem molestias, placeat explicabo voluptatem fugit praesentium expedita laborum vero vitae maxime enim, ea culpa nobis?
                                    </p>
                                    <a href="#" class="btn btn-primary">Read More</a>
                                </div>
                            
                            </div>
                        </div>
                    </section>
                </body>
            </html>
        </Fragment>
    );
}

export default Landing;