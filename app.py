import gradio as gr
import requests
import os

from dotenv import load_dotenv 
load_dotenv() 

API_KEY = os.getenv("STABILITY_API_KEY")
API_ENDPOINT = os.getenv("STABILITY_API_ENDPOINT")

def generate_3d_model(image_file_path):
    try:
        response = requests.post(
            API_ENDPOINT,
            headers={
                "authorization": f"Bearer {API_KEY}",
            },
            files={
                "image": open(image_file_path, "rb")
            },
            data={},
        )

        if response.status_code == 200:
            output_path = "./output/output.glb"
    
            os.makedirs("./output", exist_ok=True)
            
            with open(output_path, 'wb') as file:
                file.write(response.content)
            
            return output_path, ""
        else:
            return None, f"Error: {response.status_code} - {response.json().get('errors', 'Unknown error')}"
    except Exception as e:
        return None, f"Exception occurred: {str(e)}"

iface = gr.Interface(
    fn=generate_3d_model,
    inputs=gr.Image(type="filepath"),
    outputs=[gr.Model3D(), gr.Textbox(label="Error Message", placeholder="")],
    title="Image to 3D Model Generator",
    description="Upload an image to generate and view a 3D model."
)

iface.launch()