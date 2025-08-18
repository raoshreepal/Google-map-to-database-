
# 🗺️ Django Google Maps Scraper

A **Django-based web application** that extracts business details from **Google Maps URLs** using **Selenium Web Scraping**.

This project allows you to enter a Google Maps link inside the **Django Admin Panel**, and it will automatically fetch details such as:

* ✅ Business Name
* ✅ Address
* ✅ Contact Number
* ✅ Website
* ✅ Email (if available)

The scraped data is stored in the database and can be managed directly through the **Django Admin** interface.

---

## 🚀 Features

* Add any **Google Maps business URL** in the admin panel.
* Auto-scraping of details using **Selenium**.
* Saves data in the database.
* Simple, frontend-less design (all management via Django Admin).
* Works on local or deployed servers.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Django 5+**
* **Selenium 4+**
* **Webdriver Manager** (for handling ChromeDriver)
* **SQLite / PostgreSQL**

---

## 📦 Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/django-google-maps-scraper.git
cd django-google-maps-scraper
```

2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run migrations

```bash
python manage.py migrate
```

5. Create superuser

```bash
python manage.py createsuperuser
```

6. Start server

```bash
python manage.py runserver
```

7. Login to **Django Admin** at:
   👉 [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🔧 How It Works

1. Login to **Django Admin**.
2. Add a new **Business** entry with a Google Maps URL.
3. On save, the scraper runs automatically and fetches business details.
4. The details are stored in the database and displayed in admin.

---

## 📂 Project Structure

```
project/
│── mapdata/
│   ├── models.py        # Business model
│   ├── admin.py         # Admin panel customization
│   ├── scraper.py       # Selenium scraping logic
│── project/
│   ├── settings.py      # Django settings
│── manage.py
```

---

## 📸 Screenshots

🔹 **Django Admin - Business Entry Form**
*Add image here*

🔹 **Scraped Business Details Stored**
*Add image here*

---

## ⚠️ Disclaimer

This project is made **for educational purposes only**.
Scraping Google Maps may violate their **Terms of Service**, so use it responsibly.

---

## 📌 Future Improvements

* Add deployment on **Vercel / Render**.
* Support batch scraping of multiple URLs.
* Export data as **CSV / Excel**.

---

## 🙌 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

## 📜 License

MIT License © 2025

---

