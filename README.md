# 🛒 Django E-commerce Project

Welcome to the Django E-commerce project! This repository contains a fully functional online store built using Django for the backend and modern web technologies for the frontend.

---

## 🔧 Features

- **User Authentication**: Register, log in, and manage accounts.
- **Admin Panel**: Fully customizable admin panel for managing products, orders, and users.
- **Product Management**: Add, edit, and delete products with categories.
- **Shopping Cart**: Seamlessly add, update, and remove items from the cart.
- **Order Processing**: Place orders and manage order history.
- **Responsive Design**: Optimized for all devices with a clean UI.

---

## 🟢 Backend Technologies

The backend of this project is powered by:

- **Django**: A high-level Python web framework.

---

## 🟡 Frontend Technologies

The frontend leverages:

- **HTML**
- **CSS**
- **Bootstrap**
- **JavaScript**

---

## 🚀 Getting Started

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

First, clone this repository to your local system using the following command:

```bash
git clone git@github.com:rezamardaniDev/PetHome.git
```

---

### 2. Set Up a Virtual Environment

Navigate to the project directory and create a virtual environment to isolate project dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

---

### 3. Install Dependencies

Install all required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

---

### 4. Run Database Migrations

Set up the database by running the migrations:

```bash
python manage.py migrate
```

---

### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

---

### 6. Access the Admin Panel

To log in to the admin panel, use the default credentials:

- **Username**: `admin`
- **Password**: `admin`

The admin panel is accessible at:

```
http://127.0.0.1:8000/admin/
```

---

## 📂 Project Structure

Below is an overview of the project's structure:

```
PetHome/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── app_name/  # Main application folder
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   └── urls.py
└── ...
```

---

## 📌 Contribution Guidelines

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Open a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

If you have any questions or feedback, feel free to reach out:

- **GitHub**: [rezamardaniDev](https://github.com/rezamardaniDev)

---

Thank you for checking out this project! Happy coding! 🎉
