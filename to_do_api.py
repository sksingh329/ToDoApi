from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"id": 1, "name": "Do Yoga", "category": "Fitness", "status": "On Hold", "Note": "", "Due Date": "30-May-23"},
    {"id": 2, "name": "Walking/Running", "category": "Fitness", "status": "In Progress", "Note": "",
     "Due Date": "30-May-23"},
    {"id": 3, "name": "Learn Rest Assured", "category": "Learning", "status": "In Progress", "Note": "",
     "Due Date": "30-May-23"},
    {"id": 4, "name": "Learn Java", "category": "Learning", "status": "In Progress", "Note": "",
     "Due Date": "30-May-23"},
    {"id": 5, "name": "Fix Regression Issue", "category": "Work", "status": "Not Started", "Note": "",
     "Due Date": "30-May-23"}
]


@app.get("/")
def welcome():
    """Return welcome message"""
    return {"message": "Welcome to TO DO API"}


@app.get("/api/tasks")
def get_tasks(category : str | None = None, status : str | None = None) -> list:
    """Get tasks"""
    results = tasks
    if category:
        results = [result for result in results if result['category'] == category]
    if status:
        results = [result for result in results if result['status'] == status]
    return results


@app.get("/api/tasks/{id}")
def get_task_by_id():
    pass