def allocate_projects(employees, projects):
    result = []
    project_skills = {project["name"]: project["required_skills"] for project in projects}
    employee_skills = {employee["name"]: set(employee["skills"]) for employee in employees}

    for project in projects:
        project_name = project["name"]
        required_skills = set(project_skills[project_name])

        for employee in employees:
            employee_name = employee["name"]
            if employee["current_project"] is None and required_skills.issubset(employee_skills[employee_name]):
                result.append({"employee": employee_name, "project": project_name})
                employee["current_project"] = project_name
                break

    return result

employees = [
    {"name": "John", "skills": ["Python", "Database"], "current_project": None},
    {"name": "Emma", "skills": ["Java", "Testing"], "current_project": None},
    {"name": "Kelly", "skills": ["Python", "Java"], "current_project": None}
]

projects = [
    {"name": "Project A", "required_skills": ["Python", "Database"]},
    {"name": "Project B", "required_skills": ["Java", "Testing"]},
    {"name": "Project C", "required_skills": ["Python", "Java"]}
]

allocation_result = allocate_projects(employees, projects)
print(allocation_result)
