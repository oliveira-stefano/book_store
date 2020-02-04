from app import create_app, db
import os

app = create_app(os.getenv("FLASK_ENV", "development"))

@app.shell_context_processor
def create_context_processor():
    return dict(
        app=app,
        db=db
    )

if __name__ == "__main__":
    app.run(debug=True)