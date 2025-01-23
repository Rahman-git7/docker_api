from fastapi import FastAPI, HTTPException
import docker

app = FastAPI(title="Docker Management API")
client = docker.from_env()

@app.get("/containers")
async def list_containers():
    try:
        containers = client.containers.list(all=True)
        return [
            {
                "id": container.id[:12],
                "name": container.name,
                "status": container.status
            }
            for container in containers
        ]
    except docker.errors.APIError as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

#EOF
    