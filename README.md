# Spotify Server

A FastAPI backend for a Spotify clone application.

## Local Development

1. Create a virtual environment: `python -m venv virtual_env`
2. Activate the virtual environment:
   - Windows: `virtual_env\Scripts\activate`
   - Unix/MacOS: `source virtual_env/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and update with your database credentials
5. Start the server: `uvicorn main:app --reload`

## Deploying to Render

### Automatic Deployment with Blueprint

This repository includes a `render.yaml` file which can be used for automatic deployment on Render.

1. Push this repository to GitHub
2. Create a new Blueprint on Render and connect to this repository
3. Render will automatically detect the `render.yaml` configuration and set up the services

### Manual Deployment

1. Create a new Web Service on Render
2. Connect to your GitHub repository
3. Select Python environment
4. For the build command, use: `pip install -r requirements.txt`
5. For the start command, use: `uvicorn main:app --host=0.0.0.0 --port=$PORT`
6. Add the environment variables:
   - `DATABASE_URL`: Your PostgreSQL connection string (with SSL enabled)

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
  Format: `postgres://username:password@hostname:port/database?sslmode=require`
- `PORT`: Port for the web server (set automatically by Render)