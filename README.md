# Flight_Roster
CS308 Flight roster project. 

# Framework

Directory Structure

This project follows a basic directory structure to maintain organization and separation of concerns between the front-end and back-end codebases. Here's an overview of the structure:

client/: This directory contains the front-end codebase, which is responsible for the user interface and client-side logic of the application.
public/: Contains static assets like HTML files and images.
src/: Contains the source code of the React application.
components/: Reusable UI components.
pages/: Components representing entire pages of the application. (i will start with the login page.)
services/: Services for handling API calls and other business logic.
utils/: Utility functions that can be used across the application.
App.js: Main application component.
index.js: Entry point to the React application.
package.json: Manages client-side dependencies and scripts.
server/: This directory contains the back-end codebase, which is responsible for handling data storage, business logic, and communication with the front end.
api/: API route definitions for handling client requests.
config/: Configuration files for the server, such as database settings or authentication.
models/: Database models or schema definitions.
controllers/: Business logic for handling requests from the client.
middlewares/: Express middlewares for tasks like logging, error handling, or authentication.
utils/: Utility functions specific to the server-side logic.
database.js: Database connection and configuration.
server.js: Entry point for the server application.
package.json: Manages server-side dependencies and scripts.


Small explanation for both groups:

Front-end team: The front-end team works on the  client/ directory, focusing on building the user interface and client-side functionality of the application. They create components, define page layouts, and manage data presentation and interaction using React. This team interacts with the back-end team's APIs to fetch and update data as needed.

Back-end team: The back-end team works on the server/ directory, focusing on implementing server-side logic, managing data storage and retrieval, and defining APIs for communication with the front end. They create database models, implement business logic, and handle client requests by defining API endpoints. This team ensures that the application's data is secure, consistent, and accessible to the front-end components.

Feel free to change the directories as how you like it. It is just a basic scheme to make our project more organized.

Updated: 22/04/2024 
-E.G
