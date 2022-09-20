from django.shortcuts import render

# Create your views here.
def prodi2(request):
    judul = ["Akuntansi (S1)", "Managemen (S1)", "Ekonomi Syariah (S1)", "Ilmu Ekonomi Pembangunan (S1)", "Akuntansi (D3)", "Perpajakan (D3)", "Marketing (D3)", "Keuangan Perbankan (D3)"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'feb\index.html', konteks)
