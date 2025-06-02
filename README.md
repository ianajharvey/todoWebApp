# To-Do Web App

A simple and interactive To-Do List web application built using **Python** and **Streamlit**. Users can add tasks, mark them as completed, and delete them — all in a clean and responsive UI.
Built as part of a learning course

## Features

- Add new tasks via a text input
- Remove completed tasks from the list
- Tasks persist between sessions using file storage
- Instant updates using Streamlit's reactivity

## Installation

To run the app locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/ianajharvey/todoWebApp.git
cd todoWebApp
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

## Requirements

All dependencies are listed in `requirements.txt`. The app primarily uses:

- `streamlit`

## Future Improvements

- Add due dates and prioritization
- Enable persistent storage using a database (e.g. SQLite)
- User authentication for personalized lists

## License

This project is free to use
