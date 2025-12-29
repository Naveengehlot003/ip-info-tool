🌐 IP Address Information Tool

A Flask-based web application that lets users lookup IP address details, view approximate location on a map, maintain search history, and download IP reports as PDF.

✨ Features

🔍 Lookup IP address information

📍 View location on interactive Leaflet Map

🏛 Auto-detect user IP

🕘 Search history (session-based)

📄 Download IP report as PDF (ReportLab)

🌙 Clean Bootstrap UI

🚀 Ready to deploy on Render

🖼️ Demo (Screenshots)

IP details display

Location map preview

PDF download button

Search history section

(Add screenshots here when deployed)

🛠️ Tech Stack

Python

Flask

Requests API

Leaflet Map

Bootstrap

ReportLab (PDF)

📂 Project Structure
ip-info-tool/
 ├─ app.py
 ├─ templates/
 │   └─ index.html
 ├─ static/
 ├─ requirements.txt
 └─ Procfile

⚙️ Installation (Local Setup)
git clone <repo-url>
cd ip-info-tool

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app.py


Open in browser:

http://127.0.0.1:5000/

🚀 Deploy on Render

Push project to GitHub

Create Web Service on Render

Use:

Build Command

pip install -r requirements.txt


Start Command

gunicorn app:app


Done 🎉

🧾 Environment Variables (Optional)

Add on Render dashboard:

SECRET_KEY = your_secure_key

🗺️ APIs Used

ipapi.co – IP information lookup

OpenStreetMap / Leaflet – Map tiles

📌 Future Enhancements

User authentication

Database-based history

CSV export

Light/Dark theme switch

Geo-location analytics dashboard

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.


👨‍💻 Author

Developed by Naveen Gehlot
Feel free to connect or contribute 🙂
