# Vacation Planning Assistant 🌴  

Welcome to the **Vacation Planning Assistant**, a Streamlit-based web app designed to help you plan your dream vacation effortlessly. Input your preferences, and let the app generate tailored travel recommendations based on your budget, available time, and travel preferences.

---

## Features ✨
- **Interactive Input Fields**  
  Enter your vacation preferences, such as destinations, budget, and available days, to receive customized travel recommendations.
  
- **Theme Customization**  
  Switch between **Light** and **Dark** themes for a personalized user experience.
  
- **AI-Powered Recommendations**  
  Powered by **Groq API**, the app generates vacation suggestions, including cost, days required, activities, and best travel times.

- **Sidebar Tools**  
  Explore travel tips, destination details, and budget breakdowns directly in the app's sidebar.

---

## Installation 🛠️

### Prerequisites
1. Install [Python 3.8+](https://www.python.org/).
2. Install `pip` (Python's package installer).
3. Set up an API key for [Groq API](https://groq.com/).

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vacation-planning-assistant.git
   cd vacation-planning-assistant
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory and add your API key:
   ```env
   GSK_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage 🚀

1. Open the app in your browser (`http://localhost:8501` by default).
2. Enter your vacation preferences:
   - **Destinations**: Specify your preferred locations or vacation types (e.g., "Paris", "Beaches").
   - **Budget**: Enter your budget in USD.
   - **Available Days**: Number of days you have for the vacation.
   - **Travel Preferences**: Choose from "Adventure", "Relaxation", or "Family-Friendly".
3. Click **Generate Recommendations** to view AI-suggested vacation plans.

4. Use the **Sidebar** to explore:
   - Destination Details
   - Travel Tips
   - Budget Breakdown

---

## Project Structure 📂

```plaintext
vacation-planning-assistant/
├── app.py                # Main Streamlit application
├── .env                  # Environment variables (add your API key here)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Themes 🌗

- **Light Theme**  
  Clean, bright, and minimalistic.

- **Dark Theme**  
  Eye-friendly dark mode with enhanced color contrast.

Switch between themes using the toggle button in the sidebar.

---

## Dependencies 📦

- [Streamlit](https://streamlit.io/) - Web application framework.
- [pandas](https://pandas.pydata.org/) - Data analysis and manipulation.
- [dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management.
- [Groq API](https://groq.com/) - AI-powered recommendations engine.
- [ast](https://docs.python.org/3/library/ast.html) - Safer evaluation of expressions.
- [re](https://docs.python.org/3/library/re.html) - Regular expressions for data extraction.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Contributing 🤝

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---



Happy vacation planning! 🎉
