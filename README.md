# chatbot_development

Chatbot In the competitive sphere of e-commerce, deploying advanced, interactive, and user-centric sales chatbots is essential for elevating customer experience and streamlining business operations.

# E-commerce Sales Chatbot

A full-stack chatbot for product search and conversation simulation built for Uplyft Internship (June 2025 Case Study).

---

## Features

- User registration/login (JWT Auth)
- Chatbot interface (React + Tailwind)
- Backend API (Flask + SQLAlchemy)
- Product filtering, search & mock data
- Conversation history storage

---

## Tech Stack

- **Frontend:** React.js, TailwindCSS
- **Backend:** Flask, Flask-JWT-Extended
- **Database:** SQLite + SQLAlchemy
---

## Setup Instructions

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed_data.py
python app.py
```

## Step 4.5: API Testing with Postman

### Purpose

Ensure all backend endpoints are functioning correctly and return expected responses using Postman.




### Expected Behavior

- Responses include valid data
- Token required for protected endpoints
- Error messages returned on bad inputs or missing auth
