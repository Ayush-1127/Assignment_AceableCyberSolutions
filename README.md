# Assignment_AceableCyberSolutions

This repository contains Docker images for both the frontend and backend of the Assignment Aceable Cyber Solutions project. Follow the instructions below to pull and run the images.

---

##  Pull Docker Images

To pull the frontend and backend Docker images from Docker Hub, run the following commands:

```sh
docker pull ayush799/assignment_aceablecybersolutions:frontend-v1
docker pull ayush799/assignment_aceablecybersolutions:backend-v1
```

---

##  Run Docker Containers

Once the images are pulled, you can run them using the following commands:

```sh
docker run -p 3000:80 ayush799/assignment_aceablecybersolutions:frontend-v1
docker run -p 8000:8000 ayush799/assignment_aceablecybersolutions:backend-v1
```

- The **frontend** will be available at: `http://localhost:3000`
- The **backend** will be running at: `http://localhost:8000`

---

## 🛠️ Setting Up the Frontend

If you want to set up the frontend manually, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/Ayush-1127/Assignment_AceableCyberSolutions.git
   ```
2. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
3. Install dependencies:
   ```sh
   npm install
   ```
4. Start the development server:
   ```sh
   npm run dev
   ```

---

## 🛠️ Setting Up the Backend

To set up the backend manually, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/Ayush-1127/Assignment_AceableCyberSolutions.git
   ```
2. Navigate to the backend directory:
   ```sh
   cd backend
   ```
3. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Run database migrations:
   ```sh
   python manage.py migrate
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

Now, the backend will be running at `http://localhost:8000`.

---


