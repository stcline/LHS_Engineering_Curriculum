import os
from datetime import datetime, timedelta

# Define the lesson content for each course and day
lessons = {
    "PLTW-Intro to Engineering": [
        "## Monday: Onshape - Making the Step\n\n"
        "- **Objective**: Apply CAD skills to create simple mechanical parts (Bloom's Level: Apply)\n"
        "- **Warm-up**: Discuss how CAD software is used in engineering design.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Introduction to making steps in Onshape.\n"
        "  - *Hands-on Activity*: Practice creating steps in Onshape.\n"
        "- **Activity**: Create a simple mechanical part using Onshape's step tool.\n"
        "- **Reflection Question**: How does using CAD software improve design accuracy?\n"
        "- **Standards Addressed**: Engineering Design Pathway Standards: D1.0, D2.0",
        
        "## Tuesday: Onshape - Making the Step\n\n"
        "- **Objective**: Enhance CAD skills by practicing creating steps in Onshape (Bloom's Level: Apply)\n"
        "- **Warm-up**: Review key features of Onshape related to step creation.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Advanced techniques for creating steps.\n"
        "  - *Hands-on Activity*: Practice creating complex step designs in Onshape.\n"
        "- **Activity**: Refine a previous design by incorporating advanced step features.\n"
        "- **Reflection Question**: What challenges did you face while enhancing your step designs?\n"
        "- **Standards Addressed**: Engineering Design Pathway Standards: D1.0, D2.0",
        
        "## Wednesday: Alternative Energy Car - Solar Panels\n\n"
        "- **Objective**: Explore solar panels as an alternative energy source for vehicles (Bloom's Level: Apply)\n"
        "- **Warm-up**: Discuss the benefits and limitations of solar energy in transportation.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Introduction to solar panel technology and its application in vehicles.\n"
        "  - *Hands-on Activity*: Experiment with solar panels to power small car models.\n"
        "- **Activity**: Build a simple solar-powered car using provided kits and test its performance under different light conditions.\n"
        "- **Reflection Question**: What factors affect the efficiency of solar panels in powering vehicles?\n"
        "- **Standards Addressed**: CTE.EC.A.A1.1",
        
        "## Thursday: Alternative Energy Car - Fuel Cells\n\n"
        "- **Objective**: Analyze the use of fuel cells as an alternative energy source for vehicles (Bloom's Level: Analyze)\n"
        "- **Warm-up**: Discuss how fuel cells work and their potential benefits over traditional combustion engines.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Overview of fuel cell technology used in vehicles.\n"
        "  - *Hands-on Activity*: Experiment with fuel cell-powered car models, comparing performance with solar-powered models from previous lessons.\n"
        "- **Activity**: Test different types of fuel cells to determine which provides the best performance for car models under various conditions.\n"
        "- **Reflection Question**: What are the trade-offs between using fuel cells versus other alternative energy sources like solar panels or batteries?\n"
        "- **Standards Addressed**: CTE.EC.A.A1.1",
        
        "## Friday: Alternative Energy Car - Batteries\n\n"
        "- **Objective**: Evaluate the effectiveness of batteries as an alternative energy source for vehicles (Bloom's Level: Evaluate)\n"
        "- **Warm-up**: Discuss the role of batteries in modern electric vehicles and their environmental impact.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Overview of battery technology used in vehicles.\n"
        "  - *Hands-on Activity*: Experiment with battery-powered car models, comparing performance with other energy sources from previous lessons.\n"
        "- **Activity**: Test different types of batteries to determine which provides the best performance for car models under various conditions.\n"
        "- **Reflection Question**: What are the trade-offs between using batteries versus other alternative energy sources like solar panels or fuel cells?\n"
        "- **Standards Addressed**: CTE.EC.A.A1.1",
    ],
    
    "PLTW-Principles of Engineering": [
        "## Monday: Simple Machines, Part Two (Screw)\n\n"
        "- **Objective**: Understand the application of screws as simple machines (Bloom's Level: Understand)\n"
        "- **Warm-up**: Discuss examples of screws used in everyday life.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: The mechanics of screws and their applications.\n"
        "  - *Hands-on Activity*: Experiment with screws to understand their mechanical advantage.\n"
        "- **Activity**: Calculate the mechanical advantage of different screw types.\n"
        "- **Reflection Question**: How do screws differ from other simple machines in terms of efficiency?\n"
        "- **Standards Addressed**: CTE.MPD.D.D1.2: Apply mechanical advantage concepts in engineering systems.",
        
        "## Tuesday: Practice Quiz - Simple Machines\n\n"
        "- **Objective**: Reinforce learning through a practice quiz on simple machines (Bloom's Level: Apply)\n"
        "- **Warm-up**: Quick review quiz on simple machine concepts covered so far.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Review key concepts related to simple machines.\n"
        "  - *Hands-on Activity*: Take a practice quiz on simple machines.\n"
        "- **Activity**: Discuss answers and clarify any misconceptions from the quiz.\n"
        "- **Reflection Question**: Which simple machine concept do you find most difficult, and why?\n"
        "- **Standards Addressed**: CTE.MPD.D.D1.2: Apply mechanical advantage concepts in engineering systems.",
        
        "## Wednesday: VEX V5 Programming Interface\n\n"
        "- **Objective**: Learn about VEX V5 programming interface for robotics (Bloom's Level: Understand)\n"
        "- **Warm-up**: Discuss how programming interfaces simplify robotics control.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Overview of VEX V5 programming interface.\n"
        "  - *Hands-on Activity*: Introduction to basic programming tasks using VEX V5.\n"
        "- **Activity**: Program a basic movement sequence using VEX V5 interface.\n"
        "- **Reflection Question**: What was the most challenging aspect of using the VEX V5 interface?\n"
        "- **Standards Addressed**: CTE.MPD.C.C3.1: Understand manufacturing processes including automation technologies.",
        
        "## Thursday: Optical and Distance Sensors\n\n"
        "- **Objective**: Explore optical and distance sensors used in engineering applications (Bloom's Level: Apply)\n"
        "- **Warm-up**: Discuss how sensors are used to enhance precision in engineering systems.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Overview of optical and distance sensors and their applications.\n"
        "  - *Hands-on Activity*: Experiment with sensors to understand their functionality in different setups.\n"
        "- **Activity**: Implement a sensor-based system to measure distance or detect objects.\n"
        "- **Reflection Question**: How do optical and distance sensors improve the accuracy of engineering systems?\n"
        "- **Standards Addressed**: CTE.MPD.C.C3.1: Understand manufacturing processes including automation technologies.",
        
        "## Friday: Advanced Robotic Programming\n\n"
        "- **Objective**: Implement advanced programming techniques for robotic systems (Bloom's Level: Analyze)\n"
        "- **Warm-up**: Reflect on previous day's challenges with sensor integration.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Advanced programming techniques for integrating sensors with robotic systems.\n"
        "  - *Hands-on Activity*: Enhance robotic programs by incorporating sensor feedback for improved functionality.\n"
        "- **Activity**: Develop a program that uses sensor data to make autonomous decisions in a robotic system.\n"
        "- **Reflection Question**: How can integrating sensors with robotics enhance system performance?\n"
        "- **Standards Addressed**: CTE.MPD.C.C3.1: Understand manufacturing processes including automation technologies."
    ],
    
    "PLTW-Design & Development": [
        "## Monday: Review Unit Exam\n\n"
        "- **Objective**: Prepare students for electronics unit exam through review activities (Bloom's Level: Understand)\n"
        "- **Warm-up**: Review key concepts from the electronics unit with a group discussion.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Recap major topics covered in the electronics unit.\n"
        "  - *Hands-on Activity*: Exam preparation through practice questions.\n"
        "- **Activity**: Review session focusing on circuit analysis and electronic components.\n"
        "- **Reflection Question**: Which topic in this unit did you find most challenging, and why?\n"
        "- **Standards Addressed**: CTE.EC.A.A1.1: Understand electronic systems and their applications in engineering contexts.",
        
        "## Tuesday: Inputs and Outputs\n\n"
        "- **Objective**: Explore inputs and outputs as they relate to alternative energy cars (Bloom's Level: Apply)\n"
        "- **Warm-up**: Discuss the role of inputs and outputs in vehicle design, especially alternative energy cars.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Overview of inputs and outputs in automotive systems.\n"
        "  - *Hands-on Activity*: Analyze input/output systems in alternative energy cars.\n"
        "- **Activity**: Identify key input/output components in a model car setup.\n"
        "- **Reflection Question**: How do inputs and outputs affect the efficiency of alternative energy cars?\n"
        "- **Standards Addressed**: CTE.EC.A.A1.1: Understand renewable energy systems and their applications in engineering contexts.",
        
        "## Wednesday: Optical and Distance Sensors\n\n"
        "- **Objective**: Explore optical and distance sensors as part of automotive technology (Bloom's Level: Apply)\n"
        "- **Warm-up**: Discuss how sensors are used in modern vehicles for safety and efficiency.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Introduction to optical and distance sensors.\n"
        "  - *Hands-on Activity*: Demonstrate sensor functionality with small models.\n"
        "- **Activity**: Test different sensor setups on model cars to understand their impact on navigation.\n"
        "- **Reflection Question**: How do sensors enhance vehicle performance and safety?\n"
        "- **Standards Addressed**: CTE.EC.A.A1.1: Understand renewable energy systems and their applications in engineering contexts.",
        
        "## Thursday: Optical and Distance Sensors (Continued)\n\n"
        "- **Objective**: Implement optical and distance sensors in practical applications (Bloom's Level: Create)\n"
        "- **Warm-up**: Review previous day's learning on sensor technology.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Advanced applications of sensors in automotive systems.\n"
        "  - *Hands-on Activity*: Integrate sensors into a functional model car system.\n"
        "- **Activity**: Develop a project using sensors to automate tasks or improve vehicle functionality.\n"
        "- **Reflection Question**: What challenges did you encounter when integrating sensors into your project?\n"
        "- **Standards Addressed**: CTE.EC.A.A1.1: Understand renewable energy systems and their applications in engineering contexts.",
        
        "## Friday: Advanced Sensor Applications\n\n"
        "- **Objective**: Evaluate the effectiveness of sensor integration in automotive systems (Bloom's Level: Evaluate)\n"
        "- **Warm-up**: Discuss real-world examples of sensor applications in vehicles.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Case studies on advanced sensor applications in modern vehicles.\n"
        "  - *Hands-on Activity*: Analyze case studies to identify successful sensor integration strategies.\n"
        "- **Activity**: Present findings on how sensors can be optimized for better vehicle performance.\n"
        "- **Reflection Question**: How can sensor technology be further developed to enhance automotive safety and efficiency?\n"
        "- **Standards Addressed**: CTE.EC.A.A1.1: Understand renewable energy systems and their applications in engineering contexts."
    ],

    "PLTW-Computer Integrated Manufacturing": [
        "## Monday: Robotic Inputs and Outputs\n\n"
        "- **Objective**: Understand the basics of robotic inputs and outputs in manufacturing (Bloom's Level: Understand)\n"
        "- **Warm-up**: Discuss the role of robotics in modern manufacturing processes.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Introduction to robotic inputs and outputs.\n"
        "  - *Hands-on Activity*: Explore basic programming for robotic systems.\n"
        "- **Activity**: Program a simple task using robotic inputs and outputs.\n"
        "- **Reflection Question**: What was one new thing you learned about robotics today?\n"
        "- **Standards Addressed**: CTE.MPD.C.C3.1: Understand manufacturing processes including automation technologies.",
        
        "## Tuesday: Robotic Inputs and Outputs (Continued)\n\n"
        "- **Objective**: Apply knowledge of robotic inputs and outputs through practical applications (Bloom's Level: Apply)\n"
        "- **Warm-up**: Review key concepts from previous day's lesson on robotics.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Practical applications of robotic inputs and outputs.\n"
        "  - *Hands-on Activity*: Program a more complex task using robotic inputs and outputs.\n"
        "- **Activity**: Refine previous programs to include more sophisticated input/output controls.\n"
        "- **Reflection Question**: What improvements did you make to your robotic program today?\n"
        "- **Standards Addressed**: CTE.MPD.C.C3.1: Understand manufacturing processes including automation technologies.",
        
        "## Wednesday: Optical and Distance Sensors\n\n"
        "- **Objective**: Explore optical and distance sensors used in manufacturing automation (Bloom's Level: Apply)\n"
        "- **Warm-up**: Discuss the role of sensors in improving manufacturing precision.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Overview of optical and distance sensors.\n"
        "  - *Hands-on Activity*: Explore sensor integration into manufacturing systems.\n"
        "- **Activity**: Implement a sensor-based control system for a manufacturing task.\n"
        "- **Reflection Question**: What advantages do sensors provide in automated manufacturing processes?\n"
        "- **Standards Addressed**: CTE.MPD.C.C3.1: Understand manufacturing processes including automation technologies.",

        "## Thursday: Optical and Distance Sensors\n\n"
        "- **Objective**: Implement optical and distance sensors in practical manufacturing applications (Bloom's Level: Create)\n"
        "- **Warm-up**: Review previous day's learning on sensor technology.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Advanced applications of sensors in manufacturing systems.\n"
        "  - *Hands-on Activity*: Integrate sensors into a functional manufacturing system.\n"
        "- **Activity**: Develop a project using sensors to automate tasks or improve system functionality.\n"
        "- **Reflection Question**: What challenges did you encounter when integrating sensors into your project?\n"
        "- **Standards Addressed**: CTE.MPD.C.C3.1: Understand manufacturing processes including automation technologies.",
        
        "## Friday: Advanced Sensor Applications\n\n"
        "- **Objective**: Evaluate the effectiveness of sensor integration in manufacturing systems (Bloom's Level: Evaluate)\n"
        "- **Warm-up**: Discuss real-world examples of sensor applications in manufacturing.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Case studies on advanced sensor applications in modern manufacturing systems.\n"
        "  - *Hands-on Activity*: Analyze case studies to identify successful sensor integration strategies.\n"
        "- **Activity**: Present findings on how sensors can be optimized for better system performance.\n"
        "- **Reflection Question**: How can sensor technology be further developed to enhance manufacturing efficiency?\n"
        "- **Standards Addressed**: CTE.MPD.C.C3.1: Understand manufacturing processes including automation technologies."
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