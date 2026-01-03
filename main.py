main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal
import schemas

app = FastAPI()

#to create tables
models.Base.metadata.create_all(bind=engine)

#DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message" : "Student DB API running"}

#add student
@app.post("/students")
def add_student(name: str, course: str, db: Session = Depends(get_db)):
    student = models.Student(name=name, course=course)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

#get all students
@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

#get student by ID
@app.get("/students{stud_id}")
def get_stud_by_id(stud_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == stud_id).first()
    if student is None:
        return {"error": "Student not found"}
    return student

#delete student by ID
@app.delete("/students{stud_id}")
def del_stud_by_id(stud_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == stud_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student data not found")
        #return {"error": "Student not found"}
    db.delete(student)
    db.commit()
    return {"message" : f"The student record deleted for id {stud_id}"}

'''
#update POST API
@app.post("/students", response_model=schemas.StudentResponse)
def add_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(name = student.name, course = student.course)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
'''

#update API(PUT)
@app.put("/students{stud_id}")
def update_student(stud_id : int, updated_data: schemas.StudentCreate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == stud_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student data not found")
        #return {"error": "Student not found"}
    student.name = updated_data.name
    student.course = updated_data.course

    db.commit()
    db.refresh(student)
    return {"message": "Data updated successfully", "student": student}

#filter by parameter
from typing import List
@app.get("/students/{course}", response_model=List[schemas.StudentResponse])
def get_details_by_course(course: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.course == course).all()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student under {course} department is not found")
    return student

#User & Password creation
import utils

@app.post("/user", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    #check if username exists
    existing_user = db.query(models.User).filter(models.User.name == user.name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = utils.hash_password(user.password)
    new_user = models.User(name = user.name, email=user.email, password = hashed_password)
   
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
