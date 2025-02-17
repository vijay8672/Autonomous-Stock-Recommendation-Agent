import os
from pathlib import Path

# Define the list of directories and files for the project structure
project_structure = [
    f"src/agents/agents.py",
    f"src/agents/__init__.py",
    f"src/models/model.py",
    f"src/models/__init__.py", 
    f"src/utils/util.py",
    f"src/utils/__init__.py",
    f"src/logging_setup/logger.py",
    f"src/logging_setup/__init__.py",
    f"src/exceptions/exception.py",
    f"src/exceptions/__init__.py",
    f"Dockerfile",
    f"config/config.yml",
    f"requirements.txt",
    f"notebooks/exploration.ipynb",
    f"notebooks/data_visualization.ipynb",
    f"setup.py",
    f"README.md",
    f".gitignore",
    f".env",
    f"tests/test_agents.py",   # Test file for agent logic
    f"tests/test_models.py",   # Test file for model logic
    f"tests/test_utils.py",    # Test file for utilities
        
]


def create_project_structure():
    for file_path in project_structure:
        full_path=Path(file_path)
        
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        if not full_path.exists():
            full_path.touch()
            
if __name__=="__main__":
    create_project_structure()
    
    