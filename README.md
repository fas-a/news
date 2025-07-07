# Installation Guide

Follow these steps to install this project:

## Prerequisites
Ensure you have installed:
- **Git**: [Download Git](https://git-scm.com/)
- **Node.js**: [Download Node.js](https://nodejs.org/)
- **npm**: Usually included with Node.js installation.
- **Python**: [Download Python](https://www.python.org/)

## Installation Steps
1. **Clone the Repository**
    ```bash
    git clone https://github.com/fas-a/news
    cd news
    ```

2. **Install Back-End Dependencies**
    Navigate to the backend directory:
    ```bash
    cd backend
    ```
    Create a virtual environment (optional):
    ```bash
    py -m venv venv
    .\venv\Scripts\activate
    ```
    Install all Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Back-End Environment**
    Create a `.env` file based on the `.env.example` template and adjust the configuration as needed.

4. **Run the Back-End Application**
    To start the backend application, use the command:
    ```bash
    uvicorn main:app --reload
    ```

5. **Access the Back-End API**
    The API will be available at `http://localhost:8000`.

6. **Install Front-End Dependencies**
    Run the following command to install all dependencies:
    ```bash
    cd front_end
    npm install
    ```

7. **Configure Front-End Environment**
    Create a `.env` file based on the `.env.example` template and adjust the configuration as needed.

8. **Run the Front-End Application**
    To start the application, use the command:
    ```bash
    npm run dev
    ```

9. **Access the Front-End Application**
    Open your browser and access the application at `http://localhost:5173`.

## Notes
If you encounter any issues, refer to the documentation or contact the developer.
