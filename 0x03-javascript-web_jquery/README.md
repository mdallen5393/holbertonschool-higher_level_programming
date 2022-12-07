# PROJECT: 0x03. JavaScript - Web jQuery

## AUTHOR: Matthew Allen

## TASKS

### 0. No JQuery - `0-script.js`

Script that updates the text color of the `<header>` element to red (`#FF0000`):

* Using `document.querySelector` to select the HTML tag
* Does not use the JQuery API
* Using `0-main.html` for testing

### 1. With JQuery - `1-script.js`

Script that updates the text color of the `<header>` element to red (`#FF0000`):

* Using the JQuery API
* Does not use `document.querySelector` to select the HTML tag
* Using `1-main.html` for testing

### 2. Click and turn red - `2-script.js`

Script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

* Using the JQuery API
* Using `2-main.html` for testing

### 3. Add `.red` class - `3-script.js`

Script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`:

* Using the JQuery API
* Using `3-main.html` for testing

### 4. Toggle classes - `4-script.js`

Script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:

* The `<header>` element will always have one class: `red` or `green`, never both in the same time and never empty
* If the current class is `red`, when the user clicks on `DIV#toggle_header`, the class will be updated to `green`, and vise-versa
* Using the JQuery API
* Using `4-main.html` for testing

### 5. List of elements - `5-script.html`

Script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:

* The new element is: `<li>Item</li>`
* The new element is added to `UL.my_list`
* Using the JQuery API
* Using `5-main.html` for testing

### 6. Change the text - `6-script.js`

Script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`:

* Using the JQuery API
* Using `6-main.html` for testing

### 7. Star wars character - `7-script.js`

Script that fetches the character `name` from this URL: `https://sqapi-api.hbtn.io/api/people/5/?format=json`:

* The name is displayed in the HTML tag `DIV#character`
* Using the JQuery API
* Using `7-main.html` for testing

### 8. Star Wars movies - `8-script.js`

Script that fetches and lists the `title` for all movies by using this URL: `https//sqapi.hbtn.io/api/films/?format=json`:

* All movie titles are listed in the HTML tag `UL#list_movies`
* Using the JQuery API
* Using `8-main.html` for testing

### 9. Say Hello! - `9-script.js`

Script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`:

* The translation of "hello" is displayed in the HTML tag `DIV#hello`
* Using the JQuery API
* Script works when imported from the `<head>` tag
* Using `9-main.html` for testing
