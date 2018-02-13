from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/home')
def homepage():
	return 'This is a homepage'

@app.route('/test')
def test():
	num1 = input('Enter first number:')
	num2 = input('Enter second number:')
	sum = float(num1) + float(num2)
	print('This is Addition operation')
	print('Sum of your numbers is:')
	return sum 
	
 
if __name__ == "__main__":
    app.run()