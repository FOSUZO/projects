# Vulnerability Scanner - Portfolio Project

## Project Overview
This is a **portfolio-ready Vulnerability Scanner** built using **Python** and **FastAPI**.  
It allows users to scan multiple URLs for common web vulnerabilities, open ports, and security headers.  
The application provides a **user-friendly web interface** with progress bar, loading spinner, and color-coded results.

---

## Features
- Scan multiple URLs simultaneously
- Check for basic **OWASP Top 10 vulnerabilities**:
  - SQL Injection
  - XSS (Cross-site scripting)
  - Open Redirect
- Scan for **open ports** (80, 443, 8080, 8000)
- Detect if site uses **HTTPS**
- Display results in **color-coded cards**:
  - Red = Possible vulnerability
  - Green = Safe
- Save scan results as **JSON** files in `results/` folder
- **Responsive design** using Bootstrap
- **Progress bar and loading spinner** during scan

---

## Technologies Used
- Python 3.x
- FastAPI
- aiohttp, asyncio
- Jinja2 templating
- Bootstrap 5
- tqdm (for progress)

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_GITHUB_LINK/vuln_scanner_portfolio.git
   cd vuln_scanner_portfolio
2. Create and activate a virtual environment:   
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. How to Run
   ```bash
   uvicorn main:app --reload
  
 Open your browser at http://127.0.0.1:8000 
 - Enter URLs separated by commas

 - Click Scan

 - View scan results on the page

 - JSON files are saved in results/ folder

---


##Demo

The result of scanning:

![Scan Results Screenshot](https://github.com/FOSUZO/projects/blob/main/vuln%20scanner/assets/screenshot.png?raw=true)





---

## Notes
- For educational purposes only

- Do not scan networks or websites without permission

- Always test on your own lab environment or public test sites

---

5. Open in browser:
   ```cpp
   vuln_scanner_portfolio/
   │── main.py
   │── scanner.py
   │── templates/
   │    └── index.html
   │── static/
   │    └── style.css
   │── results/
   │── requirements.txt
   │── README.md

## Author
# Sukhrob
- Portfolio project for Cybersecurity studies
- GitHub: https://github.com/FOSUZO/projects





 







