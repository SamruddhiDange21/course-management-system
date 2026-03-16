# Course Management System

A web-based Course Management System developed using Flask.
The application allows management of academic data such as programs, departments, instructors, and courses through a simple web interface.

## Project Overview

This project was created as part of a Database Management Systems (DBMS) assignment.
It demonstrates how academic information can be organized and managed through a structured web application.

The system allows users to view and add records for different academic entities.

## Features

* View list of courses
* Add new courses
* Manage programs
* Manage departments
* Manage instructors
* Organized web interface using HTML and CSS

## Project Structure

course-management-system
│
├── app.py
├── templates/
│   ├── index.html
│   ├── courses.html
│   ├── programs.html
│   ├── departments.html
│   ├── instructors.html
│   ├── add_course.html
│   ├── add_program.html
│   ├── add_department.html
│   └── add_instructor.html
│
├── static/
│   └── style.css

## Requirements

To run this project locally you will need:

* Python 3
* Flask
* MySQL
* mysql-connector-python

## Installation

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/course-management-system.git

2. Navigate into the project folder

cd course-management-system

3. Install dependencies

pip install flask
pip install mysql-connector-python

4. Run the application

python app.py

5. Open in browser

http://127.0.0.1:5000

## Future Improvements

* Database schema file
* Update and delete operations
* Improved UI and validation

## Author

Created as a DBMS academic project.
