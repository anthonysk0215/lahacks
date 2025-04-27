# WayFinder AI: Your Automated Tour Guide

An augmented reality tour guide application built for Snap Spectacles, providing real-time location-based recommendations and interactive map features. The application combines Snap's AR capabilities with Fetch.ai's autonomous agents for intelligent tour recommendations.

## 🚀 Features

- Real-time location tracking
- Interactive map with place markers
- AR information cards for nearby places
- AI-powered tour recommendations using Fetch.ai agents
- Integration with Snap Places API
- Autonomous agent-based decision making for personalized tours

## 🛠️ Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: Lens Studio (Spectacles)
- **APIs**: 
  - Snap Places API
  - Fetch.ai uAgents
- **Location Services**: GPS and AR tracking
- **AI/ML**: Fetch.ai Autonomous Agents

## 📋 Prerequisites

- Python 3.8+
- Lens Studio
- Git
- Snap Spectacles (optional, can use Lens Studio emulator)
- Snap Places API credentials
- Fetch.ai API credentials (contact project maintainer)

## 🚀 Getting Started

### Backend Setup

1. **Clone the repository**
```bash
git clone https://github.com/anthonysk0215/lahacks.git
cd lahacks
```

2. **Set up Python environment**
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the backend directory:
```bash
touch .env
```
Add your API keys and configuration:
```
SNAP_PLACES_API_KEY=your_snap_api_key
FETCH_AI_API_KEY=your_fetch_ai_api_key
```
(Contact project maintainer for required keys)

5. **Start the backend server**
```bash
python main.py
```
Server runs on `http://localhost:8001`

### Frontend Setup (Lens Studio)

1. **Open the project**
- Launch Lens Studio
- File > Open Project
- Navigate to `Spectacles-Sample` directory
- Select the project

2. **Configure APIs**
- Set up your Snap Places API credentials
- Configure Fetch.ai agent settings
- Update API configuration in project settings

3. **Test the application**
- Connect Spectacles device or use Lens Studio emulator
- Ensure backend server is running
- Test map functionality and place detection
- Verify AI-powered recommendations

## 🤝 Contributing

1. **Create a new branch**
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes**
- Follow the project's coding style
- Add tests if applicable
- Update documentation

3. **Commit your changes**
```bash
git add .
git commit -m "Description of your changes"
```

4. **Push to the branch**
```bash
git push origin feature/your-feature-name
```

5. **Create a Pull Request**
- Go to the GitHub repository
- Create a pull request from your branch to main
- Request review from team members

## 📝 Project Structure

```
.
├── backend/               # Python FastAPI backend
│   ├── app/              # Application code
│   │   ├── agent.py      # Fetch.ai agent implementation
│   │   └── models.py     # Data models
│   ├── main.py           # Main server file
│   └── requirements.txt  # Python dependencies
├── Spectacles-Sample/    # Lens Studio project
│   ├── Assets/          # Project assets
│   └── Scripts/         # Lens Studio scripts
└── README.md            # This file
```

## 🙏 Acknowledgments

- Snap Inc. for Lens Studio and Spectacles platform
- Fetch.ai for autonomous agent technology
- Contributors and maintainers
