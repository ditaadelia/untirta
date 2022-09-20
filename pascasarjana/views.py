from django.shortcuts import render

# Create your views here.
def prodi8(request):
    judul = ["Pendidikan Bahasa Indonesia", "Teknologi Pendidikan", "Hukum", "Administrasi Publik", "Akuntansi", "Manajemen", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Ilmu Pertanian", "Ilmu Komunikasi", "Teknik Kimia", "Pendidikan Dasar", "Ekonomi"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'pascasarjana\index.html', konteks)
