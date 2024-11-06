# BookStream - Book Cataloging App

A streaming selection and book cataloging application that allows users to register and evaluate books across different platforms. This MVP (Minimum Viable Product) project connects with a dedicated API for book evaluation and registration.

![LSCC-callout](https://github.com/user-attachments/assets/946818cb-85c7-405c-986f-98966623bed1)

## 🎯 Features

- Book registration with streaming platform selection
- Book evaluation system with grades and comments
- Support for multiple streaming platforms:
  - Amazon Kindle
  - Physical Books
- Interactive user interface built with Flet
- Integration with dedicated API for data persistence

## 🔧 Dependencies

- Python 3.x
- Flet
- Requests
- HTTPX
- JSON

## 🚀 Getting Started

### Prerequisites

1. Clone both repositories:
```bash
# Main application
git clone https://github.com/Caio-Felice-Cunha/BookStream-API-Django-Flat.git

# Required API
git clone https://github.com/Caio-Felice-Cunha/API-Book-Reg-Aval.git
```

2. Install required packages:
```bash
pip install flet requests httpx
```

### Running the Application

1. First, start the API server
2. Run the main application:
```bash
python main.py
```

## 💻 Usage

1. **Register a Book**:
   - Enter the book name
   - Select the streaming platform (Amazon Kindle or Physical Book)
   - Click "Register"

2. **Evaluate a Book**:
   - Click on a book from the list
   - Provide a grade (1-5)
   - Add your comments
   - Click "Evaluate"

## 🔄 API Integration

The application integrates with a dedicated API that handles:
- Book storage and retrieval
- Evaluation management
- Data persistence

## 🌟 Acknowledgments

This project was developed as part of the "4 days 4 projects" initiative by [Pythonando](https://pythonando.com.br) on YouTube.

## ⚠️ Note

This is an MVP (Minimum Viable Product) version of the application. Features and functionality may be limited or subject to change in future versions.
