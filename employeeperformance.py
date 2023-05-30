# Rule base
rules = {
    'rule1': {'Communication': 8, 'Productivity': 9, 'Output': 'Excellent'},
    'rule2': {'Communication': 7, 'Productivity': 9, 'Output': 'Good'},
    'rule3': {'Communication': 6, 'Productivity': 9, 'Output': 'Average'},
    'rule4': {'Communication': 8, 'Productivity': 6, 'Output': 'Good'},
    'rule5': {'Communication': 7, 'Productivity': 6, 'Output': 'Average'},
    'rule6': {'Communication': 6, 'Productivity': 6, 'Output': 'Poor'},
    'rule7': {'Communication': 8, 'Productivity': 3, 'Output': 'Average'},
    'rule8': {'Communication': 7, 'Productivity': 3, 'Output': 'Poor'},
    'rule9': {'Communication': 6, 'Productivity': 3, 'Output': 'Poor'},
}

class Employee:
    def __init__(self, name, productivity, teamwork, communication):
        self.name = name
        self.productivity = productivity
        self.teamwork = teamwork
        self.communication = communication

    def calculate_performance_score(self):
        performance_score = (self.productivity + self.teamwork + self.communication) / 3
        return performance_score

    def evaluate_performance(self):
        for rule, conditions in rules.items():
            if (
                conditions['Communication'] <= self.communication
                and conditions['Productivity'] <= self.productivity
            ):
                return conditions['Output']
        return 'Unknown'

    def display_employee_data(self):
        print("Employee Data:")
        print(f"Name: {self.name}")
        print(f"Productivity: {self.productivity}")
        print(f"Teamwork: {self.teamwork}")
        print(f"Communication: {self.communication}")

# Main program
def main():
    print("Employee Performance Evaluation")
    print("-------------------------------")
    name = input("Enter Employee Name: ")
    productivity = int(input("Enter Productivity rating (3/6/9): "))
    teamwork = int(input("Enter Teamwork rating (0-10): "))
    communication = int(input("Enter Communication rating (7-9: "))

    employee = Employee(name, productivity, teamwork, communication)
    performance_score = employee.calculate_performance_score()
    performance = employee.evaluate_performance()

    employee.display_employee_data()
    print(f"Performance Score: {performance_score}")
    print(f"Performance: {performance}")

# Run the main program
if __name__ == '__main__':
    main()
