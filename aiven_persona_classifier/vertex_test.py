import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel


load_dotenv()

project_id = os.getenv("VERTEX_PROJECT_ID")

vertexai.init(project=project_id, location="us-central1")

model = GenerativeModel(model_name="gemini-1.5-flash-001")

response = model.generate_content(
    "What's a good name for a flower shop that specializes in selling bouquets of dried flowers?"
)

print(response.text)