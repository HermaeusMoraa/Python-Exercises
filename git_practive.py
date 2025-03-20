employees = [
    {"name": "Alice", "attendance": 20, "completed_projects": 15, "average_score": 8.5},
    {"name": "Bob", "attendance": 18, "completed_projects": 12, "average_score": 7.8},
    {"name": "Charlie", "attendance": 22, "completed_projects": 18, "average_score": 9.0},
    {"name": "David", "attendance": 25, "completed_projects": 20, "average_score": 6.5},
    {"name": "Eve", "attendance": 24, "completed_projects": 22, "average_score": 8.0},
]

# performance_score = (attendance_weight * attendance) + (projects_weight * completed_projects) + (score_weight * average_score)


def calculate_performance(my_list):

    attendance_weight = 0.5
    projects_weight = 0.3
    score_weight = 0.2

    performance_scores = []

    for employee in my_list:
        performance_score = (
                (employee["attendance"] * attendance_weight) +
                (employee["completed_projects"] * projects_weight) +
                (employee["average_score"] * score_weight)
        )

        performance_scores.append({"name": employee["name"], "performance_score": performance_score})


    performance_scores.sort(key=lambda x: x["performance_score"], reverse=True)


    return performance_scores


performance = calculate_performance(employees)
for employee in performance:
    print(f"{employee['name']} - Performance Score: {employee['performance_score']}")





