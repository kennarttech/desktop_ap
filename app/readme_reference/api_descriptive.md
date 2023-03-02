### curl is a command-line tool used to transfer data to or from a server using various protocols, including HTTP, HTTPS, FTP, SMTP, and more. It's a powerful tool that allows you to make requests to web servers and fetch data from them.


## curl -X POST -H "Content-Type: application/json" -d '{"id": 4, "name": "David", "age": 24, "major": "Physics"}' http://localhost:5000/students


1. This curl is use to send request to the server 
## curl -X POST -H "Content-Type: application/json" -d '{"id": 4, "name": "David", "age": 24, "major": "Physics"}' http://192.168.43.164:4000/students


2. curl http://192.168.43.164:4000/students


3.  curl is the name of the command-line tool
    -X POST specifies the HTTP method to use (in this case, POST)
    -H "Content-Type: application/json" sets the HTTP header of the request to Content-Type: application/json. This tells the server that the data being sent in the request body is in JSON format.
    -d '{"id": 4, "name": "David", "age": 24, "major": "Physics"}' specifies the data to be sent in the request body. The data is a JSON-formatted string containing the information of the new student.
    http://localhost:5000/students is the URL of the server to send the request to. In this case, it's the URL of the Flask application running on the local machine.

When you run the curl command, it sends a POST request to the Flask server with the JSON payload specified in the -d option. The server then processes the request and returns a response, which is printed to the console.




4. ----------------------------------------------------------------------
4.  This code defines three classes: LoginGUI, AdminDashboardGUI, and UserDashboardGUI. It also imports the tkinter and requests modules.


5. In the _login_btn_clicked method of LoginGUI, the user's username and password are retrieved from the entry boxes. These values are then sent in a POST request to a server running at http://localhost:5000/login. If the server returns a 200 status code (indicating that the login was successful), the message label is updated to display "Login successful" in green text. The self.master.destroy() line closes the login window. If the user is an admin, an AdminDashboardGUI instance is created and its run method is called. Otherwise, a UserDashboardGUI instance is created with the user's ID and its run method is called.

6. The AdminDashboardGUI class creates a simple GUI that welcomes the admin and provides a button labeled "View All Data". When the button is clicked, a GET request is sent to http://localhost:5000/data and the response data is printed to the console.

7. The UserDashboardGUI class is similar to the AdminDashboardGUI, but it displays a welcome message for the user and provides two buttons: "Save Data" and "View Data". When the "Save Data" button is clicked, a POST request is sent to http://localhost:5000/data with some example data. When the "View Data" button is clicked, a GET request is sent to http://localhost:5000/data with a query parameter specifying the user ID, and the response data is printed to the console.

