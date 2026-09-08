"""
student.py: an inheritance of a class
"""

__author__ = "Dillon Strickland"

from typing import override

class Student:
    """
    Class to represent a student.
    """
    @override
    def __init__(self, student_id:int, student_name:str, courses:list):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__courses = courses

    @override
    def __str__(self):
        info = f"Student: {self.__student_name ({self.__student_id})}"
        info += f"\nCourses:\n"

    # Getters
    def get_student_id(self) -> int:
        return self.__student_id

    def get_student_name(self) -> str:
        return self.__student_name

    def get_courses(self) -> list:
        return self.__courses

    # Setters
    def set_student_id(self, student_id:int):
        self.__student_id = student_id

    def set_student_name(self, student_name:str):
         self.__student_name = student_name

    def set_courses(self, courses:list):
        self.__courses = courses

# Testing purposes
def main():
    pass

# Run testing method
if __name__ == "__main__":
    main()