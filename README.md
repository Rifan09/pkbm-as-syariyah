---

## 🏫 **PKBM As-Syari’yah Website**

Website resmi **PKBM As-Syari’yah** — platform informasi dan layanan pendidikan nonformal berbasis web, yang mencakup sistem **pendaftaran siswa**, **berita kegiatan**, dan **galeri multimedia**.
Dibangun menggunakan **Django**, dengan integrasi **Cloudinary** untuk media storage dan **Railway** sebagai hosting.

---
## 🌐 Website Resmi

🔗 **[Kunjungi Website PKBM As-Syari’yah](https://pkbmassyariyah.my.id)**  
*(Jika domain custom belum aktif, gunakan Railway URL: [https://pkbm-as-syariyah-production.up.railway.app/](https://pkbm-as-syariyah-production.up.railway.app/))*

---

### **Fitur Utama**

| Fitur                                                 | Deskripsi                                                                                                |
| :---------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| 🧾 **Pendaftaran Online**                             | Formulir digital untuk calon peserta didik (Paket A, B, C) dengan upload dokumen otomatis ke Cloudinary. |
| 📰 **Berita & Informasi**                             | Admin dapat menambahkan berita dan artikel pendidikan yang tampil di halaman publik.                     |
| 🖼️ **Galeri Kegiatan**                               | Menampilkan foto dan video kegiatan belajar, keterampilan, dan acara PKBM per bulan.                     |
| 👨‍🏫 **Daftar PTK (Pendidik & Tenaga Kependidikan)** | Tampilan interaktif berisi profil guru dan instruktur PKBM.                                              |
| ⚙️ **Panel Admin Django**                             | Kelola data pendaftaran, berita, dan galeri dengan mudah melalui dashboard admin.                        |

---

### 🧰 **Tech Stack**

* **Framework:** Django
* **Database:** PostgreSQL (via Railway)
* **Media Storage:** Cloudinary
* **Static Serving:** WhiteNoise
* **Frontend:** HTML5, Bootstrap 5, CSS3, JavaScript (AOS Animation, Swiper.js)
* **Hosting:** Railway
* **Version Control:** GitHub

---

### 📁 **Struktur Direktori Utama**

```
pkbm-as-syariyah/
│
├── manage.py
├── requirements.txt
├── Procfile
├── README.md
│
├── pkbm/                 # Folder utama proyek (settings, urls, wsgi)
├── pkbmapp/              # Aplikasi utama (berita, galeri, profil PKBM)
├── pendaftaran/          # Aplikasi pendaftaran siswa
│
├── static/               # File CSS, JS, images
├── staticfiles/          
├── media/                # File upload (Cloudinary akan menangani di production)
├── templates/            # Template HTML
│
└── db.sqlite3            # Database lokal (otomatis digantikan oleh PostgreSQL di Railway)
```

---

### ⚙️ **Instalasi Lokal (Development)**

#### 1️⃣ Clone repository

```bash
git clone https://github.com/username/pkbm-as-syariyah.git
cd pkbm-as-syariyah
```

#### 2️⃣ Buat virtual environment & aktifkan

```bash
python -m venv venv
venv\Scripts\activate  # (Windows)
# atau
source venv/bin/activate  # (Mac/Linux)
```

#### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Jalankan migrasi database

```bash
python manage.py migrate
```

#### 5️⃣ Jalankan server lokal

```bash
python manage.py runserver
```

Lalu buka di browser:
👉 `http://127.0.0.1:8000/`

---

### ☁️ **Deploy ke Railway + Cloudinary**

#### 1️⃣ Upload project ke GitHub

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

#### 2️⃣ Deploy ke Railway

1. Login ke [https://railway.app](https://railway.app)
2. Klik **New Project → Deploy from GitHub repo**
3. Tambahkan **PostgreSQL plugin**
4. Tambahkan environment variables:

   ```
   DATABASE_URL=postgresql://...
   DJANGO_SECRET_KEY=your-secret-key
   CLOUDINARY_CLOUD_NAME=your-cloud-name
   CLOUDINARY_API_KEY=your-api-key
   CLOUDINARY_API_SECRET=your-api-secret
   DEBUG=False
   ```

#### 3️⃣ Jalankan migrasi & collectstatic di Railway shell:

```bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

---

### 🧩 **Environment Variables**

| Variable                | Deskripsi                    |
| :---------------------- | :--------------------------- |
| `DJANGO_SECRET_KEY`     | Secret key Django            |
| `DEBUG`                 | Set ke `False` di production |
| `DATABASE_URL`          | PostgreSQL URL dari Railway  |
| `CLOUDINARY_CLOUD_NAME` | Nama akun Cloudinary         |
| `CLOUDINARY_API_KEY`    | API Key dari Cloudinary      |
| `CLOUDINARY_API_SECRET` | API Secret dari Cloudinary   |

---

### 🧾 **File Penting untuk Deploy**

#### `Procfile`

```
web: gunicorn pkbm.wsgi
```

#### `requirements.txt` (minimal)

```
Django>=5.0
dj-database-url
psycopg2-binary
cloudinary
django-cloudinary-storage
gunicorn
whitenoise
```
---

### 👨‍💻 **Developer**

**Rifan — AI & Web Developer Integration**
Membangun sistem pembelajaran dan digitalisasi PKBM berbasis Django.

---


