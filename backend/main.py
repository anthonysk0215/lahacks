from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import LocationInput, TourRecommendation
from app.agent import TourGuideAgent
import uvicorn
from datetime import datetime

app = FastAPI(title="AR Tour Guide Backend")

# Allow CORS for Lens Studio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the tour guide agent
tour_guide = TourGuideAgent()

@app.post("/recommendations")
async def get_recommendations(location: LocationInput):
    try:
        response = await tour_guide.agent.get_tour_recommendations(location)
        return response.recommendation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}

if __name__ == "__main__":
    # Start the agent
    tour_guide.agent.run()
    
    # Start the FastAPI server on port 8001 instead
    uvicorn.run(app, host="0.0.0.0", port=8001)