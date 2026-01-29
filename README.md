# SocialCore-FastAPI

A modern, modular FastAPI-based social media backend application featuring user management, post creation, image handling, and JWT-based authentication. Built with clean architecture principles and RESTful API design.

## 🏗️ Architecture

SocialCore-FastAPI follows a well-structured, modular architecture that separates concerns and promotes maintainability:

```
SocialCore-FastAPI/
├── auth/                    # Authentication & Authorization
│   ├── authentication.py    # Login endpoint and token generation
│   └── oath2.py            # JWT token creation and validation
├── db/                      # Database Layer
│   ├── database.py         # Database connection and session management
│   ├── models.py           # SQLAlchemy ORM models (User, Post)
│   ├── db_user.py          # User CRUD operations
│   ├── db_post.py          # Post CRUD operations
│   └── hash.py             # Password hashing utilities
├── routers/                 # API Endpoints
│   ├── user.py             # User registration endpoints
│   └── posts.py            # Post creation, retrieval, and file upload
├── images/                  # Static file storage for uploaded images
├── main.py                  # Application entry point
├── schemas.py               # Pydantic models for request/response validation
└── requirement.txt          # Project dependencies
```

### Key Architectural Components

- **Routers**: Organize API endpoints by feature (users, posts, authentication)
- **Database Layer**: Separates database models (`models.py`) from business logic (`db_user.py`, `db_post.py`)
- **Authentication**: Centralized JWT-based security in the `auth/` directory
- **Schemas**: Pydantic models ensure data validation and serialization
- **Static Files**: Mounted `/images` directory for serving uploaded content

## ✨ Core Functionalities

### 1. User Management

- **User Registration**: Secure user creation with email and password validation
  - Email format validation using regex patterns
  - Password requirements: minimum 8 characters, at least one letter and one number
  - Automatic password hashing using bcrypt

- **JWT Authentication**: Token-based authentication for secure API access
  - Login via `/token` endpoint
  - Access tokens with 30-minute expiration
  - Protected endpoints require valid bearer tokens

### 2. Post System

- **Post Creation**: Users can create posts with captions and images
  - Support for both URL-based and uploaded images
  - Automatic timestamp recording
  - User association with posts (foreign key relationship)

- **Post Retrieval**: Fetch all posts with complete user information

- **Post Deletion**: Secured deletion with ownership verification

### 3. Image Upload & Storage

One of the standout features is the **secure random filename generation** for uploaded images:

```python
# Random 10-character alphanumeric string generation
rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
filename = f"{rand_str}{extension}"
```

**Benefits**:
- **Uniqueness**: Prevents filename collisions
- **Security**: Obscures original filenames, preventing path traversal attacks
- **Privacy**: Uploaded image names are not predictable

### 4. Static File Serving

The application mounts the `images/` directory as a static file endpoint:

```python
app.mount("/images", StaticFiles(directory="images"), name="images")
```

This allows uploaded images to be accessed via: `http://localhost:8000/images/{filename}`

## 📋 API Endpoints

### Authentication

| Method | Endpoint | Description | Authentication Required |
|--------|----------|-------------|------------------------|
| POST | `/token` | User login, returns JWT access token | No |

### User Management

| Method | Endpoint | Description | Authentication Required |
|--------|----------|-------------|------------------------|
| POST | `/user/` | Register a new user | No |

### Posts

| Method | Endpoint | Description | Authentication Required |
|--------|----------|-------------|------------------------|
| POST | `/post/create_post` | Create a new post | Yes |
| GET | `/post/all` | Retrieve all posts | No |
| POST | `/post/upload_file` | Upload an image file | No |
| DELETE | `/post/delete_post/{id}` | Delete a specific post | Yes |

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SocialCore-FastAPI
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv SocialEnv
   SocialEnv\Scripts\activate

   # Linux/MacOS
   python3 -m venv SocialEnv
   source SocialEnv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

   **Dependencies include**:
   - `fastapi` - Modern web framework
   - `uvicorn` - ASGI server
   - `sqlalchemy` - ORM for database operations
   - `pydantic` - Data validation
   - `bcrypt` - Password hashing
   - `python-multipart` - File upload support
   - `python-jose[cryptography]` - JWT token handling

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

   The server will start at `http://127.0.0.1:8000`

## 📚 API Documentation

FastAPI provides **automatic interactive API documentation**:

- **Swagger UI**: Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  - Interactive interface to test all endpoints
  - View request/response schemas
  - Authenticate and test protected endpoints

- **ReDoc**: Navigate to [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
  - Alternative documentation interface
  - Clean, organized endpoint documentation

## 🔐 Security Features

- **Password Hashing**: Bcrypt algorithm for secure password storage
- **JWT Tokens**: Stateless authentication with HS256 algorithm
- **Email Validation**: Regex-based email format verification
- **Password Policy**: Enforced complexity requirements
- **Protected Endpoints**: Bearer token authentication for sensitive operations
- **Random Filenames**: Prevents enumeration attacks on uploaded files

## 💾 Database

- **ORM**: SQLAlchemy for database abstraction
- **Database**: SQLite (`Instagram.db`) - easily swappable for PostgreSQL, MySQL, etc.
- **Models**:
  - **User**: Stores user credentials and profile information
  - **Post**: Stores post data with foreign key relationship to User

### Relationships
- One-to-Many: A user can have multiple posts
- Cascading: User posts are linked via SQLAlchemy relationships

## 🛠️ Development

### Project Structure Highlights

- **Modular Design**: Each feature is organized into its own module
- **Dependency Injection**: FastAPI's dependency system for database sessions and authentication
- **Type Safety**: Pydantic schemas ensure type validation at runtime
- **Separation of Concerns**: Clear distinction between routing, business logic, and data access

### Special Implementation Details

**Random Filename Generation** ([posts.py](posts.py#L43-L45)):
```python
rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
_, extension = os.path.splitext(file.filename)
filename = f"{rand_str}{extension}"
```

**Password Validation** ([schemas.py](schemas.py#L11-L18)):
- Minimum 8 characters
- At least one numeric digit
- At least one alphabetic character

## 📝 License

This project is open-source and available for educational and commercial use.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

**Built with ❤️ using FastAPI**
