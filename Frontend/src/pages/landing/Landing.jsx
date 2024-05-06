import React from "react";
import { Link } from "react-router-dom";
import Header from "../../components/header/Header";
import styles from '../landing/Landing.module.css';
import headerPic from '../../assets/headerPic.jpg';
import dragAndDrop from '../../assets/dragDrop.png';
import colorPal from '../../assets/colorPal.jpg';

const Landing = () =>
{
    return(
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
                    <section>
                        <div id="headerHome" className="p-5">
                            <div className="p-20 bg-light">
                                <img 
                                    id={styles.headImage} 
                                    src={headerPic} 
                                    height="500" 
                                    width="630"
                                />
                                <div className="container bg-light">
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
                    <div className="p-2 bg-light"></div>
                    <section id="fileDrop" class="p-5 bg-dark">
                        <h2 className="text-light text-center">Shop By Picture</h2>
                        <div className="container-md">
                            <div className="row align-items-center justify-content-between">
                                <div className="col p-5">
                                    <p className="text-light"> 
                                        Discovering your perfect outfit is now easier than ever. 
                                        Simply upload an image containing colors you adore, and our system will analyze the hues present to curate personalized clothing suggestions tailored to your unique palette. 
                                        Whether you're drawn to vibrant blues, earthy greens, or fiery reds, our system ensures that every recommendation aligns with your color preferences, helping you effortlessly express your style with confidence. 
                                        Try it now and let the magic of color transform your fashion journey!
                                    </p>
                                    <Link to={"/image-upload"} className="btn btn-primary">Upload</Link>
                                </div>
                                <div className="col-sm">
                                    <img src={dragAndDrop} className="img-fluid"/>
                                </div>
                            </div>
                        </div>
                    </section>
                    {/* <div className="p-2 bg-light"></div>
                    <section id="fileDrop" className="p-5 bg-light">
                    <h2 className="text-dark text-center">Shop By Color</h2>
                        <div className="container-md">
                            <div className="row align-items-center justify-content-between">
                                <div className="col-sm">
                                    <img src={colorPal} className="img-fluid" alt="" />
                                </div>
                                <div className = "col p-5">
                                    <p className = "text-dark">
                                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Obcaecati error corrupti itaque omnis possimus quidem molestias, placeat explicabo voluptatem fugit praesentium expedita laborum vero vitae maxime enim, ea culpa nobis?
                                    </p>
                                    <a href="#" className="btn btn-primary">Read More</a>
                                </div>
                            
                            </div>
                        </div>
                    </section> */}
                </body>
            </html>
        </>
    );
}

export default Landing;