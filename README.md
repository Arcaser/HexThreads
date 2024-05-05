# HexThreads
Matching Clothes to Hexcodes
## Description
We are developing a web application designed to enhance user interaction with images. The primary functionality involves capturing an image of an item, conducting color analysis to identify the corresponding hex code, and presenting users with a curated selection from a comprehensive database of available.

# Table of Contents

1. [Technologies](#technologies)
2. [The Team](#the-team)
3. [Features](#features)
4. [Instructions for Running the Project](#instructions-for-running-the-project)
5. [Overview of the Backend](#overview-of-the-backend)
6. [Overview of the Frontend](#overview-of-the-frontend)


## Technologies

	~MongoDB
	~Python
	~JavaScript
## The Team
Harmony Iroha, Robert Hood, Ryan Campbell, Gregory Smith

## Features

- Image Upload
- Clothes recommendation

## Instructions for running the project
### Frontend
```
npm run dev
```

### Backend
```
python main.py
```

## Overview of the Backend

### Overview of App.py
__Imports:__ The necessary modules and libraries are imported. These include Flask, Flask-CORS for enabling Cross-Origin Resource Sharing, ColorThief for extracting colors from images, base64 for decoding base64-encoded image data, and MongoDBConnector for interacting with a MongoDB database.
__Constants and Configuration:__ Constants like ALLOWED_EXTENSIONS (set of supported file extensions) and Flask configuration (MAX_CONTENT_LENGTH) are defined.
__Flask App Setup:__ An instance of the Flask app is created.
__MongoDB Configuration:__ The MongoDB URI and database name are set. An instance of MongoDBConnector is created to interact with the MongoDB database.
__File Upload Endpoint (/upload):__ This endpoint handles POST requests with JSON data containing image items. Each item includes the store name and binary data of the image. The binary data is decoded and stored in the MongoDB database using the add_clothes_store method of the MongoDBConnector instance.
__Color Grab Endpoints (/colorgrab):__ There are two endpoints for grabbing colors. One endpoint (/colorgrab/<store>/<rgb>) handles requests with a specified store name, while the other (/colorgrab/<rgb>) handles requests without a store name. Both endpoints return color information from the database based on the RGB value provided.
__Dominant Color Extraction Endpoint (/color):__ This endpoint handles both GET and POST requests. It extracts the dominant color from an uploaded image using the ColorThief library and returns it in JSON format.
__Palette Extraction Endpoint (/palette/<int:size>):__ This endpoint also handles GET and POST requests. It extracts a color palette from an uploaded image using the ColorThief library, with the size of the palette specified by the size parameter. The extracted colors are returned as a JSON array.
__App Execution:__ The Flask app is run if the script is executed directly.

Overall, this Flask application provides a simple API for uploading images, extracting color information, and interacting with a MongoDB database to store and retrieve color data.

### Overview of db.py
__Imports:__ The class imports necessary modules such as pymongo for MongoDB interaction, ColorThief for extracting colors from images, BytesIO for working with binary data, and datetime for handling timestamps.
__Initialization:__ The class constructor __init__ takes the MongoDB URI and database name as parameters and initializes a connection to the MongoDB server and selects the specified database.
__Adding Clothes Store Data:__ The method add_clothes_store adds information about a clothes store to the database. It takes the store name and binary image data as parameters. It uses ColorThief to extract the dominant color and a palette of colors from the image. Then, it constructs a document containing the store name, image binary data, color palette, dominant color, and current date and time. Finally, it inserts this document into the 'clothes_stores' collection in the MongoDB database.
__Getting Colors:__ The method get_colors retrieves documents from the database based on a given RGB value and optional store name. It constructs a query to find documents that match the RGB value in their color palette. If a store name is provided, it adds that condition to the query. It then executes the query and returns the matching documents.

Overall, this class provides a convenient interface for storing information about clothes stores along with their associated images and colors in a MongoDB database, and it also allows for querying and retrieving color information based on RGB values and store names.

## Overview of Frontend

### Overview of the Components
### Header Overview

#### Header.module.css
##### CSS Navigation Menu Styling:
This code is designed to style a navigation menu, commonly used in web development to navigate between different pages or sections of a website.
##### Breakdown:
1. *Font Import*:
- Imports fonts from Google Fonts API. It imports the Inter and 	Poppins font families with various weights (400, 600, 700).
2. *NavBar Styling*:
- **'.topnav'**: styles the navbar container.
  	- Sets the background color to a dark shade (#333).
  	- Specifies overflew behavior
  	- Set the font familty to "Poppins" with a fallback to sans-serif.
  	- Applies bold font weight to the text.
3. *Hidden Links*:
- **'#myLinks':**: Hides the links inside the navigation menu (except for the logo/home).
4. *Navigation Links Styling*:
- **'.topnav a'**: Styles the navigation menu links.
  - Sets text color to white
  - Defines padding for the links
  - Removes text decoration (underlines)
  - Sets font size to 17 pixels
  - Configures display as block to ensure each link occupies a seperate lines
  - Adds transition effects for smooth animation
5.  *Hamburger Menu Icon Styling*:
- **'.topnav a.icon'**: Styles the hamburger menu icon.
	- Sets a black background for the icon
   	- Positions the icon absolutely within the navbar container
   	- Places the icon at the top right corner
6.*Hover Effect*:
- **'.topnav a:hover'**: Styles the navigation links on hover.
  	- Changes background color to a light grey (#d2d2e7).
  	- Adjusts text color to black for better contrast.

### Header.jsx
##### Summary:
This React component represents a header/navigation bar for a web application. It utilizes React Router for navigation and FontAwesome icons for the hamburger menu. The header is responsive, with a toggle functionality for mobile devices.

##### Breakdown:
1. *React Component Definition*:
   - Imports necessary dependencies from React, React Router, and FontAwesome.
   - Defines a functional component named __'Header'__.
2. *CSS Module Import*:
   - Imports CSS module __'Header.module.css'__ for styling.
3. *FontAwesome Library Setup*:
   - Imports and configures FontAwesome library to use the solid bars icon ('**faBars**').
4. *Header Component Implementation*:
   - Defines a function **menuToggle()** to toggle the display of navigation links.
   - Renders JSX elements:
     	- **<div className={styles.topnav}>**: Container for the header/navigation bar, 	styled using CSS modules.
     	- **<Link to="/">Logo</Link>**: Logo/home link, routed to the home page.
     	- **<div id={styles.myLinks}**: Container for navigation links, initially 		hidden on smaller screens.
     	- **<Link to="/">Home</Link>**: Link to the home page.
     	- **<Link to="/image-upload">Shop by Picture</Link>**: Link to a page for 		shopping by picture.
     	- **<Link to="/color-picker">Shop by Color</Link>**: Link to a page for 		shopping by color.
     	- **<a href={void(0)} className={styles.icon} onClick={menuToggle}>**: 			Hamburger menu icon, triggers the **menuToggle** function on click.
     	  	- Contains a FontAwesome icon (**<FontAwesomeIcon>**) for the bars icon.
5. *Export*:
   - Exports the **Header** component as the default export. 

### Overview of ColorPicker.jsx
This serves as a page/route component within a larger React application. It renders a header component and potientially other content related to color picking functionality.

#### Breakdown
1. *Imports*
   - Imports React and Fragment from the React library.
   - Imports the **Header** component from a file located at **"../../components/header/Header"**.
   - Imports a CSS module for styling (through it seems unused in the provided code snippet).
2. *Functional Component Definition*
   - Defines a functional component named **ColorPicker**.
3. *Return Statement*
   - Returns JSX elements enclosed with a Fragment.
   - Inside the Fragment, it renders the **Header** component.
4. *Export*
   - Exports the **ColorPicker** component as the default export.

### Overview of ImageUpload.jsx:
The code represents a React component named **ImageUpload**, which likely serves as a page or route component within a larger React application. It allows users to upload an image, extract colors from it, and display a palette of those colors. It utilizes React state, fetch API for making HTTP requests, and some external CSS frameworks for styling.

#### Breakdown
1. *Imports*
   - Imports React, useState hook, and **useNavigate** hook from React Router.
   - Imports the **Header** component from a file located at **../../components/header/Header**.
   - Imports a CSS module for styling (**ImageUpload.module.css**)
2. *Functional Component Definition*
   - Defines a functional component named **ImageUpload**
3. *State Management*
   - Initializes state variables using the **useState** hook:
     	- **background**: for storing the URL of the uploaded image.
     	- **count**: for storing the number of colors in the palette.
     	- **color**: for storing the selected color.
     	- **palette**: for storing the array of colors extracted from the image.
4. *Router Navigation*
   - Uses the **useNavigate** hook to get the navigation function.
5. *Event Handlers*
   - Defines event handlers for:
     	- Updating the color count(**handleCount**).
     	- Clicking on the "Drop Picture Here" button (**handleClick**).
     	- Uploading an image (**handleImageUpload**).
     	- Selecting a color from the palette (**handleColorSelection**).
6. *HTTP Requests*
   - Defines functions to make HTTP POST requests to an endpoint (**getColor** and **getPalette**) using **fetch**.
   - Extracts colors from the uploaded image and updates the state accordingly.
7. *Utility Functions*
   - Defines a utility function (**rgbToHex**) to convert RGB color codes to hexadecimal format.
8. *Return Statement*
   - Returns JSX elements:
     - Renders the **Header** component
     - Displays a form for uploading images and selecting color count.
     - Displays the uploading image and the color palette.
9. *External Resources*
    - Includes links to external CSS frameworks(**Bootstrap** and **Font Awesome**) for styling.

### Overview of Landing.jsx
Serves as the landing page for the application. It showcases the feature of the application, such as shopping by picture and shopping by color. The component integrates with React Router and uses external CSS frameworks for styling.

#### Breakdown
1. *Imports*
   - Imports React, Fragment, **Header** component, and CSS module for styling (**Landing.module.css**).
   - Imports image assets (**headerPic**, **dragAndDrop**, **colorPal**) for displaying images on the landing page.
2. *Functional Component Definition*
   - Defines a functional component named **Landing**.
3. *Return Statement*
   - Returns JSX elements:
     - Renders the **Header** component.
     - HTML structure with metadata and links to external CSS frameworks (**Bootstrap** and **Font Awesome**).
     - Divisions (**<section>**) for different sections of the landing page:
       - Header section with a heading image and a brief description of the application (**#headerHome**).
       - Section for shopping by picture, with an image and a brief description (**#fileDrop**).
       - Section for shopping by color, with an image and a brief description (**#fileDrop**).
4. *External Resources*
   - Includes links to external CSS frameworks (**Bootstrap** and **Font Awesome**) for styling.
#### Summary
The **Landing** component serves as the landing page for the application, showcasing the features of shopping by picture and shopping by color. It provides users with a visually appealing introduction to the application's functionality and encourages further exploration. The component is structured using HTML elements and integrates with external CSS frameworks for consistent styling across different devices.

