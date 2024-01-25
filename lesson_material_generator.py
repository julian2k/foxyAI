import os
import json
from config import LESSON_MATERIALS_PATH

def save_lesson_materials(lesson_plan, prompt, class_year):
    """
    Function to save the generated lesson plan as a JSON file
    :param lesson_plan: The generated lesson plan
    :param prompt: The topic of the lesson plan
    :param class_year: The class year to determine the difficulty of the lesson plan
    :return: The path to the saved lesson plan
    """
    # Create the lesson materials directory if it doesn't exist
    if not os.path.exists(LESSON_MATERIALS_PATH):
        os.makedirs(LESSON_MATERIALS_PATH)

    # Create a unique filename for the lesson plan
    filename = f"{prompt.replace(' ', '_').lower()}_class_{class_year}.json"
    filepath = os.path.join(LESSON_MATERIALS_PATH, filename)

    # Save the lesson plan as a JSON file
    with open(filepath, 'w') as f:
        json.dump(lesson_plan, f)

    return filepath

def generate_and_save_lesson_materials(prompt, class_year):
    """
    Function to generate a lesson plan and save it as a JSON file
    :param prompt: The topic of the lesson plan
    :param class_year: The class year to determine the difficulty of the lesson plan
    :return: The path to the saved lesson plan
    """
    # Generate the lesson plan
    lesson_plan = generate_lesson_plan(prompt, class_year)

    # Save the lesson plan
    filepath = save_lesson_materials(lesson_plan, prompt, class_year)

    return filepath