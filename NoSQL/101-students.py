#!/usr/bin/env python3
"""
Module for handling student data in MongoDB.
This module provides a function to retrieve and sort students by their average score.
"""

from pymongo.collection import Collection
from typing import List, Dict


def top_students(mongo_collection: Collection) -> List[Dict]:
    """
    Retrieve all students from a MongoDB collection and sort them by average score.

    Args:
        mongo_collection: PyMongo collection object containing student data.

    Returns:
        List of dictionaries, each containing student data with an added
        'averageScore' key, sorted by average score in descending order.
    """
    # Retrieve all students from the collection
    students = mongo_collection.find()

    # List to store students with their average scores
    students_with_avg = []

    # Calculate average score for each student
    for student in students:
        # Get the topics list, default to empty list if not present
        topics = student.get('topics', [])
        if topics:
            # Calculate average score from topics
            scores = [topic['score'] for topic in topics]
            average_score = sum(scores) / len(scores)
        else:
            average_score = 0.0

        # Create a new student dictionary with averageScore
        student_with_avg = student.copy()
        student_with_avg['averageScore'] = average_score
        students_with_avg.append(student_with_avg)

    # Sort students by averageScore in descending order
    sorted_students = sorted(students_with_avg, key=lambda x: x['averageScore'], reverse=True)

    return sorted_students


if __name__ == "__main__":
    # This block is for testing purposes and will not execute when imported
    pass
