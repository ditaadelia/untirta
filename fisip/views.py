from django.shortcuts import render

# Create your views here.
def prodi4(request):
    judul = ["Ilmu Komunikasi", "Ilmu Pemerintahan", "Administrasi Publik"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fisip\index.html', konteks)
