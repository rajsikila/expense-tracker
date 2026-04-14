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
        margin: 0;
        font-family: 'Segoe UI', sans-serif;
        background: #0f172a;
        color: white;
    }

    .container {
        max-width: 500px;
        margin: 40px auto;
        background: #1e293b;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 0 30px rgba(0,0,0,0.5);
    }

    h1 {
        color: #38bdf8;
        text-align: center;
    }

    form {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
    }

    input {
        flex: 1;
        padding: 10px;
        border-radius: 8px;
        border: none;
        background: #334155;
        color: white;
    }

    button {
        padding: 10px;
        background: #22c55e;
        border: none;
        border-radius: 8px;
        color: white;
        cursor: pointer;
    }

    button:hover {
        background: #16a34a;
    }

    .card {
        background: #334155;
        padding: 12px;
        margin: 10px 0;
        border-radius: 10px;
        display: flex;
        justify-content: space-between;
    }

    .delete {
        color: #ef4444;
        text-decoration: none;
        font-weight: bold;
    }

    .total {
        margin-top: 20px;
        font-size: 22px;
        text-align: center;
        color: #22c55e;
    }
</style>
</head>

<body>

<div class="container">
    <h1>💸 Expense Tracker</h1>

    <form method="POST">
        <input type="text" name="desc" placeholder="Description" required>
        <input type="number" name="amount" placeholder="Amount" required>
        <button>Add</button>
    </form>

    {% for e in expenses %}
        <div class="card">
            <span>{{ e[0] }} - ₹{{ e[1] }}</span>
            <a class="delete" href="/delete/{{ loop.index0 }}">✖</a>
        </div>
    {% endfor %}

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
