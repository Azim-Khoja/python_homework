# Homework 1.  ToDo List Application

# 1. Define Task Class:
# Create a Task class with attributes such as task title, description, due date, and status.

class Task:
    def __init__(self, title, description, due_date, status="INCOMPLETE"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status


# 2. Define ToDoList Class:
# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.

class Todolist(Task):
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        print(f"'{task.title}' added saccessfully.")

    def show_all_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
        else:
            print("All tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task.title} - {task.status} (Due {task.due_date})")

    def mark_task_complete(self, index):
        try:
            task = self.tasks[index - 1]
            if task.status.lower() == 'complete':
                print(f"'{task.title}' is already complete.")
            else:
                task.status = "COMPLETE"
                print(f"Task '{task.title}' marked as complete.")
        except IndexError:
            print("Invalid task number")

    def show_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status.lower() != "complete"]
        if not incomplete:
            print("All tasks are complete.")
        else:
            print("Incomplete Tasks:")
            for i, task in enumerate(incomplete, 1):
                print(f"{i}. {task.title} - {task.status} (Due {task.due_date})")


# 3. Create Main Program:
# Develop a simple CLI to interact with the ToDoList.
# Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.

def main():
    todo = Todolist()

    while True:
        print("\n=== ToDo List Menu ===")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Show incomplete tasks")
        print("4. Mark task as complete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            todo.add_task(title, description, due_date)

        elif choice == "2":
            todo.show_all_tasks()

        elif choice == "3":
            todo.show_incomplete_tasks()

        elif choice == "4":
            todo.show_all_tasks()
            try:
                index = int(input("Enter task number to mark as complete: "))
                todo.mark_task_complete(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# 4. Test the Application:
# Create instances of tasks and test the functionality of your ToDoList.

if __name__ == "__main__":
    main()


# Homework 2. Simple Blog System


# 1. Define Post Class:
# Create a Post class with attributes like title, content, and author.

# 2. Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.

# 3. Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.

# 4. Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.

# 5. Test the Application:
# Create instances of posts and test the functionality of your Blog system.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)
        print(f"Post '{title}' added successfully.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            print("\nAll Blog Posts:")
            for i, post in enumerate(self.posts, 1):
                print(f"{i}. {post.title} by {post.author}")

    def show_posts_by_author(self, author_name):
        filtered = [p for p in self.posts if p.author.lower() == author_name.lower()]
        if not filtered:
            print(f"No posts found by '{author_name}'.")
        else:
            print(f"\nPosts by {author_name}:")
            for i, post in enumerate(filtered, 1):
                print(f"{i}. {post.title}")

    def delete_post(self, index):
        try:
            post = self.posts.pop(index - 1)
            print(f"Post '{post.title}' deleted successfully.")
        except IndexError:
            print("Invalid post number.")

    def edit_post(self, index, new_title, new_content):
        try:
            post = self.posts[index - 1]
            post.title = new_title
            post.content = new_content
            print(f"Post updated successfully.")
        except IndexError:
            print("Invalid post number.")

    def show_latest_posts(self, count=3):
        if not self.posts:
            print("No posts available.")
        else:
            latest = self.posts[-count:]  # last 'count' posts
            print(f"\nLatest {len(latest)} Posts:")
            for i, post in enumerate(reversed(latest), 1):
                print(f"{i}. {post.title} by {post.author}")


def main():
    blog = Blog()

    while True:
        print("\n--- Simple Blog System ---")
        print("1. Add new post")
        print("2. List all posts")
        print("3. Show posts by author")
        print("4. Edit a post")
        print("5. Delete a post")
        print("6. Show latest posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            title = input("Enter post title: ").strip()
            content = input("Enter post content: ").strip()
            author = input("Enter author name: ").strip()
            blog.add_post(title, content, author)

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ").strip()
            blog.show_posts_by_author(author)

        elif choice == "4":
            blog.list_all_posts()
            try:
                index = int(input("Enter post number to edit: "))
                new_title = input("Enter new title: ").strip()
                new_content = input("Enter new content: ").strip()
                blog.edit_post(index, new_title, new_content)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            blog.list_all_posts()
            try:
                index = int(input("Enter post number to delete: "))
                blog.delete_post(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":
            blog.show_latest_posts()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


blog = Blog()
blog.add_post("First Post", "Hello World", "Azimjon")
blog.add_post("Second Post", "Another blog entry", "Azimjon")
blog.add_post("Third Post", "Learning Python", "Mark")

blog.list_all_posts()

# Postni tahrirlash
blog.edit_post(2, "Updated Second Post", "Updated content")

# Postni o‘chirish
blog.delete_post(1)

# Eng so‘nggi 2 ta postni ko‘rsatish
blog.show_latest_posts(2)


if __name__ == "__main__":
    main()




