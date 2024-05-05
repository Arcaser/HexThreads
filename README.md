# HexThreads
Matching Clothes to Hexcodes
## Description
We are developing a web application designed to enhance user interaction with images. The primary functionality involves capturing an image of an item, conducting color analysis to identify the corresponding hex code, and presenting users with a curated selection from a comprehensive database of available.

## Table of Contents
- [Technologies](#technologies)
- [Features](#features)
- [The Team](#team)
- [Overview of the Backend](#Backend)
- [Overview of the Frontend](#Frontend)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

  

## Technologies

	~MongoDB
	~Python
	~JavaScript
## The Team
Harmony Iroha, Robert Hood, Ryan Campbell, Gregory Smith

## Features

- Image Upload
- Clothes recommendation

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

# Overview of Frontend

## Overview of .eslintrc.cjs
This is a JavaScript object that represents a configuration file for ESLint, a popular linting tool used for static code analysis in JavaScript projects. Let's break down its key components:

**root:** Specifies that ESLint should stop looking for configuration files in parent directories once it finds this one. This ensures that this configuration applies to the entire project.
**env:** Specifies the environment in which the code will run. In this case, it's configured for browser and ES2020 (ECMAScript 2020) environments.
extends: Extends the base configuration by incorporating additional sets of rules. It includes:
	***'eslint:recommended':*** A set of recommended rules by ESLint.
	***'plugin:react/recommended':*** A set of recommended rules for React applications.
	***'plugin:react/jsx-runtime':*** Rules for React JSX runtime.
	***'plugin:react-hooks/recommended':*** Rules for React hooks.
**ignorePatterns:** Specifies file patterns to be ignored by ESLint. Files matching these patterns won't be linted. In this case, it's ignoring the 'dist' directory and the '.eslintrc.cjs' file.
**parserOptions:** Configures parser options for ESLint. It sets the ECMAScript version to 'latest' and specifies 'module' as the source type.
**settings:** Provides additional settings for ESLint. Here, it specifies the React version as '18.2'.
**plugins:** Specifies ESLint plugins to be used. In this case, it includes the 'react-refresh' plugin.
**rules:** Configures ESLint rules. It overrides some of the default rules:
	***'react/jsx-no-target-blank':*** ***'off':*** Disables the rule that prevents using target="_blank" in JSX, allowing it.
	***'react-refresh/only-export-components':*** Configures a custom rule provided by the 'react-refresh' plugin. It warns when non-component exports are present, allowing constant exports.
 
Overall, this configuration ensures that ESLint checks JavaScript code for potential errors, enforces best practices, and provides React-specific linting for React projects.

## Summary of .gitignore File

### Logs and Debug Files
- `logs`: Ignore logs directory.
- `*.log`, `npm-debug.log*`, `yarn-debug.log*`, `yarn-error.log*`, `pnpm-debug.log*`, `lerna-debug.log*`: Ignore various log files.
  
### Dependency Directories
- `node_modules`: Ignore the node_modules directory.
- `dist`, `dist-ssr`: Ignore output directories.

### Local Development Artifacts
- `*.local`: Ignore local development artifacts.

### Editor Specific Files and Directories
- `.vscode/*`: Ignore Visual Studio Code editor directories.
  - `!.vscode/extensions.json`: Except for the extensions.json file.
- `.idea`: Ignore JetBrains IDE directories.
- `.DS_Store`: Ignore macOS directory metadata files.
- `*.suo`, `*.ntvs*`, `*.njsproj`, `*.sln`, `*.sw?`: Ignore Visual Studio related files.


## HexThreads Web Application Overview

### HTML Structure

- `<!doctype html>`: Declares the document type as HTML5.
- `<html lang="en">`: Defines the root HTML element with the language attribute set to English.
- `<head>`: Contains metadata and links to external resources.
  - `<meta charset="UTF-8" />`: Specifies the character encoding of the document as UTF-8.
  - `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`: Sets the viewport for responsive design.
  - `<title>HexThreads</title>`: Sets the title of the web page.
- `<body>`: Contains the content of the web page.
  - `<div id="root"></div>`: Container for rendering the React application.
  - `<script type="module" src="/src/main.jsx"></script>`: Loads the main JavaScript file for the application using ECMAScript modules.

This HTML file serves as the entry point for the HexThreads web application, providing the basic structure and loading the necessary JavaScript resources for rendering the React components.

## Package-lock.json Overview

The `package-lock.json` file is automatically generated for any project where npm or Yarn is used for package management. It serves as a manifest for the exact versions of dependencies and sub-dependencies installed in the project.

### Purpose

- **Deterministic Builds**: Ensures that every time dependencies are installed, the exact same versions are used. This prevents discrepancies between development and production environments.

- **Faster Installs**: Since the exact version information is already stored in `package-lock.json`, subsequent installations can be faster as npm or Yarn can directly fetch the specified versions without needing to resolve dependency versions again.

### Structure

- **Top-Level Dependencies**: Lists all direct dependencies of the project along with their specific version numbers.

- **Sub-dependencies**: Each dependency may have its own dependencies (sub-dependencies). These are listed under each direct dependency, along with their versions.

- **Version Resolutions**: Specifies the resolved version of each dependency. This ensures consistency across different environments.

### Modifying `package-lock.json`

- **Manual Edits**: It's generally not recommended to manually edit `package-lock.json`, as it can lead to inconsistencies. Instead, update dependencies using npm or Yarn commands (`npm install` or `yarn add`).

- **Automatic Updates**: The file is automatically updated whenever changes are made to dependencies or when installing/updating packages using npm or Yarn.

### Example

Here's a simplified example of a `package-lock.json` file:

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "lockfileVersion": 1,
  "dependencies": {
    "lodash": {
      "version": "4.17.21",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz"
    },
    "axios": {
      "version": "0.21.1",
      "resolved": "https://registry.npmjs.org/axios/-/axios-0.21.1.tgz"
    }
  }
}
```

## Package.json File Overview

The `package.json` file is a metadata file for Node.js projects. It contains various fields that provide information about the project, its dependencies, scripts, and other configurations.

### Sample `package.json` Structure:

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "A brief description of my project.",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.17.1",
    "lodash": "^4.17.21"
  },
  "devDependencies": {
    "jest": "^27.0.6"
  },
  "author": "Your Name",
  "license": "MIT"
}
```
## `vite.config.js` Summary

The provided code is a configuration file for Vite, a build tool for modern web development projects. It uses ES module syntax.

### Summary:

- **Import Statement**: 
  - Imports the `defineConfig` function from the 'vite' package.
  - Imports the 'react' plugin from the '@vitejs/plugin-react' package.

- **Configuration Export**:
  - Exports a default configuration object using the `defineConfig` function.
  - The `defineConfig` function is used to define Vite's configuration settings.

- **Configuration Object**:
  - `plugins`: An array containing configuration options for Vite plugins.
    - In this case, it includes the 'react' plugin.
    - The 'react' plugin enables Vite to handle React projects efficiently.

- **External Resources**:
  - A comment with a link to the Vite documentation for further reference.

### Purpose:
The purpose of this configuration is to set up Vite for a React project by enabling the 'react' plugin, which allows Vite to handle JSX and React components effectively during development and production builds.
