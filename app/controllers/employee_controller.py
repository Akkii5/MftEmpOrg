from flask import request, jsonify, Blueprint
from app.models.database import db
from app.models.employee import Employee

employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route("/employees", methods=["GET"])
def get_all_employees():
    employees = Employee.query.all()
    return jsonify([{
        "id": emp.id, "fname": emp.fname, "lname": emp.lname,
        "email": emp.email, "address": emp.address, "org_code": emp.org_code
    } for emp in employees])

@employee_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee_by_id(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify({
        "id": emp.id, "fname": emp.fname, "lname": emp.lname,
        "email": emp.email, "address": emp.address, "org_code": emp.org_code
    })

@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.json
    new_employee = Employee(
        fname=data["fname"], lname=data["lname"], email=data["email"],
        address=data["address"], org_code=data["org_code"]
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": "Employee created"}), 201

@employee_bp.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    data = request.json
    emp.fname = data.get("fname", emp.fname)
    emp.lname = data.get("lname", emp.lname)
    emp.email = data.get("email", emp.email)
    emp.address = data.get("address", emp.address)
    db.session.commit()
    return jsonify({"message": "Employee updated"}), 200

@employee_bp.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Employee deleted"}), 200
