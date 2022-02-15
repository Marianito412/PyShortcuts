from msilib.schema import Shortcut
import requests, json
import os
from ui import ShortcutWidget
DEBUG = True

if DEBUG:
    import keys
    BOT_API_KEY = keys.orwellKey

    NotionKey = keys.NotionSecret
    databaseId = keys.NotionDatabaseId
else:
    BOT_API_KEY = os.environ.get("ORWELL_API")

    NotionKey = os.environ.get("NOTION_KEY")
    databaseId = os.environ.get("DATABASE_ID")

header = {
    "Authorization": f"Bearer {NotionKey}",
    "Notion-Version": "2021-05-13",
    "Content-Type": "application/json",
}

def add_task(value):

    projects_url = "https://api.notion.com/v1/search"

    projects = requests.request("POST", projects_url, json={"page-size": 100}, headers=header).json()
    for project in projects["results"]:
        try:
            if project["properties"]["Name"]["title"][0]["plain_text"] == value.split(": ")[0]:
                page_id = project["id"]
                url = f"https://api.notion.com/v1/blocks/{page_id}/children"
                print(page_id)
        except:
            pass
    tickets_id = requests.request("GET", url, headers=header).json()["results"][-1]["id"]

    title = value.split(": ")[1]
    payload = {
        "parent": {"type": "database_id", "database_id": f"{tickets_id}"},
        "properties":{
            "Name": {"title": [{"text": {"content": f"{title}"}}]},
        }
    }
    add_url = f"https://api.notion.com/v1/pages"
    response = requests.request("POST", add_url, json=payload, headers = header).json()
    print(response)

if __name__ == "__main__":
    add_task("InfiniteJourney: Stuff to do")