# Image to 3D Model Generator

This project is a simple Gradio web application that allows users to upload an image and generate a 3D model using Stability AI Stabale Fast 3D (SF3D) API. The generated 3D model is displayed in the application, and any errors encountered during the process are shown on the screen.

![demo](demo/demo.gif)

## Features

- Upload an image file to generate a 3D model.
- View the 3D model directly within the application.
- Displays error messages if something goes wrong during the model generation.

## Prerequisites

- Python 3.9 or later
- [Stability AI API key](https://stability.ai/) (required for accessing the 3D model generation service)
- Required Python packages (listed in the `requirements.txt`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/codemaker2015/image-to-3d-model-generator.git
   cd image-to-3d-model-generator
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add your Stability AI API key and endpoint like this:

   ```env
   STABILITY_API_KEY=your_stability_api_key
   STABILITY_API_ENDPOINT=your_stability_api_endpoint
   ```

   Replace `your_stability_api_key` and `your_stability_api_endpoint` with your actual Stability AI API key and endpoint.

## Usage

1. **Run the application:**

   ```bash
   python app.py
   ```

   This will launch the Gradio interface in your web browser.

2. **Using the Interface:**

   - **Upload an Image:** Click on the "Upload Image" button to upload the image file you want to convert to a 3D model.
   - **View 3D Model:** If the process is successful, the 3D model will be displayed in the app.
   - **Error Messages:** If there is an error, the error message will be displayed in the textbox below the 3D model viewer.

## File Structure

- `app.py`: The main application code.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `.env`: File to store environment variables (API keys).

## Example Output

- 3D Model: A `.glb` file format that can be viewed in the Gradio interface.
- Error Message: Displays any issues encountered during the API call, such as authorization failures or other errors.