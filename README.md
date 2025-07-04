
# FASTx

FASTx is a **Flask-based full-stack web application**, inspired by Blinkit, designed to simulate a hyperlocal grocery delivery service with integrated support for customers, store managers, delivery agents, and administrators. The system enables browsing, ordering, managing inventory, and optimizing deliveries in real time.

---

## 🚀 Objective

To create a modular, scalable, and testable delivery system that supports:

### 🛒 Customer Interface

- Browse items from multiple stores with detailed product information.
- Search by item name and category.
- Real-time stock availability indicators.
- Shopping cart management (add/remove functionality).
- Multiple payment options: **Card, UPI, COD**.
- View order history and track orders in real-time.

### 🚚 Delivery System

- Track real-time order status: *collected, in transit, delivered*.
- Maintain delivery history for all agents.
- Assign delivery tasks based on location and availability.
- Pre-computed distance matrices for fast route optimization.
- Dynamic shortest-path route planning considering:
  - Delivery agent's current location
  - Store locations
  - Customer addresses
  - Order status

### 🏬 Store Management

- Dedicated dashboards for each store manager (3 stores total).
- Inventory management: add, edit, remove items.
- Monitor and update stock levels.
- Manage prices and discounts.
- Handle and track order fulfillment.
- View store-specific analytics and order history.

### 🛠️ Admin Dashboard

- Oversee all users, stores, and orders.
- Monitor delivery agents and their assignments.
- View system-wide statistics and performance analytics.

### 🔐 Authentication & Security

- Secure login system for all roles (customer, delivery, store, admin).
- **Role-based access control**.
- Passwords hashed with **bcrypt**.
- Session management for seamless navigation and persistent login.

---

## 🧱 Project Structure

```bash
SW_PROJECT_2025/
│
├── app/                      # Core application logic
│   ├── auth/                 # Authentication and login/logout
│   ├── customer/             # Customer views and logic
│   ├── delivery/             # Delivery agent dashboards
│   ├── store/                # Store manager interface
│   ├── admin/                # Admin dashboard
│   ├── utils/                # Utility functions (e.g. distance calculator)
│   └── templates/            # Jinja2 HTML templates
│
├── tests/                    # Pytest-based test cases
│
├── .github/workflows/       # CI workflow using GitHub Actions
│   └── python-app.yml
│
├── run.py                   # Entry point to start Flask app
├── config.py                # Configuration settings
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python package dependencies
└── RUNER 1.pptx             # Presentation slides
````

---

## 🧪 Testing

* All modules include **unit and integration tests** under the `tests/` directory.
* Uses **pytest** for testing.
* Code coverage is tracked via `coverage.py` and exported to `coverage.xml`.

### 📦 To run tests:

```bash
pip install -r requirements.txt
pytest --cov=app tests/
```

---

## ⚙️ CI/CD Integration

The project uses **GitHub Actions** for Continuous Integration.

### 📄 `.github/workflows/python-app.yml`

The workflow performs:

* Code checkout
* Python environment setup
* Dependency installation
* Running unit tests with `pytest`
* Checking code coverage

This ensures all pushes and pull requests are automatically validated.

---

## ✅ Getting Started Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abhinavteja2005/SW_PROJECT_2025.git
   cd SW_PROJECT_2025
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   ```bash
   python run.py
   ```

4. **Access the app at:**

   ```
   http://localhost:5000/
   ```

---

## 👤 Roles Summary

| Role          | Features                                                            |
| ------------- | ------------------------------------------------------------------- |
| **Customer**  | Browse, search, add to cart, place order, track order, view history |
| **Store Mgr** | Inventory management, order processing, analytics                   |
| **Delivery**  | View assigned deliveries, status updates, optimized route mapping   |
| **Admin**     | System-wide monitoring, user tracking, performance analytics        |

---

## 🧠 Tech Stack

* **Backend**: Python, Flask
* **Frontend**: HTML, CSS, Jinja2 Templates
* **Database**: Python
* **Authentication**: Flask-Login, bcrypt
* **Testing**: Pytest, Coverage.py
* **CI/CD**: GitHub Actions

---

## 📎 Contributors

* [Dasari Veera Venkata Abhinav Teja](https://github.com/abhinavteja2005)
* [Pulugu Lokeswara Reddy]
--

```

```
