#Plant tracker
##Very simple backend only CRUD API to track plants

##Tech Stack
-Python
-FastAPI
-Pydantic

##How to run
Create and activate a Python virtual environment:
python -m venv myenv
myenv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

From the project route, run:
uvicorn main:app --reload

The API will be available at: http://127.0.0.1:8000
Swagger documentation: http://127.0.0.1:8000/docs
