# a piece of code to show how to use pydantic
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, ValidationError

# 1. Define your Schema (The Contract)
class Employee(BaseModel):
    id: int
    name: str
    role: str
    skills: List[str] = Field(default_factory=list)

class Company(BaseModel):
    company_name: str
    is_active: bool
    founding_year: int
    employees: List[Employee]
    # Optional field with a default
    website: Optional[str] = "https://example.com"

# 2. Production Handling Logic
def process_company_data(json_file_path: str):
    try:
        with open(json_file_path, 'r') as file:
            # We use model_validate_json to parse AND validate in one step
            raw_content = file.read()
            company = Company.model_validate_json(raw_content)

        # 3. Accessing Data
        print(f"Processing: {company.company_name}")
        
        for emp in company.employees:
            print(f"- {emp.name} ({emp.role})")
            
    except ValidationError as e:
        # In production, log this to a monitoring tool
        print(f"Schema Validation Error: {e.json()}")
    except FileNotFoundError:
        print("Error: JSON file not found.")

# Usage
process_company_data('company_data.json')