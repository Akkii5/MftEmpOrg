from flask import request, jsonify, Blueprint
from app.models.database import db
from app.models.organisation import Organisation

organisation_bp = Blueprint('organisation_bp', __name__)

@organisation_bp.route("/organisations", methods=["GET"])
def get_all_organisations():
    orgs = Organisation.query.all()
    return jsonify([{"code": org.code, "org_name": org.org_name, "details": org.details} for org in orgs])

@organisation_bp.route("/organisations/<int:code>", methods=["GET"])
def get_organisation_by_code(code):
    org = Organisation.query.filter_by(code=code).first()
    if not org:
        return jsonify({"error": "Organisation not found"}), 404
    return jsonify({"code": org.code, "org_name": org.org_name, "details": org.details})

@organisation_bp.route("/organisations", methods=["POST"])
def create_organisation():
    data = request.json
    new_org = Organisation(
        code=data["code"], org_name=data["org_name"], details=data["details"]
    )
    db.session.add(new_org)
    db.session.commit()
    return jsonify({"message": "Organisation created"}), 201

@organisation_bp.route("/organisations/<int:code>", methods=["PUT"])
def update_organisation(code):
    org = Organisation.query.get(code)
    if not org:
        return jsonify({"error": "Organisation not found"}), 404
    data = request.json
    org.org_name = data.get("org_name", org.org_name)
    org.details = data.get("details", org.details)
    db.session.commit()
    return jsonify({"message": "Organisation updated"}), 200

@organisation_bp.route("/organisations/<int:code>", methods=["DELETE"])
def delete_organisation(code):
    org = Organisation.query.get(code)
    if not org:
        return jsonify({"error": "Organisation not found"}), 404
    db.session.delete(org)
    db.session.commit()
    return jsonify({"message": "Organisation deleted"}), 200
