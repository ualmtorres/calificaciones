from fastapi import APIRouter

router = APIRouter()

califications = [
    {"id": 1, "student": "Robert Smith", "calification": 5},
    {"id": 2, "student": "Jane Atkinson", "calification": 6},
    {"id": 3, "student": "Mary Johnson", "calification": 7}
]

# Define route to get all califications
@router.get("/")
async def get_califications():
    return califications

# Define route to get a calification by ID
@router.get("/{calification_id}")
async def get_calification(calification_id: int):
    for calification in califications:
        if calification["id"] == calification_id:
            return calification
    return {"error": "Calification not found"}