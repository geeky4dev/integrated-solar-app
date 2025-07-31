# ☀️ Integrated Solar App

**All‑in‑one solar energy platform** that integrates four existing solar web applications into a **single micro‑frontend host** with a **microservices/API backend orchestrator**.  
Seamlessly access **Solar AI Designer**, **Solar Radiation Dashboard**, **Solar Optimizer**, and **Solar Savings Calculator** in one place! 🚀

---

## 📌 Project Overview

This project connects **four specialized solar tools** into a **central hub**:

| App | Description | Backend API URL | Frontend URL |
|-----|-------------|-----------------|--------------|
| 🌞 **Solar AI Designer** | AI‑powered rooftop PV design assistant. | https://solar-ai-designer-backend.onrender.com | https://solar-ai-designer-frontend.onrender.com |
| 📊 **Solar Radiation Dashboard** | Explore solar radiation trends & maps. | https://solar-dashboard-ar8s.onrender.com | https://solar-dashboard-1.onrender.com |
| 🎯 **Solar Optimizer** (Tilt & Azimuth) | Find best tilt & orientation for panels. | https://solar-optimizer-backend.onrender.com | https://solar-orientation-tilt-app.onrender.com |
| 💰 **Solar Savings Calculator** | Estimate cost savings & ROI. | https://solar-savings-app-backend.onrender.com | https://solar-savings-app-frontend.onrender.com |

---

## 🛠 Architecture

The **Integrated Solar App** uses:

- 🖥 **Frontend Host** → React + Vite + Bootstrap (Micro‑frontend container).
- 🔌 **Backend Orchestrator** → Flask (Python) API Gateway for routing requests to the 4 microservices.
- 🧩 **Micro‑frontend Integration** → Each solar app runs independently but can also run inside this host.
- 🌐 **Remote APIs** → Calls existing deployed backends on Render.

**Architecture Diagram:**

[ User Browser ]  
|  
v  
[ Frontend Host (React) ]  
|  
v  
[ Backend Orchestrator (Flask) ]  
|  
+--> Solar AI Designer API  
+--> Solar Radiation Dashboard API  
+--> Solar Optimizer API  
+--> Solar Savings Calculator API  


---

## 📂 Project Structure  

Integrated-Solar-App/  
├── backend-orchestrator/ # Flask - API Gateway  
│ ├── app.py  
│ ├── requirements.txt  
│ ├── runtime.txt  
│ └── Procfile  
├── frontend-host/ # React - Micro-frontend host  
│ ├── index.html  
│ ├── package.json  
│ ├── vite.config.js  
│ └── src/  
│ ├── App.jsx  
│ └── components/  
├── README.md  
└── docker-compose.yml # Optional for local integration  


---

## 🚀 Getting Started (Local Development)  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/yourusername/Integrated-Solar-App.git
cd Integrated-Solar-App

2️⃣ Start the Backend Orchestrator (Flask)

cd backend-orchestrator
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run --port=5001

3️⃣ Start the Frontend Host (React + Vite)
Open a new terminal:

cd frontend-host
npm install
npm run dev

Your frontend should now be running at:

http://localhost:5173
and connected to the backend at:

http://localhost:5001


☁️ Deployment on Render
We use a single GitHub repo with two services on Render:

Backend Orchestrator
Type: Web Service
Language: Python
Root directory: backend-orchestrator/
Start command: gunicorn app:app

Frontend Host
Type: Static Site
Root directory: frontend-host/
Build command: npm install && npm run build
Publish directory: frontend-host/dist

Steps:
Push all changes to GitHub (git add . && git commit -m "update" && git push origin main).
In Render, create a Web Service for backend-orchestrator.

In Render, create a Static Site for frontend-host.
Update your frontend’s vite.config.js to proxy API requests to your deployed backend URL.

Deploy both services.

🎯 Features
✅ Centralized dashboard for all 4 solar tools
✅ Works with existing deployed backends
✅ Microservices & micro‑frontend architecture
✅ Modular — each tool can run standalone
✅ Clean, fast, and responsive UI

________________________________________

📜 License
MIT License © 2025 geeky4dev — use freely, with attribution. Contributions welcome!
Made with ☀️ and 💚 by geeky4dev for renewable energy enthusiasts!
________________________________________

🙌 Contributing
Feel free to open issues or submit pull requests! All contributions welcome.
________________________________________

🌞 Powering the future with the sun — one integrated app at a time!
