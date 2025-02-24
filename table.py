from flask import Flask, request, render_template_string

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST']) 
def multiplication_table():
    result = [] 
    if request.method == 'POST': 
        a = int(request.form['number']) 
        for b in range(1, 21): 
            p = a * b 
            sum = (a, 'X', b, '=', p)
            result.append(sum) 

    return render_template_string('''
    <html> 
    <head> 
        <title>Multiplication Table</title> 
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: url(data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400' viewBox='0 0 600 400'%3E%3Cg opacity='0.05'%3E%3Ctext x='50%' y='50%' font-size='50' text-anchor='middle' fill='%23000'%3EMani's Calculator%3C/text%3E%3C/g%3E%3C/svg%3E) no-repeat center center;
                background-size: cover;
                background-color: #e0f7fa;
                color: #00796b;
            }
            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.8);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            h1 {
                color: #004d40;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                background: #b2dfdb;
                margin: 5px 0;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            input[type="number"], input[type="submit"] {
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #00796b;
                margin: 5px;
                background-color: #00796b;
                color: white;
            }
            input[type="number"]:focus, input[type="submit"]:hover {
                background-color: #004d40;
                border-color: #004d40;
            }
        </style>
    </head> 
    <body>
        <div class="container">
            <h1>Enter a number to get its multiplication table</h1> 
            <form method="post"> 
                <input type="number" name="number" required> 
                <input type="submit" value="Generate Table"> 
            </form> 
            {% if result %}
                <h2>Multiplication Table</h2> 
                <ul> 
                {% for value in result %} 
                    <li>{{ value }}</li> 
                {% endfor %}
                </ul> 
            {% endif %} 
        </div>
    </body> 
    </html>''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
