
from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

Patient_details = [{
    "id": 1,
    "patient_name": "sai",
    "age": 32,
    "gender": "male",
    "contact": "9876543210",
    "disease": "cold",
    "doctor_assigned": "Dr. Sharat"
}]


# ------------------ HOME PAGE ------------------

@app.route("/", methods=["GET"])
def homepage():
    return '''
    <h1><center>WELCOME TO HOSPITAL MANAGEMENT SYSTEM</center></h1>

    <h3>To register a patient, please visit: /form</h3>

    <hr>

    <h3>Available API Endpoints:</h3>
    <ul>
        <li>GET /api/patients</li> ---> to get all patients details
        <li>GET /api/patients/&lt;id&gt;</li> ---> to get single patient details
        <li>POST /api/patients</li> ---> to post details of patient
        <li>PUT /api/patients/&lt;id&gt;</li> ---> to update the details of patients
        <li>DELETE /api/patients/&lt;id&gt;</li> ---> to delete the details of patient
    </ul>
    <hr>

    <h4>⚠ Use Postman Application to test POST, PUT, DELETE  APIs</h4>
    '''


# ------------------ FORM PAGE ------------------

@app.route("/form")
def form():
    return '''
    <h1><center>Patient Registration Form</center></h1>

    <form action="/api/patients" method="post">

        Name:
        <input type="text" name="patient_name"><br><br>

        Age:
        <input type="number" name="age"><br><br>

        Gender:
        <input type="radio" name="gender" value="male">Male
        <input type="radio" name="gender" value="female">Female
        <br><br>

        Contact:
        <input type="tel" name="contact" pattern="[0-9]{10}" maxlength="10">
        <br><br>

        Disease:
        <input type="text" name="disease"><br><br>

        Doctor Assigned:
        <select name="doctor_assigned">
            <option value="Dr. Sharat">Dr. Sharat</option>
            <option value="Dr. Seenu">Dr. Seenu</option>
            <option value="Dr. Mahesh">Dr. Mahesh</option>
            <option value="Dr. Gayathri">Dr. Gayathri</option>
            <option value="Dr. Neha">Dr. Neha</option>
        </select>
        <br><br>

        <input type="submit" value="Submit Details">

    </form>
    '''


# ------------------ GET ALL ------------------

@app.route("/api/patients", methods=["GET"])
def all_patients():
    return jsonify(Patient_details), 200


# ------------------ GET SINGLE ------------------

@app.route("/api/patients/<int:patient_id>", methods=["GET"])
def single_patient(patient_id):
    for patient in Patient_details:
        if patient["id"] == patient_id:
            return jsonify(patient), 200
    return jsonify({"message": "Patient Not Found"}), 404


# ------------------ POST ------------------
@app.route("/api/patients", methods=["POST"])
def register_patient():

    if request.is_json:
        data = request.json
    else:
        data = request.form

    new_patient = {
        "id": Patient_details[-1]["id"] + 1 if Patient_details else 1,
        "patient_name": data.get("patient_name"),
        "age": data.get("age"),
        "gender": data.get("gender"),
        "contact": data.get("contact"),
        "disease": data.get("disease"),
        "doctor_assigned": data.get("doctor_assigned")
    }

    Patient_details.append(new_patient)

    if request.is_json:
        return jsonify(new_patient), 201

    return redirect("/success")



# ------------------ PUT ------------------

@app.route("/api/patients/<int:patient_id>", methods=["PUT"])
def update_patient(patient_id):
    data = request.json

    for patient in Patient_details:
        if patient["id"] == patient_id:
            patient["patient_name"] = data.get("patient_name", patient["patient_name"])
            patient["age"] = data.get("age", patient["age"])
            patient["gender"] = data.get("gender", patient["gender"])
            patient["contact"] = data.get("contact", patient["contact"])
            patient["disease"] = data.get("disease", patient["disease"])
            patient["doctor_assigned"] = data.get("doctor_assigned", patient["doctor_assigned"])
            return jsonify(patient), 200

    return jsonify({"message": "Patient Not Found"}), 404


# ------------------ DELETE ------------------

@app.route("/api/patients/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    for patient in Patient_details:
        if patient["id"] == patient_id:
            Patient_details.remove(patient)
            return jsonify({"message": "Patient deleted successfully"}), 200

    return jsonify({"message": "Patient Not Found"}), 404


# ------------------ SUCCESS PAGE ------------------

@app.route("/success")
def success():
    return '''
    <h2>Details Submitted Successfully</h2>
    <a href="/">Go Back to Home</a>
    '''


if __name__ == "__main__":
    app.run(debug=True)
