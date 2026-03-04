from django.shortcuts import render, redirect
from .forms import NameValidationForm

def validate_details(request):

  request.session.setdefault("attempts_left", 3)
  request.session.setdefault("score",0)
  
  attempts_left = request.session["attempts_left"]
  score = request.session["score"]

  if request.method == "POST":

    if attempts_left <= 0:
      return render(request, "validator/form.html",{
        "form":NameValidationForm(),
        "attempts_left":attempts_left,
        "score":score,
        "locked":True,
      })

    form = NameValidationForm(request.POST)
    
    request.session["attempts_left"] -= 1

    if form.is_valid():
      request.session["score"]+=1
      return redirect("success") 
  else:
    form = NameValidationForm()

  return render(request,"validator/form.html",{
    "form":form,
    "attempts_left": request.session["attempts_left"],
    "score": request.session["score"],
    "locked": request.session["attempts_left"] <= 0,
  }
)

def success(request):
    return render(request, "validator/success.html", {
        "score": request.session.get("score", 0)
    })






