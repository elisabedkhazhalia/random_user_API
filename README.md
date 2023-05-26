# Random User API Data Extraction

This project utilizes the Random User API to extract random user data and store it in a SQLite database. It also displays a notification for each user generated using the win10toast library. The project is written in Python.

## How it works

The program performs the following steps:

1. Connects to the Random User API (https://randomuser.me/api/) to retrieve random user data.
2. Uses the `requests` library to send an HTTP GET request to the API endpoint.
3. Checks the response status code to ensure a successful request. If there is an error (e.g., server error), it displays an appropriate message and exits.
4. Parses the JSON response received from the API to extract user information such as name, gender, email, username, and password.
5. Stores the user data into a SQLite database table named "users" using the `sqlite3` module.
6. Prints the inserted user's information to the console.
7. Displays a system notification using the `win10toast` library, showing the user's name, gender, email, and username.
8. Repeats the above steps to generate a specified number of random users (in this case, 5).
9. Commits the changes to the database and closes the connection.

The project also includes a `data.json` file that stores the API response data in JSON format for further reference or analysis.

Please note that you need to have the required libraries (`requests`, `sqlite3`, `json`, `win10toast`) installed in your Python environment to run the program successfully. You can refer to the project's code in the `randomUser.py` file for a detailed implementation.

Feel free to customize and enhance the project as per your requirements and use it as a starting point for working with the Random User API and SQLite databases.
