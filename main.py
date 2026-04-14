from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

expenses = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Expense Tracker</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #f4f6f8;
            text-align: center;
        }

        .container {
            background: white;
            width: 400px;
            margin: 50px auto;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        h1 {
            color: #333;
        }

        input {
            padding: 10px;
            margin: 5px;
            border-radius: 6px;
            border: 1px solid #ccc;
        }

        button {
            padding: 10px 15px;
            border: none;
            border-radius: 6px;
            background: #4CAF50;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #45a049;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        li {
            background: #f9f9f9;
            margin: 8px;
            padding: 10px;
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
        }

        a {
            color: red;
            text-decoration: none;
            font-weight: bold;
        }

        .total {
            font-size: 20px;
            font-weight: bold;
            margin-top: 15px;
        }

    </style>
</head>
<body>

    <div class="container">
        <h1>💸 Expense Tracker</h1>

        <form method="POST">
            <input type="text" name="desc" placeholder="Description" required>
            <input type="number" name="amount" placeholder="Amount" required>
            <button type="submit">Add</button>
        </form>

        <h3>Expenses</h3>
        <ul>
            {% for e in expenses %}
                <li>
                    {{ e[0] }} - ₹{{ e[1] }}
                    <a href="/delete/{{ loop.index0 }}">✖</a>
                </li>
            {% endfor %}
        </ul>

        <div class="total">Total: ₹{{ total }}</div>
    </div>

</body>
</html>
"""
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        desc = request.form.get('desc')
        amount = request.form.get('amount')

        if desc and amount:
            expenses.append((desc, int(amount)))

        return redirect('/')

    total = sum(e[1] for e in expenses)
    return render_template_string(HTML, expenses=expenses, total=total)


@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)
    return redirect('/')


if __name__ == '__main__':
    app.run()
