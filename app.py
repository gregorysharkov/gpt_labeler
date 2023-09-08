'''main application entry point'''

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
    '''default entry point to the application'''
    if request.method == "POST":
        review = request.form.get('review')
        processed_revew = process_review(review)
        return redirect(
            url_for(
                'index',
                original_review=review,
                processed_revew=processed_revew,
            )
        )

    original_review = request.args.get('original_review')
    processed_review = request.args.get("processed_revew")
    return render_template(
        "index.html",
        original_review=original_review,
        processed_review=processed_review
    )


def process_review(review: str | None) -> str:
    '''function processes review'''
    if review is None:
        return ""

    return "Thank you for your review, " + review


if __name__ == "__main__":
    app.run()