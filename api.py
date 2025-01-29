from fastapi import FastAPI, HTTPException
import docker 


app = FastAPI(title="Docker Management API")
client = docker.from_env()

@app.get("/images")
async def get_images():
    try:
        images = client.images.list(all=True)
        return [
            {
                "id": image.id[:12],
                "tags": image.tags,
                "size": image.attrs["Size"]
            }
            for image in images
        ]
    except docker.errors.APIError as e:
        raise HTTPException(status_code=500, detail=str(e))
