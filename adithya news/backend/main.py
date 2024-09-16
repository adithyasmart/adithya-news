from fastapi import FastAPI, HTTPException
import httpx
import os
from pydantic import BaseModel
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = FastAPI()
HACKERNEWS_API_URL = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
STORY_BASE_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty"

class Story(BaseModel):
    title: str
    author: str
    url: str
    score: int
    time: str

@app.get("/top-stories", response_model=list[Story])
async def get_top_stories():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(HACKERNEWS_API_URL)
            response.raise_for_status()
            story_ids = response.json()[:10]
            stories = []

            for story_id in story_ids:
                story_response = await client.get(STORY_BASE_URL.format(story_id))
                story_response.raise_for_status()
                story_data = story_response.json()
                formatted_time = datetime.fromtimestamp(story_data['time']).strftime('%Y-%m-%d %H:%M:%S')
                stories.append(Story(
                    title=story_data['title'],
                    author=story_data['by'],
                    url=story_data['url'],
                    score=story_data['score'],
                    time=formatted_time
                ))

            return stories

    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail="Error fetching data from HackerNews API.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
