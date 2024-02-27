# URL Shortener

A simple URL shortener web application built with Flask.

## Overview

This project provides a web-based URL shortener where users can input long URLs, and the application generates shorter, easy-to-share URLs. The project is built using Flask, Flask-Bootstrap, and Flask-WTF.

## Features

- Shortens long URLs to unique, easily shareable short URLs.
- Utilizes a randomly generated key for short URL creation.
- Stores the mapping of short URLs to original long URLs in a JSON file.
- Responsive web design with Bootstrap for an enhanced user experience.

## Project Structure

- `main/Main.py`: The main Flask application file.
- `templates/index.html`: HTML template for the web interface.
- `json/urls.json`: JSON file to store the mapping of short URLs to original long URLs.

## Usage

- Access the application in your web browser.
- Enter a long URL in the provided form.
- Click the "Shorten" button to generate a short URL.
- The short URL will be displayed, and you can use it to redirect to the original long URL.

## Configuration

- The SECRET_KEY is randomly generated for security purposes.
- Shortened URLs are stored in the json/urls.json file.


## Getting Started

This step involves installing the required Python packages (dependencies) for your project. In a Flask project, dependencies are often listed in a `requirements.txt` file. You can install these dependencies using the following command also make sure to clone the repo using the url given using using your command-prompt / terminal:



1. **Clone the repository:**

   ```bash
   git clone https://github.com/krsna016/upskill-campus-intern.git

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
