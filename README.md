# 🌧️ Rain Alert with SMS Notification

This Python script checks upcoming weather forecasts using the **OpenWeatherMap API** and sends an SMS alert via **Twilio** if rain is expected in the next few hours.

---

## 📌 Features

- ✅ Checks short-term (3-hour interval) weather forecasts.
- ✅ Detects if rain is expected in the next 12 hours.
- ✅ Sends SMS alerts automatically using Twilio.
- ✅ Secure credentials using environment variables.
- ✅ Proxy support for cloud deployment (e.g., PythonAnywhere).

---

## 🛠️ Requirements

- Python 3.7+
- OpenWeatherMap API key
- Twilio account with a verified phone number

---

## 📦 Dependencies

Install required packages using:

```bash
pip install -r requirements.txt
```
---

### Required packages:
- requests
- twilio
- python-dotenv (optional, for local development)

---

## 🔐 Environment Variables
Store the following credentials as environment variables (e.g., in a .env file for local development):
```bash

TWILIO_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
OWM_API_KEY=your_openweathermap_api_key

# Optional (for proxy support)
http_proxy=http://your.proxy:port
https_proxy=https://your.proxy:port

```
---

## 📍 Configuration
The location used in this script is:
```bash
Latitude: your_latitude
Longitude: your_longitude
```
To customize, change the coordinates in weather_params.

---

## 🚀 How to Run
▶️ Locally (with .env)
1. Clone this repository:
 ```bash

git clone https://github.com/yourusername/rain-alert.git
cd rain-alert

```
2. Create a .env file with your credentials.
3. Run the script:
```bash

python main.py

```

---


## 🌐 Deployment on PythonAnywhere
To deploy this on PythonAnywhere:
1. Upload your project files.
2. Set environment variables in:
   - Web > Environment Variables or in .bashrc.
3. Schedule the script via Tasks > Schedule a new task.

---

## 🧪 Sample Output
If rain is expected:
```bash
Rain expected — sending SMS...
Message sent with status: queued
```
If no rain:
```bash
No rain expected in the next few hours.
```
---

## 📄 License
This project is licensed under the MIT License.
---

## 🤝 Contributing
Feel free to fork the repo and open pull requests. Feedback and suggestions are welcome!
---
## 📞 Contact
Created by Sayan Sanki
📧 sayansanki1997@gmail.com

📧 sayansanki1997@gmail.com
   






