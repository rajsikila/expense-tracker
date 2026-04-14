from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

expenses = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Expense Tracker</title>
</head>
<body style="font-family: Arial; text-align:center;">

    <h1>💸 Expense Tracker</h1>
    <h3>Track your daily spending (Cloud App)</h3>

    <form method="POST">
        <input type="text" name="desc" placeholder="Expense description" required>
        <input type="number" name="amount" placeholder="Amount" required>
        <button type="submit">Add</button>
    </form>

    <h2>Expenses:</h2>
    <ul>
        {% for e in expenses %}
            <li>
                {{ e[0] }} - ₹{{ e[1] }}
                <a href="/delete/{{ loop.index0 }}">❌</a>
            </li>
        {% endfor %}
    </ul>

    <h2>Total: ₹{{ total }}</h2>

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