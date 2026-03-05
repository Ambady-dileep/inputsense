from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import NameValidationForm


def validate_details(request):

    request.session.setdefault("attempts_left", 3)
    request.session.setdefault("score", 0)
    request.session.setdefault("validated", False)

    if request.method == "POST":

        attempts_left = request.session["attempts_left"]

        if attempts_left <= 0:
            return render(request, "validator/form.html", {
                "form": NameValidationForm(),
                "attempts_left": 0,
                "score": request.session["score"],
                "locked": True,
            })

        # Block double success — already validated this session
        if request.session.get("validated"):
            return redirect("success")

        form = NameValidationForm(request.POST)

        if form.is_valid():
            # Attempts are NOT decremented on a successful submit
            request.session["score"] += 1
            request.session["validated"] = True
            request.session.modified = True
            return redirect("success")
        else:
            # Decrement only on failure, clamped to floor of 0
            request.session["attempts_left"] = max(0, attempts_left - 1)
            request.session.modified = True

    else:
        form = NameValidationForm()

    return render(request, "validator/form.html", {
        "form": form,
        "attempts_left": request.session["attempts_left"],
        "score": request.session["score"],
        "locked": request.session["attempts_left"] <= 0,
    })


@require_POST
def reset(request):
    request.session.flush()
    request.session["attempts_left"] = 3
    request.session["score"] = 0
    request.session["validated"] = False
    return redirect("validation")


def success(request):
    if not request.session.get("validated"):
        return redirect("validation")

    score = request.session.get("last_score", request.session.get("score", 0))
    attempts_left = request.session.get("last_attempts_left", request.session.get("attempts_left", 0))

    request.session["validated"] = False
    request.session.modified = True

    return render(request, "validator/success.html", {
        "score": score,
        "attempts_left": attempts_left,
    })  