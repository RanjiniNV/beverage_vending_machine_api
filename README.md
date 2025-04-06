# 🥤 Beverage Vending Machine API

A simple backend API for a beverage vending machine built with **FastAPI** and **MongoDB**.  
It allows you to manage inventory, define drink recipes, place orders, and view the drink menu – all through easy-to-use RESTful endpoints.

> 🔧 No authentication has been added yet – this is currently an open API for learning and testing purposes.

---

## 🚀 Features

- Add inventory items (ingredients)
- Define recipes for beverages
- Place drink orders (auto-deducts ingredients)
- View full menu and recipe details
- Swagger UI for easy testing and interaction

---

## 📂 Project Structure

- **Inventory** – Tracks current available ingredients
- **Recipe** – Stores beverage compositions
- **Orders** – Keeps history of all drink orders

These are stored in the `vending_db` MongoDB database.

---

## 🛠 Tech Stack

- **FastAPI** – Python web framework
- **MongoDB** – NoSQL database
- **pymongo** – MongoDB driver for Python
- **Uvicorn** – ASGI server for FastAPI

---

## ⚙️ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/vending-machine-api.git
cd vending-machine-api
