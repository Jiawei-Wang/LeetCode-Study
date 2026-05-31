# server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so your JavaScript client can safely communicate with this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permits requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Permits GET, POST, etc.
    allow_headers=["*"],
)

# Mock Database: A single post with one initial comment
posts_db = {
    1: {
        "id": 1,
        "title": "Learning APIs with Code",
        "content": "Seeing actual code makes abstract concepts click.",
        "comments": [
            {"id": 1, "text": "This is a great start!"}
        ]
    }
}

# Define what data we expect when someone adds a comment
class CommentSchema(BaseModel):
    text: str


# ENDPOINT 1: Fetch a post and its comments
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts_db[post_id]


# ENDPOINT 2: Add a comment to a specific post
@app.post("/posts/{post_id}/comments")
def add_comment(post_id: int, comment: CommentSchema):
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Generate an incremental ID for the new comment
    new_id = len(posts_db[post_id]["comments"]) + 1
    new_comment = {"id": new_id, "text": comment.text}
    
    # Append it to our mock database
    posts_db[post_id]["comments"].append(new_comment)
    
    return {"message": "Comment added successfully!", "comment": new_comment}

# To run this server, you would execute this in your terminal:
# uvicorn server:app --reload