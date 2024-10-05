## Instructions for Generating Lesson Plans and Python Dictionary

### Use the attached file to generate a lesson plan for each day of the week.

1. **Upload the Schedule:**
   - Begin by uploading the weekly schedule file (e.g., "Weekly-Outline-Week-of-10_7.pdf") to Perplexity. <!---change the date-->

2. **Extract Course Information:**
   - Identify the courses and their respective activities for each day from the uploaded schedule.
   - Ensure that all courses are accounted for: PLTW-Intro to Engineering, PLTW-Principles of Engineering, PLTW-Design & Development, and PLTW-Computer Integrated Manufacturing.

3. **Generate Lesson Plans:**
   - For each course and day listed in the schedule, create a detailed lesson plan including:
     - **Objective:** Clearly define what students should achieve by the end of the lesson, using Bloom's Taxonomy levels (e.g., Understand, Apply, Analyze, Evaluate, Create).
     - **Warm-up:** Design an engaging activity or discussion to introduce the day's topic.
     - **Instruction:** Outline the lecture and hands-on activities planned for the lesson.
     - **Activity:** Describe any additional tasks or projects students will complete.
     - **Reflection Question:** Pose a question that encourages students to reflect on what they learned.
     - **CA CTE Standards:** List relevant California CTE Engineering standards addressed in the lesson.

4. **Create Python Dictionary:**
   - Convert each lesson plan into a structured Python dictionary format. Ensure all elements are included consistently across all courses.
   - Use clear and concise language to describe each part of the lesson plan.

5. **Verify Accuracy:**
   - Double-check that all lesson plans are correctly formatted and that no details are missing.
   - Ensure that learning objectives align with Bloom's Taxonomy levels and that CA CTE Standards are accurately referenced.

6. **Example Python Dictionary Format:**

```python
lessons = {
    "PLTW-Intro to Engineering": [
        "## Tuesday: Desk Organizer Design Presentation\n\n"
        "- **Objective**: Evaluate and present design solutions (Bloom's Level: Evaluate)\n"
        "- **Warm-up**: Discuss the importance of design iteration.\n"
        "- **Instruction**:\n"
        "  - *Lecture*: Review key design principles.\n"
        "  - *Hands-on Activity*: Present desk organizer designs.\n"
        "- **Reflection Question**: What was the most valuable feedback you received?\n"
        "- **CA CTE Standards**: CTE.MPD.D.D1.1",
        
        # Add more days following this format...
    ],
    # Repeat for other courses...
}
```

7. **Prevent Errors:**
   - Use consistent formatting for each lesson plan entry in the dictionary.
   - Include comments or notes within your code to clarify any complex sections or logic.
   - Consider using a checklist to ensure all elements are included for each lesson plan.
