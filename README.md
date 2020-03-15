# QUIAOIT
Exercise for Flask-REST Plus CRUD

GET (Give) - Gets all the products in the database.

GET - Outputs the JSON format of the given ID, if there is. Otherwise, it would output a 404 error.

DELETE - If the given ID is not empty, it will output a string message that the given ID number is deleted, otherwise, it will give a response code.

PUT (or UPDATE) - If the given ID is not empty, it will output a string that would give the modified ID, with the JSON of the updated information on the given ID. Otherwise, it will give a 404 response code. It assumes that the input of the information to update is correct.

POST - Adds the user's input to the database. Assumes that the user input is correct.
