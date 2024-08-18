from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    address = request.form.get('address')

    # 處理表單數據 (這裡簡單地打印輸入)
    print(f'Name: {name}, Phone: {phone}, Address: {address}')
    
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting your information!"

if __name__ == '__main__':
    app.run(debug=True)
