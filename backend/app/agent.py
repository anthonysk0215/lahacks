from uagents import Agent, Context, Protocol
from .models import LocationInput, Landmark, TourRecommendation
from typing import List
from datetime import datetime

class TourGuideAgent:
    def __init__(self):
        # Updated Agent initialization without address parameter
        self.agent = Agent(
            name="tour_guide_agent",
            port=8000,
            endpoint=["http://127.0.0.1:8000/submit"]
        )
        
        # Set up the protocol
        self.protocol = Protocol("tour_recommendations")
        self.setup_protocol()

    def setup_protocol(self):
        @self.protocol.on_message
        async def handle_location(ctx: Context, sender: str, msg: dict):
            try:
                # Convert dict to LocationInput
                location = LocationInput(**msg)
                recommendations = self.process_recommendations(location)
                return recommendations.dict()
            except Exception as e:
                ctx.logger.error(f"Error processing location: {e}")
                return {"error": str(e)}

    def process_recommendations(self, location: LocationInput) -> TourRecommendation:
        # Process landmarks and create recommendations
        landmarks = self.rank_landmarks(location.landmarks or [])
        route_order = self.calculate_optimal_route(landmarks, location)
        total_time = self.calculate_total_time(landmarks)

        return TourRecommendation(
            landmarks=landmarks,
            route_order=route_order,
            total_time=total_time
        )

    def rank_landmarks(self, landmarks: List[dict]) -> List[Landmark]:
        # Convert dict landmarks to Landmark objects and rank them
        landmark_objects = [Landmark(**l) for l in landmarks]
        
        # Sort by rating and distance
        return sorted(
            landmark_objects,
            key=lambda x: (x.rating or 0) - (x.distance or 0) / 10000
        )

    def calculate_optimal_route(self, landmarks: List[Landmark], location: LocationInput) -> List[int]:
        # Simple ordering based on distance
        return list(range(len(landmarks)))

    def calculate_total_time(self, landmarks: List[Landmark]) -> int:
        return sum(l.estimated_time or 30 for l in landmarks)

    async def get_tour_recommendations(self, location: LocationInput) -> TourRecommendation:
        return self.process_recommendations(location) 