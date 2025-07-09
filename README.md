# Ratify – Django Backend

This is the backend for Ratify — a food expense tracking app built out of pure spite and practicality.

It takes scanned receipt data from the Flutter app, verifies the user via Firebase, and stores everything in a clean, searchable, rat-proof database. You want data? You want timestamps? You want a JSON breakdown of every euro spent and who paid it? Ratify gives it to you — without the lies.

## 🔥 Core Responsibilities

- Verifies Firebase ID tokens (no backend auth BS)
- Receives parsed expense data via REST
- Associates expenses with users and months
- Tracks who paid and what’s still unpaid
- Calculates 50/50 breakdowns (because that was the deal)

## 🛠️ Tech Stack

- Python 3.10
- Django
- Django REST Framework
- Firebase Admin SDK (for token validation)
- SQLite or PostgreSQL

## 📐 API Overview

| Endpoint                    | Method | Description                              |
|----------------------------|--------|------------------------------------------|
| `/api/expenses/add/`       | POST   | Submit an expense                        |
| `/api/expenses/month/`     | GET    | Retrieve all expenses for a given month |
| `/api/expenses/<id>/`      | PATCH  | Update payment status or details         |
| `/api/summary/<YYYY-MM>/`  | GET    | Get total per user and their share 💸    |

## 📦 Example Expense Payload

```json
{
  "date": "2025-07-08",
  "amount": 27.50,
  "description": "Mercadona groceries",
  "who_paid": "user_123",
  "paid_status": false,
  "raw_text": "MERCADONA\n8 JULY 2025\nTOTAL: 27.50 EUR\n..."
}
