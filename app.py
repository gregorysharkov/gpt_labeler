'''main application entry point'''

from flask import Flask, redirect, render_template, request, url_for

from src.request_utils import generate_response

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

    response = generate_response(review)
    response_text = response['choices'][0]['message'].content

    return "Thank you for your review<br/>" + response_text


if __name__ == "__main__":
    app.run()