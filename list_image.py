import docker 

client = docker.from_env()

def list_image():
    
    # get images
    images = client.images.list(all=True)

    # display

    for image in images:
        print(f"ID: {image.id[:12]}")
        print(f"Tags: {image.tags}")
        print(f"Size: {image.attrs['Size']}bytes")
        print("-" * 20)

if __name__ == "__main__":
    list_image()

def list_ubuntu_images():
    
    images = client.images.list(all=True)

    for image in images:
        if image.tags and "ubuntu" in image.tags[0].lower(): 
            print(f"ID: {image.id[:12]}")
            print(f"Tags: {image.tags}")
            print(f"Size: {image.attrs['Size']}bytes")
            print("-" * 20)

if __name__ == "__main__": 
    list_ubuntu_images()
    

    

  