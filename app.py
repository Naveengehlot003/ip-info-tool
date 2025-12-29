from flask import Flask, render_template, request, redirect, send_file, session
import requests
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = "secure_key_here"   # required for history storage

# ---------- IP Lookup ----------
def get_ip_info(ip):
    url = f"https://ipapi.co/{ip}/json/"
    return requests.get(url).json()

@app.route("/", methods=["GET", "POST"])
def index():
    if "history" not in session:
        session["history"] = []

    user_ip = request.remote_addr
    data = None

    if request.method == "POST":
        ip = request.form.get("ip_input")
        data = get_ip_info(ip)
    else:
        data = get_ip_info(user_ip)

    # Save to history
    session["history"].append({
        "ip": data.get("ip"),
        "city": data.get("city"),
        "country": data.get("country_name")
    })
    session.modified = True

    return render_template("index.html", data=data, history=session["history"])

# ---------- PDF Download ----------
@app.route("/download_pdf/<ip>")
def download_pdf(ip):
    data = get_ip_info(ip)

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    y = 800
    p.drawString(50, y, "IP Address Report")
    y -= 40

    for k, v in data.items():
        p.drawString(50, y, f"{k}: {v}")
        y -= 20
        if y < 50:
            p.showPage()
            y = 800

    p.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"ip_report_{ip}.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run(debug=True)
