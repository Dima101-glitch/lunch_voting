# Lunch Voting API

A Django REST API for managing restaurant menus and employee voting for lunch options. The project is containerized using Docker for easy deployment.

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/) installed

### Installation & Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/lunch_voting.git
   cd lunch_voting
   ```

2. **Create a `.env` file** (if required) based on `.env.example` and configure your environment variables.

3. **Build and start the Docker containers:**
   ```sh
   docker-compose up --build -d
   ```

4. **Apply database migrations:**
   ```sh
   docker-compose exec web python manage.py migrate
   ```

5. **Create a superuser:**
   ```sh
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Access the application:**
   - API: `http://localhost:8000/`
   - Admin Panel: `http://localhost:8000/admin/`

### Running Tests
To run tests inside the Docker container:
```sh
docker-compose exec web pytest
```

### Stopping the Project
To stop and remove containers:
```sh
docker-compose down
```
