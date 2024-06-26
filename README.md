# Note Application Backend

A note-taking application developed with Django, Django Rest Framework and knox

The application of this backend service can be found here.
[Note app on Google cloud](https://note-app-react-5e74ajfmaa-ew.a.run.app/)

### Further developments
- Unhandled exceptions management
- Find and fix bugs

### Routes and endpoint details
````
[
        {
            'Endpoint': 'api/v1/notes',
            'method': 'GET',
            'body': None,
            'description': 'Returns array of notes',
            'status code': '200',
            'authRequired': True
        },
        {
            'Endpoint': 'api/v1/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note',
            'status code': '200',
            'authRequired': True
        },
        {
            'Endpoint': 'api/v1/notes',
            'method': 'POST',
            'body': {},
            'description': 'Creates new note with data sent in post request',
            'status code': '201',
            'authRequired': True
        },
        {
            'Endpoint': 'api/v1/notes/id',
            'method': 'PUT',
            'body': {},
            'description': 'Updates an existing note with data sent in post request',
            'status code': '200',
            'authRequired': True
        },
        {
            'Endpoint': 'api/v1/notes/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting note',
            'status code': '204',
            'authRequired': True
        },
        {
            'Endpoint': 'api/v1/auth/login',
            'method': 'POST',
            'body': {'username': '', 'password': ''},
            'description': 'Returns user data + Authorize token',
            'status code': '200',
            'authRequired': False
        },
        {
            'Endpoint': 'api/v1/auth/logout',
            'method': 'POST',
            'body': None,
            'description': 'Return HTTP 204 and deletes user token',
            'status code': '204',
            'authRequired': False
        },
        {
            'Endpoint': 'api/v1/auth/logoutall',
            'method': 'POST',
            'body': None,
            'description': 'Return HTTP 204 and deletes all associated user tokens',
            'status code': '204',
            'authRequired': False
        },
        {
            'Endpoint': 'api/v1/auth/register',
            'method': 'POST',
            'body': {'username': '', 'password': '', 'email': ''},
            'description': 'Returns user data + Authorize token',
            'status code': '201',
            'authRequired': False
        },
        {
            'Endpoint': 'api/v1/auth/user',
            'method': 'GET',
            'body': None,
            'description': 'Requires token authorization header, returns authenticated user detail',
            'status code': '200',
            'authRequired': True
        },
    ]
````

Please use and report any bugs found here: [Report bugs](https://github.com/Olujuwon/note_rest_api/issues)
