# TextArtify1

TextArtify1 is a simple web application that uses the Hugging Face API to generate images from text prompts. It provides an easy-to-use interface powered by Gradio.

## Project Description

TextArtify1 allows users to input a textual description and receive a generated image based on that description. This project utilizes the `sd-community/sdxl-flash` model from Hugging Face's API to perform the image generation.

## Getting Started

To run this project locally, follow the steps below.

### Prerequisites

- Python 3.x
- Git

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Adeeb08/TextArtify1.git
    cd TextArtify1
    ```

2. **Create a Virtual Environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Your API Key**:
    - Create a `.env` file in the root directory of the project.
    - Add your Hugging Face API key to the `.env` file:
    ```env
    HUGGINGFACE_API_KEY=your_api_key_here
    ```

### Obtaining a Hugging Face API Key

1. **Sign Up or Log In** to [Hugging Face](https://huggingface.co/).
2. **Generate an API Key**:
    - Go to your profile settings.
    - Navigate to the API tokens section.
    - Generate a new token and copy it.
3. **Add the API Key to Your `.env` File**:
    - In your project directory, create a `.env` file if it doesn't already exist.
    - Add the following line to your `.env` file, replacing `your_api_key_here` with the token you just generated:
    ```env
    HUGGINGFACE_API_KEY=your_api_key_here
    ```

### Usage

1. **Run the Application**:
    ```sh
    python script.py
    ```

2. **Access the Interface**:
    - The application will provide a local URL (e.g., `http://127.0.0.1:7860`) that you can open in your web browser.
    - Enter a text prompt and click "Submit" to generate an image.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
