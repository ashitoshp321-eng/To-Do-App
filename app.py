
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

tasks = []
next_id = 1

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f0f4f8;
            margin: 0;
            padding: 40px 15px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 28px;
            border-radius: 14px;
            box-shadow: 0 5px 20px #0001;
        }
        h1 { color: #183153; text-align: center; }
        .subtitle { text-align: center; color: #64748b; }
        .add-form { display: flex; gap: 8px; margin: 25px 0; }
        input[name="task"] {
            flex: 1;
            min-width: 0;
            padding: 12px;
            border: 1px solid #cbd5e1;
            border-radius: 7px;
        }
        button, .add-button {
            padding: 11px 14px;
            border: 0;
            border-radius: 7px;
            cursor: pointer;
            color: white;
            background: #2563eb;
        }
        ul { list-style: none; padding: 0; }
        li {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 13px 0;
            border-bottom: 1px solid #e2e8f0;
        }
        li span { flex: 1; overflow-wrap: anywhere; }
        .done { text-decoration: line-through; color: #94a3b8; }
        .delete { background: #dc2626; }
        .empty { text-align: center; color: #64748b; padding: 20px; }
        .stats { color: #64748b; font-size: 14px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>My To-Do List</h1>
        <p class="subtitle">Organize your day, one task at a time.</p>

        <form class="add-form" method="POST" action="/add">
            <input name="task" placeholder="Enter a new task..." required>
            <button type="submit">Add Task</button>
        </form>

        <p class="stats">
            Total: {{ tasks|length }} |
            Completed: {{ tasks|selectattr('done')|list|length }}
        </p>

        <ul>
        {% for task in tasks %}
            <li>
                <form method="POST" action="/toggle/{{ task.id }}">
                    <button type="submit">
                        {{ "Undo" if task.done else "Done" }}
                    </button>
                </form>

                <span class="{{ 'done' if task.done else '' }}">
                    {{ task.title }}
                </span>

                <form method="POST" action="/delete/{{ task.id }}">
                    <button class="delete" type="submit">Delete</button>
                </form>
            </li>
        {% else %}
            <li class="empty">No tasks yet. Add your first task!</li>
        {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    global next_id
    title = request.form.get("task", "").strip()

    if title:
        tasks.append({
            "id": next_id,
            "title": title,
            "done": False
        })
        next_id += 1

    return redirect("/")

@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break

    return redirect("/")

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
