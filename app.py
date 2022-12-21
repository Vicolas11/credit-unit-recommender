from flask import Flask,render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/recommender', methods=['GET', 'POST'])
def creditUnitRecommender():
	if request.method == 'POST':
		semester = request.form['semester']
		level = request.form['level']	

		if semester and level:
			level = int(level)
			result = ""
			if level == 100 and semester == "First Semester":
				result = "Not yet on probation!"
			if level == 100 and semester == "Second Semester":
				result = "Register the maximum credit units"
			if level == 200 and semester == "First Semester":
				result = "Register the maximum credit units"
			if level == 200 and semester == "Second Semester":
				result = "Register below 20 but more than minimum"
			if level == 300 and semester == "First Semester":
				result = "Register above 20 but more than minimum"
			if level == 300 and semester == "Second Semester":
				result = "Register SIWES Credit units!"

			data = {'status': 200, "result": result}
			response = jsonify(data)
			response.status_code = 200
			return response
		else:
			data = {'status': 400, "error": "No text upload"}
			response = jsonify(data)
			response.status_code = 400
			return response

if __name__ == '__main__':
	app.run(debug=True)