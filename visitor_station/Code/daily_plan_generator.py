import os
from datetime import datetime, timedelta

# Define the lesson content for each course and day
lessons = {
    "PLTW-Intro to Engineering": [
        "## Tuesday: Desk Organizer Design Presentation\n\n"
        "- **Objective**: Evaluate and present design solutions (Bloom's Level: Evaluate)\n"
        "- **Warm-up**: Discuss the importance of design iteration. Reflect on personal experiences improving a design.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Review key design principles and prototyping.\n"
        "  - *Hands-on Activity*: Present desk organizer designs and receive peer feedback.\n"
        "- **Activity**: Peer feedback session using a rubric.\n"
        "- **Reflection Question**: What was the most valuable piece of feedback you received today, and how will it influence your design?\n"
        "- **CA CTE Standards**: CTE.MPD.D.D1.1: Understand the design process as a systematic approach to solving engineering problems.",
        
        "## Wednesday: Onshape Multi-part Studios\n\n"
        "- **Objective**: Create and manipulate multi-part assemblies in CAD software (Bloom's Level: Create)\n"
        "- **Warm-up**: Discuss examples of complex assemblies in everyday products.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Introduction to Onshape multi-part studios.\n"
        "  - *Hands-on Activity*: Guided tutorial on creating multi-part assemblies in Onshape.\n"
        "- **Activity**: Design a simple mechanical assembly using Onshape tools.\n"
        "- **Reflection Question**: What challenges did you face while working with multi-part assemblies in Onshape?\n"
        "- **CA CTE Standards**: CTE.MPD.D.D1.3: Use CAD software for designing engineering solutions.",
        
        "## Thursday: Onshape Multi-part Studios (Continued)\n\n"
        "- **Objective**: Enhance CAD skills by developing complex assemblies (Bloom's Level: Apply)\n"
        "- **Warm-up**: Discuss the role of assemblies in product design and manufacturing.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Review key features of Onshape multi-part studios.\n"
        "  - *Hands-on Activity*: Work on a guided project to create a more complex assembly in Onshape.\n"
        "- **Activity**: Build upon previous work by adding components to an assembly project.\n"
        "- **Reflection Question**: How does using multi-part studios improve your efficiency in designing complex assemblies?\n"
        "- **CA CTE Standards**: CTE.MPD.D.D1.3: Use CAD software for designing engineering solutions.",
        
        "## Friday: Onshape Multi-part Studios (Finalization)\n\n"
        "- **Objective**: Finalize and present completed CAD projects (Bloom's Level: Evaluate)\n"
        "- **Warm-up**: Reflect on the week's learning about multi-part assemblies and discuss any challenges faced.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Recap the week's lessons on Onshape.\n"
        "  - *Hands-on Activity*: Finalize assembly projects and prepare for presentation.\n"
        "- **Activity**: Complete and present final assembly projects, highlighting key features and design choices made during the process.\n"
        "- **Reflection Question**: What was your biggest takeaway from using Onshape this week?\n"
        "- **CA CTE Standards**: CTE.MPD.D.D1.3: Use CAD software for designing engineering solutions."
    ],
    
    "PLTW-Principles of Engineering": [
        "## Tuesday: Pulley IMA and AMA Reflection\n\n"
        "- **Objective**: Analyze mechanical systems using IMA and AMA calculations (Bloom's Level: Analyze)\n"
        "- **Warm-up**: Quick review quiz on IMA and AMA concepts.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Explain the differences between IMA and AMA.\n"
        "  - *Hands-on Activity*: Calculate IMA and AMA for different pulley setups using provided materials.\n"
        "- **Activity**: Lab activity measuring forces in a pulley system to calculate IMA and AMA.\n"
        "- **Reflection Question**: How do discrepancies between IMA and AMA affect the efficiency of a pulley system?\n"
        "- **CA CTE Standards**: CTE.MPD.D.D1.2: Apply mechanical advantage concepts in engineering systems.",
        
        "## Wednesday: Compound Machines\n\n"
        "- **Objective**: Identify simple machines within compound machines (Bloom's Level: Analyze)\n"
        "- **Warm-up**: Brainstorm examples of compound machines found in everyday life.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Explain the concept of compound machines and their applications.\n"
        "  - *Hands-on Activity*: Identify and analyze compound machines using provided kits.\n"
        "- **Activity**: Group activity: Disassemble a compound machine model and identify the simple machines within it.\n"
        "- **Reflection Question**: What advantages do compound machines offer over simple machines?\n"
        "- **CA CTE Standards**: CTE.MPD.D.D1.2: Apply mechanical advantage concepts in engineering systems.",
        
        "## Thursday & Friday: Simple Machines, Part Two\n\n"
        "- **Objective**: Design devices using simple machines to achieve specific tasks (Bloom's Level: Create)\n"
        "- **Warm-up** (Thursday): Review key concepts from previous lessons on simple machines.\n"
        "- **Instruction**:\n"
        "  - *Lecture* (Thursday): Discuss advanced applications of simple machines.\n"
        "  - *Hands-on Activity* (Thursday): Experiment with different configurations of simple machines to achieve specific tasks.\n"
        "- **Activity**: Group challenge: Design a device using simple machines that can lift a specified weight with minimal effort.\n"
        "- **Reflection Question** (Thursday): How did changing configurations affect the performance of your simple machine device?\n"
        "- **CA CTE Standards** (Thursday): CTE.MPD.D.D1.2: Apply mechanical advantage concepts in engineering systems."
    ],
    
    "PLTW-Design & Development": [
        "## Tuesday: Electronics Unit Exam\n\n"
        "- **Objective**: Demonstrate understanding of electronic components through assessment (Bloom's Level: Understand)\n"
        "- **Warm-up**: Review key concepts from the electronics unit with a group discussion.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Recap major topics covered in the electronics unit.\n"
        "  - *Hands-on Activity*: Exam preparation through practice questions.\n"
        "- **Activity**: Electronics Unit Exam: Students complete the exam individually.\n"
        "- **Reflection Question**: Which topic in this unit did you find most challenging, and why?\n"
        "- **CA CTE Standards**: CTE.EC.A.A1.1: Understand electronic systems and their applications in engineering contexts.",
        
        "## Wednesday: Alternative Energy Car - Solar Panels\n\n"
        "- **Objective**: Apply knowledge of solar panels as an alternative energy source for vehicles (Bloom's Level: Apply)\n"
        "- **Warm-up**: Discuss the benefits and limitations of solar energy in transportation.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Introduction to solar panel technology and its application in vehicles.\n"
        "  - *Hands-on Activity*: Experiment with solar panels to power small car models.\n"
        "- **Activity**: Lab activity: Build a simple solar-powered car using provided kits and test its performance under different light conditions.\n"
        "- **Reflection Question**: What factors affect the efficiency of solar panels in powering vehicles?\n"
        "- **CA CTE Standards**: CTE.EC.A.A1.1: Understand renewable energy systems and their applications in engineering contexts.",
        
        "## Thursday: Alternative Energy Car - Fuel Cells\n\n"
        "- **Objective**: Analyze the use of fuel cells as an alternative energy source for vehicles (Bloom's Level: Analyze)\n"
        "- **Warm-up**: Discuss how fuel cells work and their potential benefits over traditional combustion engines.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Overview of fuel cell technology used in vehicles.\n"
        "  - *Hands-on Activity*: Experiment with fuel cell-powered car models, comparing performance with solar-powered models from previous lessons.\n"
        "- **Activity**: Lab activity: Test different types of fuel cells to determine which provides the best performance for car models under various conditions.\n"
        "- **Reflection Question**: What are the trade-offs between using fuel cells versus other alternative energy sources like solar panels or batteries?\n"
        "- **CA CTE Standards**: CTE.EC.A.A1.1: Understand renewable energy systems and their applications in engineering contexts.",
        
        "## Friday: Alternative Energy Car - Batteries\n\n"
        "- **Objective**: Evaluate the effectiveness of batteries as an alternative energy source for vehicles (Bloom's Level: Evaluate)\n"
        "- **Warm-up**: Discuss the role of batteries in modern electric vehicles and their environmental impact.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Overview of battery technology used in vehicles.\n"
        "  - *Hands-on Activity*: Experiment with battery-powered car models, comparing performance with other energy sources from previous lessons.\n"
        "- **Activity**: Lab activity: Test different types of batteries to determine which provides the best performance for car models under various conditions.\n"
        "- **Reflection Question**: What are the trade-offs between using batteries versus other alternative energy sources like solar panels or fuel cells?\n"
        "- **CA CTE Standards**: CTE.EC.A.A1.1: Understand renewable energy systems and their applications in engineering contexts."
    ],
    
    "PLTW-Computer Integrated Manufacturing": [
        "## Tuesday: Manufacturing Research Presentation\n\n"
        "- **Objective**: Evaluate and present research findings on manufacturing processes (Bloom's Level: Evaluate)\n"
        "- **Warm-up**: Discuss recent advancements in manufacturing technology as a class.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Overview of key manufacturing processes.\n"
        "  - *Hands-on Activity*: Student presentations on manufacturing research projects.\n"
        "- **Activity**: Peer review: Students provide feedback on each other's presentations focusing on clarity and content depth.\n"
        "- **Reflection Question**: What was one new thing you learned from a peer's presentation today?\n"
        "- **CA CTE Standards**: CTE.MPD.C.C3.1: Understand manufacturing processes including casting, forming, joining, and additive manufacturing.",
        
        "## Wednesday: Flowcharts\n\n"
        "- **Objective**: Create flowcharts to visualize and organize manufacturing processes (Bloom's Level: Create)\n"
        "- **Warm-up**: Discuss how flowcharts can simplify complex processes in manufacturing.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Introduction to flowchart symbols and their uses.\n"
        "  - *Hands-on Activity*: Create a flowchart for a simple manufacturing process using software tools.\n"
        "- **Activity**: Individual task: Design a flowchart for assembling a product, detailing each step of the process.\n"
        "- **Reflection Question**: How can flowcharts improve communication and efficiency in manufacturing?\n"
        "- **CA CTE Standards**: CTE.MPD.C.C3.1: Understand manufacturing processes including planning and control systems.",
        
        "## Thursday & Friday: Robotic Inputs and Outputs\n\n"
        "- **Thursday Objective**: Apply programming skills to control robotic inputs/outputs (Bloom's Level: Apply)\n"
        "- **Warm-up (Thursday)**: Discuss how robotics is transforming modern manufacturing processes.\n"
        "- **Instruction (Thursday)**:\n"
        "  - *Lecture*: Overview of robotic inputs/outputs and basic programming concepts.\n"
        "  - *Hands-on Activity*: Program a simple robotic task using provided software tools.\n"
        "- **Activity (Thursday)**: Individual task: Write a program that controls robotic inputs/outputs to perform a specific task.\n"
        "- **Reflection Question (Thursday)**: What challenges did you encounter while programming robotic tasks, and how did you overcome them?\n"
        
        "- **Friday Objective**: Enhance robotic programming to improve efficiency (Bloom's Level: Analyze)\n"
        "- **Warm-up (Friday)**: Reflect on previous day's programming challenges and successes.\n"
        "- **Instruction (Friday)**:\n"
        "  - *Lecture*: Advanced programming techniques for robotic inputs/outputs.\n"
        "  - *Hands-on Activity*: Enhance the previous day's program with additional features or complexity.\n"
        "- **Activity (Friday)**: Continue developing robotic programs, focusing on improving efficiency and functionality.\n"
        "- **Reflection Question (Friday)**: How can advanced programming techniques improve the functionality of robotic systems in manufacturing?\n"

        "- **CA CTE Standards**: CTE.MPD.C.C3.1: Understand manufacturing processes including automation technologies."
    ]
}

# Define the start date
start_date = datetime(2024, 10, 7)

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