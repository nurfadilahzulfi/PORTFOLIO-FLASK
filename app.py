from flask import Flask, render_template

app = Flask(__name__)

# Data proyek yang lebih komprehensif
PROJECT_LIST = [
    {
        'id': 1,
        'name': 'Sistem Deteksi Kantuk | Machine Learning',
        'description': 'Mengembangkan sistem deteksi kantuk dengan menggunakan library Dlib.',
        'full_description': '''
        Proyek ini bertujuan untuk mengembangkan sistem rekomendasi yang cerdas menggunakan teknik machine learning. Dengan memanfaatkan algoritma collaborative filtering, sistem ini mampu menganalisis pola wajah pengguna melalui deteksi pada kelopak mata,
        apabila pengguna mengantuk maka alarm pada sistem secara otomatis akan berdering, proyek ini dapat diimplementasikan di berbagai bidang,
        baik dalam bidang industri otomotif dan industri lainnya.

        Fitur utama:
        - Analisis pola preferensi pengguna
        - Algoritma collaborative filtering
        - Prediksi wajah mengantuk
        ''',
        'technologies': ['Python', 'Scikit-learn', 'Pandas', 'NumPy', 'Open-CV'],
        'link': '#',
        'image': 'Deteksi-Kantuk.jpg',
        'github_link': 'https://github.com/nurfadilahzulfi/Deteksi-Pengemudi-Mengantuk',
        'challenges': [
            'Mengolah data yang besar',
            'Membangun model prediksi akurat dan efisien',
            'Mengurangi bias rekomendasi',
            'Pengolahan citra digital'
        ],
        'learnings': [
            'Teknik preprocessing data',
            'Membangun model machine learning',
            'Evaluasi performa model'
        ]
    },
    {
        'id': 2,
        'name': 'Sistem Deteksi Nomor Plat Kendaraan',
        'description': 'Sistem yang dirancang untuk menangkap plat nomor kendaraan menggunakan algoritma haarcascade.',
        'full_description': '''
        Proyek deteksi plat otomatis menggunakan algoritma haarcascade ini dirancang khusus untuk keamanan dalam berlalu lintas dan juga lingkungan lainnya.

        Fitur utama:
        - Deteksi nomor plat kendaraan
        - Export deteksi gambar kedalam bentuk teks
        ''',
        'technologies': ['Python', 'Pandas', 'Plotly', 'Flask', 'Open-CV'],
        'link': '#',
        'image': 'plat-license.jpg',
        'github_link': 'https://github.com/nurfadilahzulfi/Deteksi-Pengemudi-Mengantuk',
        'challenges': [
            'Integrasi data dari berbagai sumber',
            'Membuat visualisasi yang informatif',
            'Membangun model prediksi akurat'
        ],
        'learnings': [
            'Teknik pengolahan citra digital',
            'Pengembangan keamanan otomotif',
            'Analisis trend penjualan'
        ]
    },
    {
        'id': 3,
        'name': 'Laundry Zulfi',
        'description': 'Sistem yang dirancang untuk kemudahan dalam transaksi pencucian pakaian',
        'full_description': '''
        Proyek deteksi plat otomatis menggunakan algoritma haarcascade ini dirancang khusus untuk keamanan dalam berlalu lintas dan juga lingkungan lainnya.

        Fitur utama:
        - Pencatatan Transaksi
        - Pendataan Pelanggan
        - Penjadwalan pencucian
        ''',
        'technologies': ['Php', 'Bootstrap', 'Mysql', 'Javascript'],
        'link': '#',
        'image': 'laundry.png',
        'github_link': 'https://github.com/nurfadilahzulfi/laundry',
        'challenges': [
            'Integrasi data dari berbagai sumber',
            'Membuat visualisasi yang informatif',
            'Membangun model prediksi akurat'
        ],
        'learnings': [
            'Teknik pe',
            'Pengembangan keamanan otomotif',
            'Analisis trend penjualan'
        ]
    }   
]

@app.route('/')
def index():
    # Data profil yang lebih komprehensif
    profile_data = {
        'name': 'Nur Fadilah Zulfi',
        'title': 'Software Engineer | Data Analyst | Machine Learning Engineer',
        'description': 'Mahasiswa passionate yang berfokus pada pengembangan teknologi untuk memajukan bangsa. Dengan keahlian di bidang programming dan analisis data, saya berkomitmen untuk menciptakan solusi inovatif.',
        'photo': 'profile.jpg',
        'skills': [
            {'name': 'Python', 'level': 90},
            {'name': 'Machine Learning', 'level': 85},
            {'name': 'Data Analysis', 'level': 80},
            {'name': 'Data Science', 'level': 75},
            {'name': 'SQL', 'level': 90},
            {'name': 'JavaScript', 'level': 55}
        ],
        'education': [
            {
                'institution': 'Politeknik Negeri Lhokseumawe',
                'major': 'Teknik Informatika',
                'year': '2022 - Sekarang'
            }
        ],
        'contact': {
            'email': 'nurfadilahzulfi@gmail.com',
            'linkedin': 'http://linkedin.com/in/nur-fadilah-zulfi-43a966257',
            'github': 'https://github.com/nurfadilahzulfi',
            'instagram': '@nurfadilahzulfi'
        }
    }
    return render_template('index.html', profile=profile_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECT_LIST)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    # Cari proyek berdasarkan ID
    project = next((proj for proj in PROJECT_LIST if proj['id'] == project_id), None)
    
    if project is None:
        # Jika proyek tidak ditemukan, kembalikan ke halaman projects
        return render_template('projects.html', projects=PROJECT_LIST)
    
    return render_template('project_detail.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)