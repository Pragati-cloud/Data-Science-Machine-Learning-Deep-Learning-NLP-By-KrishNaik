from pydantic import BaseModel,Field, AnyUrl, EmailStr, field_validator, model_validator, computed_field
from typing import Annotated, Optional, List, Dict

class Patient(BaseModel):
  name:Annotated[str,Field(max_length=50, title ="Patient Name", description="Name of the patient", example="Shubha")]
  age:int = Field(gt=0, lt=70, description="Age of the patient", example=25)
  weight:float
  height:float
  allergies: List[str]

  @field_validator('weight')
  @classmethod
  def weight_positive(cls,value):
    if value<=0:
      raise ValueError('Weight must be a positive number')
    return value

  @computed_field
  @property
  def bmi(self)->float:
    return round(self.weight/(self.height**2),2)
  
  @model_validator(mode='after')  ## after pydantic validation
  def validation_allergies(cls, model):
    if len(model.allergies)==0:
      raise ValueError('Allergy list cannot be empty')
    return model


def insert_patient_details(patient: Patient):
  print(patient.name)
  print(patient.age)
  print(patient.weight)
  print(patient.height)
  print('BMI', patient.bmi)
  print(patient.allergies)

patient_info ={'name':'Pragati','age':20,'weight':48,'height':1.82,'allergies':['Dust','Pollen']}

patient1= Patient(**patient_info)
insert_patient_details(patient1)
