class BudgetCategory:
    # Constructor to initialize category name and allocated budget
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name  # Private attribute
        self.__allocated_budget = allocated_budget  # Private attribute
        self.__expenses = 0  # Private attribute to track expenses

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name (optional, if needed to update the name)
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation (should be positive)
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
        else:
            print("Allocated budget must be a positive number.")

    # Method to add expenses to the category with validation
    def add_expense(self, amount):
        if amount > 0:
            self.__expenses += amount
        else:
            print("Expense amount must be positive.")

    # Method to display the budget category summary
    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expenses
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Expenses: ${self.__expenses}")
        print(f"Remaining Budget: ${remaining_budget}")

