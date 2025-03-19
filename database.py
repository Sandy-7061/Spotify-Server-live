from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if running on Render platform
is_render = os.getenv('RENDER') == 'true' or os.getenv('IS_RENDER') == 'true' or 'RENDER_SERVICE_ID' in os.environ

# Get DATABASE_URL from environment
DATABASE_URL = os.getenv('DATABASE_URL')

# Debug: Print environment variables
print("Environment variables:")
print(f"Running on Render: {'Yes' if is_render else 'No'}")
print(f"DATABASE_URL set: {'Yes' if DATABASE_URL else 'No'}")
if DATABASE_URL:
    # Hide password in logs
    sanitized_url = DATABASE_URL.replace('//', '//<username>:<password>@')
    print(f"Using DATABASE_URL: {sanitized_url}")

# Provide helpful error if DATABASE_URL is not set
if not DATABASE_URL:
    print("Error: DATABASE_URL environment variable is not set.")
    print("Please set it to your PostgreSQL connection string.")
    print("Example: postgresql://username:password@hostname:port/database?sslmode=require")
    
    # In development, fall back to a default value
    if not is_render:
        print("Using default local database for development.")
        DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/spotify_clone'
    else:
        print("ERROR: DATABASE_URL environment variable must be set for Render deployment")
        print("Please set it in the Render dashboard under Environment Variables")
        sys.exit(1)

# Fix the dialect name - SQLAlchemy requires 'postgresql://' not 'postgres://'
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    print("Fixed DATABASE_URL dialect from 'postgres://' to 'postgresql://'")

# Create engine with proper SSL settings
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def getdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
