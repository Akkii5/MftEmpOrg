from flask import Flask
from app.models.database import create_app
from app.controllers.employee_controller import employee_bp
from app.controllers.organisation_controller import organisation_bp

app = create_app()

# Register Blueprints
app.register_blueprint(employee_bp)
app.register_blueprint(organisation_bp)

if __name__ == "__main__":
    app.run(debug=True)
