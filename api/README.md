# API for the Timetabler Application

## What about the API

The API is made to serve a mobile application being developed by [@arekings](https://github.com/arekings) and a desktop application that is to be developed yet. Links to the desktop app [[]] and mobile app [[]] are as given.

- The API serves as the applications powerhouse where all the logic is handled and what the end users have to do is to send a request for a resource and the application handles.

- The API also has implemented an algorithm that makes sure no classes collide no matter the number of classes available, it does the computation and adjusts the classes to avoid class colission or for example a `a lecturer being assigned more than one class at the same time` which leads to inconvenience.

## API endpoints

- The endpoints exposed by the API are as follows

  - /api/users
  - /api/users/username
  - /api/users/new
  - /api/users/update/username
  - /api/users/delete/username
