import os
from datetime import datetime, timedelta

# Define the lesson content for each course and day
lessons = {
    "PLTW-Intro to Engineering": [
        {
            "day": "Monday",
            "title": "Debrief Catapult Lesson",
            "objective": "Students will analyze and reflect on their catapult designs to identify areas for improvement.",
            "warm_up": "Quick write-up: 'What was the most challenging part of building your catapult?'",
            "instruction": {
                "lecture": "Review key principles of projectile motion and how they applied to the catapult project.",
                "hands_on_activity": "Group discussion on what worked well and what didn’t. Each group presents their findings."
            },
            "reflection_question": "What changes would you make to your design if you were to build the catapult again?",
            "standards_addressed": ["CTE.ECDFS.A.2.1", "CTE.ECDFS.A.3.1"]
        },
        {
            "day": "Tuesday",
            "title": "Redesign Lesson - Design for Acclimatization",
            "objective": "Students will redesign their catapults with a focus on improving performance based on feedback.",
            "warm_up": "Brainstorm session: 'List three ways you could improve your design.'",
            "instruction": {
                "lecture": "Introduction to iterative design processes and the importance of acclimatization in engineering.",
                "hands_on_activity": "Groups work on redesigning their catapults, focusing on improving accuracy and distance."
            },
            "reflection_question": "How did your redesign address the issues identified in your original design?",
            "standards_addressed": ["CTE.ECDFS.A.4.2", "CTE.ECDFS.A.6.1"]
        },
        {
            "day": "Wednesday",
            "title": "(Continued) Redesign Lesson - Design for Acclimatization",
            "objective": "(Same as Tuesday)",
            "warm_up": "(Same as Tuesday)",
            "instruction": "(Same as Tuesday)",
            "reflection_question": "(Same as Tuesday)",
            "standards_addressed": ["CTE.ECDFS.A.4.2", "CTE.ECDFS.A.6.1"]
        },
        {
            "day": "Thursday",
            "title": "PLTW Activity 1.1.3 Concept Sketching",
            "objective": "Students will learn how to create detailed concept sketches for engineering designs.",
            "warm_up": "'Sketch a simple object from memory.'",
            'instruction': {
                'lecture': 10,
                'hands_on_activity': 35
             },
             'reflection_question': "'How does creating a concept sketch help in the design process?'",
             'standards_addressed': ["CTE.ECDFS.A.3.3", 	"CTE.ECDFS.A.5.1"]
        },
        {
            'day': 'Friday',
            'title': 'PLTW Activity 1.1.3 Concept Sketching (Continued)',
            'objective': 'Continue practicing concept sketching techniques.',
            'warm_up': "'What challenges did you face while sketching yesterday?'",
            'instruction': {
                'lecture': 10,
                'hands_on_activity': 35
             },
             'reflection_question': "'How can concept sketches be used to communicate complex ideas?'",
             'standards_addressed': ["CTE.ECDFS.A.3.3", 	"CTE.ECDFS.A.5.1"]
        }
    ],

    # PLTW-Principles of Engineering
    # --------------------------------
    'PLTW-Principles of Engineering': [
        {
           'day': 'Monday',
           'title': 'Continue work on Tug of War Car',
           'objective': 'Students will continue building and refining their Tug of War cars, applying mechanical principles.',
           'warm_up': "'What mechanical advantage are you trying to achieve with your car?'",
           'instruction': {
               'lecture': 10,
               'hands_on_activity': 35
           },
           'reflection_question': "'What changes did you make today that improved your car’s performance?'",
           'standards_addressed': ['CTE.ECDFS.B.2.2', 'CTE.ECDFS.B.4.1']
       },
       {
           'day': 'Tuesday',
           'title': '(Continued) Continue work on Tug of War Car',
           'objective': '(Same as Monday)',
           'warm_up': '(Same as Monday)',
           'instruction': '(Same as Monday)',
           'reflection_question': '(Same as Monday)',
           'standards_addressed': ['CTE.ECDFS.B.2.2', 'CTE.ECDFS.B.4.1']
       },
       {
           'day': 'Wednesday',
           'title': '(Continued) Continue work on Tug of War Car',
           'objective': '(Same as Monday)',
           'warm_up': '(Same as Monday)',
           'instruction': '(Same as Monday)',
           'reflection_question': '(Same as Monday)',
           'standards_addressed': ['CTE.ECDFS.B.2.2', 'CTE.ECDFS.B.4.1']
       },
       {
          'day': 'Thursday',
          'title': 	'Tug of War Competition',
          'objective':'Students will test their Tug of War cars in a competition, applying concepts of force and motion.',
          'warm_up': "'Predict the outcome of your car’s performance in the competition based on its design features.'",
          'instruction': {
              'lecture': 5,
              'hands_on_activity': 50
          },
          'reflection_question': "'How did your car perform compared to your expectations? What would you change if you had more time?'",
          'standards_addressed': ['CTE.ECDFS.B.6.2',	'CTE.ECDFS.B.7.1']
      },
      {
         'day':	'Friday',
         'title':	'Tug of War Competition (Continued)',
         'objective':	'(Same as Thursday)',
         'warm_up':	'(Same as Thursday)',
         'instruction':	'(Same as Thursday)',
         'reflection_question':	'(Same as Thursday)',
         'standards_addressed': ['CTE.ECDFS.B.6.2',	'CTE.ECDFS.B.7.1']
     }
    ],

    # PLTW-Design & Development A
    # ---------------------------------
    'PLTW-Design & Development A': [
      {
         'day':	'Monday',
         'title':	'Nested Loops Review',
         'objective':	'Students will review nested loops in programming and understand how they can be applied in automation systems.',
         'warm_up':	"'Write out a pseudocode example for a nested loop that counts from 1 to 5 twice.'",
         'instruction':	{
             'lecture': 10,
             'hands_on_activity': 35
         },
         'reflection_question': "'How can nested loops simplify repetitive tasks in programming?'",
         'standards_addressed':['CTE.IT.C.C7.3']
     },
     {
        'day':'Tuesday',
        'title':'Arduino Sensors – Printing Values',
        'objective':'Students will learn how to collect data from various sensors using Arduino and display this data using serial communication.',
        'warm_up':"'Predict what values you might expect from a temperature sensor connected to an Arduino board.'",
        'instruction':{
          'lecture':10,
          'hands_on_activity':35
      },
      'reflection_question':"'How can sensor data be used in real-world applications such as home automation or environmental monitoring?'",
      'standards_addressed':['CTE.IT.C.C7.2','CTE.IT.C.C7.3']
     },

     # Wednesday, Thursday, Friday continue similarly...
    ],

    # PLTW-Computer Integrated Manufacturing (CIM)
    # --------------------------------------------
    'PLTW-CIM_A':[
      {
        'day':'Monday',
        'title':'Robotic Inputs and Outputs',
        'objective':'Understand the basics of robotic inputs and outputs in manufacturing.',
        'warm_up':"'Discuss the role of robotics in modern manufacturing processes.'",
        'instruction':{
          'lecture':"Introduction to robotic inputs and outputs.",
          'hands_on_activity':"Explore basic programming for robotic systems."
      },
      'reflection_question':"'What was one new thing you learned about robotics today?'",
      'standards_addressed':['CTE.MPD.C.C3']
     },
     {
        'day':'Tuesday',
        'title':'Robotic Inputs and Outputs (Continued)',
        'objective':'Apply knowledge of robotic inputs and outputs through practical applications.',
        'warm_up':"'Review key concepts from previous day's lesson on robotics.'",
        'instruction':{
          'lecture':"Practical applications of robotic inputs and outputs.",
          'hands_on_activity':"Program a more complex task using robotic inputs and outputs."
      },
      'reflection_question':"'What improvements did you make to your robotic program today?'",
      'standards_addressed':['CTE.MPD.C.C3']
     },
     {
       'day':'Wednesday',
       'title':'Optical and Distance Sensors',
       'objective':'Explore optical and distance sensors used in manufacturing automation.',
       'warm_up':"'Discuss the role of sensors in improving manufacturing precision.'",
       'instruction':{
         'lecture':"Overview of optical and distance sensors.",
         'hands_on_activity':"Explore sensor integration into manufacturing systems."
       },
       'reflection_question':"'What advantages do sensors provide in automated manufacturing processes?'",
       'standards_addressed':['CTE.MPD.C.C3']
     },
     {
       'day':'Thursday',
       'title':'Optical and Distance Sensors (Continued)',
       'objective':'Implement optical and distance sensors in practical manufacturing applications.',
       'warm_up':"'Review previous day's learning on sensor technology.'",
       'instruction':{
         'lecture':10,
         'hands_on_activity':35
       },
       'reflection_question':"'What challenges did you encounter when integrating sensors into your project?'",
       'standards_addressed':['CTE.MPD.C.C3']
     },
     {
       'day':'Friday',
       'title':'Advanced Sensor Applications',
       'objective':'Evaluate the effectiveness of sensor integration in manufacturing systems.',
       'warm_up':"'Discuss real-world examples of sensor applications in manufacturing.'",
       'instruction':{
         'lecture':"Case studies on advanced sensor applications in modern manufacturing systems.",
         'hands_on_activity':"Analyze case studies to identify successful sensor integration strategies."
       },
       'reflection_question':"'How can sensor technology be further developed to enhance manufacturing efficiency?'",
       'standards_addressed':['CTE.MPD.C.C3']
     }
   ]
}

# Define the start date
start_date = datetime(2024, 11, 18)

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