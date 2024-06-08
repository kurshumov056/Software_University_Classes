class Task:

    def __init__(self, name, due_date):

        self.comments = []
        self.completed = False

        self.name = name
        self.due_date = due_date

    def change_name(self, new_name: str):
        self.new_name = new_name

        if self.new_name != self.name:
            self.name = self.new_name
            return f"Name changed to {self.name}"

        else:
            return "Name cannot be the same."

    def change_due_date(self, new_date: str):
        self.new_date = new_date

        if self.new_date != self.due_date:
            self.due_date = self.new_date
            return f"Due date changed to {self.due_date}"
        else:
            return f"Date cannot be the same"

    def add_comment(self, comment: str):
        self.comment = comment
        self.comments.append(self.comment)
        return f"comment: '{self.comment} added to comments"

    def edit_comment(self, comment_number: int, new_comment: str):

        self.comment_number = comment_number
        self.new_comment = new_comment

        if self.comment_number in range(0, len(self.comments)):
            self.comments[self.comment_number] = self.new_comment
            return f"Edit comment succesful. New comment list: {self.comments}"
        else:
            return "Cannot find comment"

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"







