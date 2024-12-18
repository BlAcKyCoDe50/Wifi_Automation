# Wi-Fi Automation Application

![icon](https://github.com/user-attachments/assets/6a354587-8ee4-4359-b551-d3013b37b59c)


## Please provide the feedback or any improvements required, it will hardly take 2 minutes!!
### https://forms.gle/iUEDGn7JF3TjbvFaA

## Overview

This application automates the process of logging into the university Wi-Fi network using a Tkinter GUI and Selenium for web automation. It handles various edge cases related to page states and interactions, and it is packaged for cross-platform use.

![Demo](./assets/videoplayback.gif)

# Download

### To download the application, [click here](https://www.dropbox.com/scl/fi/m6hv54zx9bfyyr3gmqsdo/mainfile.exe?rlkey=8ufmi1ltzoyfbzz0zefdn7ca4&st=zshnw6gg&dl=0)

## Features

- Automated login to university Wi-Fi
- Handles login, logout, and pre-login states
- User-friendly GUI built with Tkinter
- Credentials management and storage
- Packaged for easy distribution

## Getting Started

![image](https://github.com/user-attachments/assets/e8a25549-f262-4940-926b-ba5ff8827b27)

### Prerequisites

- Python 3.x
- Docker

## Watch the Demo [click here](https://youtu.be/pp6kFQskK6s)
### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/wifi-automation.git
    cd wifi-automation
    ```

2. Install the required Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Run the application:
    ```sh
    python mainfile.pyw
    ```

### First Time Setup

1. Save your credentials using the application. This will generate a `credentials.txt` file.

## Docker

### Dockerfile

A `Dockerfile` is included in the repository. If you want to build the Docker image yourself, follow these steps:

1. Build the Docker image:
    ```sh
    docker build -t wifi-automation:v1 .
    ```

2. Run the Docker container:
    ```sh
    docker run -d wifi-automation:v1
    ```

### Docker Image

The Docker container image is available on Docker Hub. You can pull it using the following command:
    ```sh
    docker pull vishvajeetsingh09/wifiautomation:latest
    ```

## Download

To download the application, [click here](https://www.dropbox.com/scl/fi/m6hv54zx9bfyyr3gmqsdo/mainfile.exe?rlkey=8ufmi1ltzoyfbzz0zefdn7ca4&st=zshnw6gg&dl=0)


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
