from pydantic import BaseModel, Field

class Todo(BaseModel):
    id: int = Field(None, description="Auto-generated ID") # Optional field (None), auto-generated ID
    task: str = Field(..., max_length=50) # Required field (...), max length 50 characters

