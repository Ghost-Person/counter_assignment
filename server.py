from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "Griffith is a putz."

@app.route('/')
def times():
    if "time" not in session:
        session["time"] = 0
    else:
        session['time'] += 1
    return render_template("index.html")

@app.route('/restart')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)