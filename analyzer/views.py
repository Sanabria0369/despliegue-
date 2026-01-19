from django.shortcuts import render
from .forms import EmailForm
from .svm_model import predict_email

def index(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['contenido']
            resultado, prob = predict_email(texto)
            return render(request, 'analyzer/result.html', {
                'resultado': resultado,
                'phishing': round(prob[0]*100, 2),
                'legitimo': round(prob[1]*100, 2)
            })
    else:
        form = EmailForm()
    return render(request, 'analyzer/index.html', {'form': form})
