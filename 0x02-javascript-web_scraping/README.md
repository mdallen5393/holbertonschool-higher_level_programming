# PROJECT: 0x02. JavaScript - Web scraping

## AUTHOR: Matthew Allen

## TASKS

### 0. Readme - `0-readme.js`

Script that reads and prints the content of a file.

* The first argument is the file path
* The content of the file is in `utf-8`
* If an error occurrs during the reading, an error is printed

### 1. Write me - `1-writeme.js`

Script that writes a string to a file.

* First argument is the file path
* Second argument is the string to write
* The content of the file is written in `utf-8`
* If an error occurrs during writing, an error object is printed

### 2. Status code - `2-statuscode.js`

Script that displays the status code of a `GET` request.

* First argument is the URL to request (`GET`)
* The status code must is printed as follows: `code: <status code>`
* Uses the `request` module

### 3. Star wars movie title - `3-starwars_title.js`

Script that prints the title of a Star Wars movie where the episode number matches a given integer.

* First argument is the movie ID
* Uses the Star wars AIP with endpoint `https://swapi-api.hbtn.io/api/films/:id`
* Uses the `request` module

### 4. Star wars Wedge Antilles - `4-starwars_count.js`

Script that prints the number of movies where the character "Wedge Antilles" is present.

* First argument is the API URL of the Star wars API: `https://swapi-api.hbtn.io/api/films/`
* Wedge Antilles is character ID `18`, which is used for filtering the result of the API
* Uses the `request` module

### 5. Loripsum - `5-request_store.js`

Script that gets the contents of a webpage and stores it in a file.

* First argument is the URL to request
* Second argument is the file path to store the body response
* The file is UTF-8 encoded
* Uses the `request` module

### 6. How many completed? - `6-completed_tasks.js`

Script that computes the number of tasks completed by user id.

* First argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
* Only print users with completed task
* Uses the `request` module
