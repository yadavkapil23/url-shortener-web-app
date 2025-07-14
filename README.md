# ⚡ URLZap - FastAPI URL Shortener Web App 🌐

URLZap is a lightweight and intuitive URL shortening web application built using **FastAPI**, with support for tracking analytics like **click count**. Easily shorten long URLs and monitor their usage — all with a modern, responsive interface.

---

## 🚀 Features

- 🔗 **URL Shortening** – Generate short, unique URLs in one click.
- 📊 **Analytics Dashboard** – Track click counts on shortened links.
- 🌐 **Redirection** – Automatically redirect users to the original URL.
- 💡 **Minimal UI** – Clean and focused user experience.
- 💾 **Local JSON Storage** – Simple backend using `urls.json`.

---

## 📁 Project Structure

```bash
urlzap-webapp/
├── app/
│   ├── main.py              
│   ├── shortener.py         
│   ├── storage.py           
│   └── templates/
│       ├── index.html       
│       └── analytics.html   
├── data/
│   └── urls.json            
├── .gitignore               
├── requirements.txt         
├── README.md                

```

## ⚙️ Setup & Installation

### 🔧 Prerequisites

Ensure you have:

- ✅ Python 3.7+
- ✅ pip (Python package manager)
- ✅ Virtual environment (optional but recommended)

### 💻 Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/yadavkapil23/url-shortener-web-app.git
cd url-shortener-web-app

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the FastAPI app
uvicorn app.main:app --reload

# Open your browser at:
http://127.0.0.1:8000

```
## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute with attribution.

---

🎉 **Thank you for using URLZap!**  
If you have suggestions, ideas, or feedback — feel free to open an issue or contribute via a PR.

