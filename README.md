# QUIAOIT
Exercise for Flask-REST Plus CRUD

GET - Outputs the JSON format of the given ID, if there is. Otherwise, it would output a string message that there is no recorded info on the given ID.

DELETE - If the given ID is not empty, it will output a string message that the given ID number is deleted, otherwise, it will give a 304 response code, meaning there is nothing to delete.

PUT (or UPDATE) - If the given ID is not empty, it will output a string that would give the modified ID, with the JSON of the updated information on the given ID. Otherwise, it will give a 304 response code. It assumes that the input of the information to update is correct.
