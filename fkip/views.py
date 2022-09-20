from django.shortcuts import render

# Create your views here.
def prodi6(request):
    judul = ["Pendidikan Non Formal", "Pendidikan Guru Sekolah Dasar", "Pendidikan Anak Usia Dini", "Pendidikan Fisika", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Kimia", "Pendidikan Matematika", "Pendidikan Biologi", "Pendidikan Vokasi Teknik Elektro", "Pendidikan Vokasi Teknik Mesin", "Pendidikan Sosiologi", "Pendidikan Sejarah", "Pendidikan Khusus", "Pendidikan Kewarganegaraan", "Bimbingan Konseling", "Pendidikan IPA", "Pendidikan Seni Pertunjukan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fKIP\index.html', konteks)
