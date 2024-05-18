AirBnB Clone - The Console
This project is part of the ALX School curriculum. It's a clone of the AirBnB web application. This repository contains the first part of the project: a command interpreter to manage objects in the application.

Description of the Project
The goal of this project is to create a simple clone of the AirBnB web application. It involves several steps, including building a console to manage objects, creating a web server, and linking it all with a front-end interface.

Description of the Command Interpreter
The command interpreter, also known as the console, is a tool that allows users to interact with the application's data model. It provides commands to create, retrieve, update, and delete objects.

How to Start It
To start the console, you'll need to have Python installed on your system. Follow these steps:

Clone the repository:


git clone https://github.com/sondosEssam/AirBnB_clone.git
Navigate to the project directory:


cd AirBnB_clone
Run the console:


./console.py
How to Use It
Once the console is running, you can use various commands to interact with the application. Here are some of the available commands:

help: Displays a list of available commands or detailed help for a specific command.
quit: Exits the console.
EOF: Exits the console.
create <class_name>: Creates a new instance of class_name, saves it (to a JSON file), and prints the ID.
show <class_name> <id>: Prints the string representation of an instance based on the class name and ID.
destroy <class_name> <id>: Deletes an instance based on the class name and ID.
all [<class_name>]: Prints all string representations of all instances. If a class name is provided, it prints all instances of that class.
update <class_name> <id> <attribute_name> <attribute_value>: Updates an instance based on the class name and ID by adding or updating the attribute.
<class name>.all(): Retrieves all instances of a class.
<class name>.count(): Retrieves the number of instances of a class.
<class name>.show("<id>"): Retrieves an instance based on its ID.
<class name>.destroy("<id>"): Deletes an instance based on its ID.
Examples
Here are some examples of how to use the command interpreter:

Creating a New Instance:


(hbnb) create User
Output:


3cfb2e7d-4c6a-4c41-967d-9e3b37b8d393

Showing an Instance:


(hbnb) show User 3cfb2e7d-4c6a-4c41-967d-9e3b37b8d393

Output:


[User] (3cfb2e7d-4c6a-4c41-967d-9e3b37b8d393) {'id': '3cfb2e7d-4c6a-4c41-967d-9e3b37b8d393', 'created_at': datetime.datetime(2023, 5, 17, 17, 23, 45, 863733), 'updated_at': datetime.datetime(2023, 5, 17, 17, 23, 45, 863748)}
Updating an Instance:


(hbnb) update User 3cfb2e7d-4c6a-4c41-967d-9e3b37b8d393 email "airbnb@mail.com"

Destroying an Instance:


(hbnb) destroy User 3cfb2e7d-4c6a-4c41-967d-9e3b37b8d393

Showing All Instances of a Class:


(hbnb) all User

Showing All Instances:


(hbnb) all

Retrieving All Instances of a Class:


(hbnb) User.all()

Output:


[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
Counting Instances of a Class:


(hbnb) User.count()
Output:


2

Showing an Instance by ID:


(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
Output:


[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
Destroying an Instance by ID:


(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")

Note
Ensure that you have all dependencies installed and properly configured. The models package should include all the necessary classes and the storage system to save and retrieve instances.
