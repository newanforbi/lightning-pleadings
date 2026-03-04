# Lightning Pleadings

A random lawsuit generator web app — dedicated to the legal beagles in penal institutions everywhere, and particularly to those at San Quentin who dared to challenge the status quo.

I now find myself embroiled in several lawsuits in California, so naturally I built a web app that generates fake lawsuit PDFs at the push of a button. Hit the button, get a professionally formatted pleading complete with randomized parties, causes of action, and legal boilerplate. Every refresh is a new case.

## Tech Stack

- **Flask** — lightweight Python web framework
- **ReportLab** — PDF generation engine for court-formatted pleadings
- **Gunicorn** — production WSGI server
- **Render** — cloud hosting and deployment

## Built Different

This entire project — every line of code, every template, every config file — was built with **Claude** straight from my **iPhone**. No laptop. No desktop. Just me, my phone, and an AI pair programmer. Proof that you can ship real software from anywhere, with anything.

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) and start generating lawsuits.

## Deploy

This app is configured for one-click deploy on Render via `render.yaml`. Connect the GitHub repo and let it rip.

## Live Demo

Check it out: [https://lightning-pleadings.onrender.com](https://lightning-pleadings.onrender.com)
