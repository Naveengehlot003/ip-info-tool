# 🌐 IP Address Information Tool

A Flask-based web application that allows users to look up IP address details, view the approximate geographic location on an interactive map, maintain a search history, and download IP reports as PDF files.

## ✨ Features
- 🔍 Lookup detailed IP address information
- 📍 View location on an interactive Leaflet Map
- 🏛 Automatically detect user IP
- 🕘 Session-based search history
- 📄 Download IP report as PDF (ReportLab)
- 🌙 Clean and responsive Bootstrap UI
- 🚀 Ready for deployment on Render

## 🖼️ Demo (Screenshots)
- IP details view
- Map location preview
- PDF download option
- Search history section
(Add screenshots after deployment)

## 🛠️ Tech Stack
- Python
- Flask
- Requests API
- Leaflet (OpenStreetMap)
- Bootstrap
- ReportLab (PDF generation)

## 📂 Project Structure
ip-info-tool/
 ├─ app.py
 ├─ templates/
 │   └─ index.html
 ├─ static/
 ├─ requirements.txt
 └─ Procfile

## ⚙️ Installation (Local Setup)
git clone <repo-url>
cd ip-info-tool

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app.py

Open in browser:
http://127.0.0.1:5000/

## 🚀 Deploy on Render
1. Push project to GitHub
2. Create Web Service on Render
3. Use these commands:

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app

## 🧾 Environment Variables (Optional)
SECRET_KEY = your_secure_key

## 🗺️ APIs Used
- ipapi.co — IP lookup service
- OpenStreetMap / Leaflet — Map tiles

## 📌 Future Enhancements
- User authentication
- Database-based history
- CSV export support
- Light/Dark theme toggle
- Geo-analytics dashboard

## 🤝 Contributing
Contributions are welcome.
For major changes, open an issue first.

## 👨‍💻 Author
Developed by Naveen Gehlot

