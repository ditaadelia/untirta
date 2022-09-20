from django.shortcuts import render

# Create your views here.
def prodi5(request):
    judul = ["Pendidikan Kedokteran", "Keperawatan (S1)", "Keperawatan (D3)", "Gizi", "Ilmu Keolahragaan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fk\index.html', konteks)
