# Remind-me-later

Remind-me-later is a web application designed to allow users to set up reminders with messages. It provides a simple and intuitive interface for users to input the date, time, message, and the method of reminder delivery (currently supporting SMS and Email). This project focuses on providing a backend API endpoint using Django to handle reminder creation and storage in a database.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)

## Features

- Allows users to set reminders with messages.
- Provides an intuitive interface for selecting date and time.
- Supports reminder delivery through SMS and Email.
- Backend API endpoint for creating and storing reminders in a database.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/remind-me-later.git

```
## Usage

- Once the development server is running, you can access the API endpoint for creating reminders at http://localhost:8000/api/reminder/.
- Send a POST request to the API endpoint with the following JSON payload:
  {
    "date": "2024-03-10",
    "time": "08:00:00",
    "message": "Don't forget to attend the meeting!",
    "reminder_type": "Email"
  }

## API Documentation

- The API endpoint for creating reminders accepts POST requests with JSON payloads containing the following fields:
  - date (string): Date of the reminder in the format "YYYY-MM-DD".
  - time (string): Time of the reminder in the format "HH:MM:SS".
  - message (string): Text message for the reminder.
  - reminder_type (string): Type of reminder delivery (e.g., "SMS", "Email").


