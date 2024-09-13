import os
from datetime import datetime, timedelta

# Define the lesson content for each course and day
lessons = {
    "PLTW-Intro to Engineering": [
        "## Monday: CAD Fundamentals - Introduction\n\n- **Warm-up**: Discuss the importance of CAD in modern engineering.\n- **Instruction**:\n  - *Lecture*: Overview of CAD software and its applications.\n  - *Hands-on Activity*: Students create a simple 2D sketch using CAD software.\n- **Reflection Question**: How does CAD improve the design process?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Tuesday: Navigating Onshape\n\n- **Warm-up**: Review key features of Onshape.\n- **Instruction**:\n  - *Lecture*: Introduction to Onshape interface and tools.\n  - *Hands-on Activity*: Students explore Onshape by creating a basic 3D model.\n- **Reflection Question**: What challenges did you face while navigating Onshape?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Wednesday: Navigating a Document\n\n- **Warm-up**: Discuss the importance of document organization in CAD.\n- **Instruction**:\n  - *Lecture*: How to manage and organize documents in Onshape.\n  - *Hands-on Activity*: Students practice organizing a project document.\n- **Reflection Question**: How does document organization affect project efficiency?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Thursday: Navigating a Document (Continued)\n\n- **Warm-up**: Recap previous day's learning.\n- **Instruction**:\n  - *Lecture*: Advanced document management techniques.\n  - *Hands-on Activity*: Students apply advanced techniques to their documents.\n- **Reflection Question**: What new document management skills did you learn today?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Friday: Essential Onshape Tips\n\n- **Warm-up**: Share favorite Onshape tips.\n- **Instruction**:\n  - *Lecture*: Essential tips and tricks for efficient use of Onshape.\n  - *Hands-on Activity*: Students apply tips to improve their CAD projects.\n- **Reflection Question**: Which tip will be most useful to you and why?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0"
    ],
    "PLTW-Principles of Engineering": [
        "## Monday: Simple Machines and IMA\n\n- **Warm-up**: Discuss examples of simple machines in everyday life.\n- **Instruction**:\n  - *Lecture*: Introduction to simple machines and Ideal Mechanical Advantage (IMA).\n  - *Hands-on Activity*: Calculate IMA for different simple machines.\n- **Reflection Question**: How does understanding IMA help in designing machines?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Tuesday: Work and AMA\n\n- **Warm-up**: Define work in a physics context.\n- **Instruction**:\n  - *Lecture*: The relationship between work and Actual Mechanical Advantage (AMA).\n  - *Hands-on Activity*: Experiment with machines to calculate AMA.\n- **Reflection Question**: How does AMA differ from IMA?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Wednesday: Levers\n\n- **Warm-up**: Identify types of levers around you.\n- **Instruction**:\n  - *Lecture*: Types of levers and their mechanical advantages.\n  - *Hands-on Activity*: Build a simple lever and measure its mechanical advantage.\n- **Reflection Question**: What factors affect the efficiency of a lever?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Thursday: Moments\n\n- **Warm-up**: Discuss the concept of torque.\n- **Instruction**:\n  - *Lecture*: Understanding moments and their applications.\n  - *Hands-on Activity*: Calculate moments for different setups.\n- **Reflection Question**: How do moments relate to stability in structures?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Friday: Efficiency\n\n- **Warm-up**: Define efficiency in engineering terms.\n- **Instruction**:\n  - *Lecture*: Factors affecting machine efficiency.\n  - *Hands-on Activity*: Measure and compare the efficiency of different machines.\n- **Reflection Question**: Why is efficiency important in engineering design?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0"
    ],
    "PLTW-Design and Development": [
        "## Monday: Introduction to Electronics - Circuit\n\n- **Warm-up**: Discuss basic components of a circuit.\n- **Instruction**:\n  - *Lecture*: Introduction to electronic circuits and components.\n  - *Hands-on Activity*: Build a simple circuit using a breadboard.\n- **Reflection Question**: What role does each component play in a circuit?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Tuesday: Schematics\n\n- **Warm-up**: Review symbols used in circuit schematics.\n- **Instruction**:\n  - *Lecture*: How to read and draw circuit schematics.\n  - *Hands-on Activity*: Create a schematic for a simple circuit.\n- **Reflection Question**: How do schematics help in circuit design?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Wednesday: Resistance\n\n- **Warm-up**: Discuss the concept of resistance in circuits.\n- **Instruction**:\n  - *Lecture*: Understanding resistance and its effects on circuits.\n  - *Hands-on Activity*: Measure resistance using a multimeter.\n- **Reflection Question**: How does resistance affect current flow in a circuit?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Thursday: Voltage Dividers\n\n- **Warm-up**: Explain the purpose of a voltage divider.\n- **Instruction**:\n  - *Lecture*: How voltage dividers work and their applications.\n  - *Hands-on Activity*: Build and test a voltage divider circuit.\n- **Reflection Question**: How can voltage dividers be used in practical applications?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Friday: Voltage and Current\n\n- **Warm-up**: Differentiate between voltage and current.\n- **Instruction**:\n  - *Lecture*: The relationship between voltage, current, and resistance.\n  - *Hands-on Activity*: Use Ohm’s Law to calculate voltage and current in circuits.\n- **Reflection Question**: How do voltage and current interact in a circuit?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0"
    ],
    "PLTW-Computer Integrated Manufacturing": [
        "## Monday: Origami Balloon & Set up Engineering Notebooks\n\n- **Warm-up**: Discuss the importance of documentation in engineering.\n- **Instruction**:\n  - *Lecture*: Introduction to engineering notebooks and their uses.\n  - *Hands-on Activity*: Create an origami balloon and document the process.\n- **Reflection Question**: Why is it important to keep detailed records in engineering?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Tuesday: History of Manufacturing\n\n- **Warm-up**: Share a historical fact about manufacturing.\n- **Instruction**:\n  - *Lecture*: Overview of the evolution of manufacturing technologies.\n  - *Hands-on Activity*: Research a significant manufacturing milestone.\n- **Reflection Question**: How has manufacturing technology evolved over time?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Wednesday: Manufacturing Enterprise Wheel\n\n- **Warm-up**: Discuss the components of a manufacturing enterprise.\n- **Instruction**:\n  - *Lecture*: Understanding the Manufacturing Enterprise Wheel.\n  - *Hands-on Activity*: Analyze a case study using the Enterprise Wheel.\n- **Reflection Question**: How does the Enterprise Wheel help in understanding manufacturing processes?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Thursday: Manufacturing Research\n\n- **Warm-up**: Identify a current trend in manufacturing.\n- **Instruction**:\n  - *Lecture*: The role of research in advancing manufacturing technologies.\n  - *Hands-on Activity*: Conduct research on a modern manufacturing technology.\n- **Reflection Question**: What impact does research have on manufacturing advancements?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0",
        "## Friday: Manufacturing Research (Continued)\n\n- **Warm-up**: Share findings from previous day's research.\n- **Instruction**:\n  - *Lecture*: Presenting research findings and their implications.\n  - *Hands-on Activity*: Prepare a presentation on the researched topic.\n- **Reflection Question**: How can your research findings be applied in real-world manufacturing?\n- **CA CTE Standards**: Engineering Design Pathway Standards: D1.0, D2.0"
    ]
}

# Define the start date
start_date = datetime(2024, 9, 16)

# Create markdown files for each lesson
for course, lesson_list in lessons.items():
    for i, lesson in enumerate(lesson_list):
        # Calculate the date for each lesson
        lesson_date = start_date + timedelta(days=i)
        # Format the date as MM-DD-YYYY
        formatted_date = lesson_date.strftime("%m-%d-%Y")
        # Create the filename
        filename = f"{course} - {formatted_date}.md"
        # Write the lesson content to the markdown file
        with open(filename, 'w') as file:
            file.write(lesson)

print("Markdown files created successfully.")