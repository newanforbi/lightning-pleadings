"""Lightning Pleadings — Random Lawsuit Generator."""

from flask import Flask, render_template, send_file

from pleading.generator import generate_lawsuit_pdf

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    pdf_buffer = generate_lawsuit_pdf()
    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=False,
        download_name="lawsuit.pdf",
    )


if __name__ == "__main__":
    app.run(debug=True)
