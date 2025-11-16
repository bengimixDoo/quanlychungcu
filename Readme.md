# Tạo venv
python -m venv venv

# Kích hoạt venv
.\venv\Scripts\Activate.ps1

# chạy requirement.txt để set up các thư viện cần thiết vào venv
pip install -r requirements.txt



# Copy Database_URL bên em 
DATABASE_URL='postgresql://neondb_owner:npg_BZMv8uX9VGQH@ep-small-art-a1we2x30-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

# thay đổi file setting.py (chuẩn câu lệnh trong neon )
# Add these at the top of your settings.py
<!-- import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qsl

load_dotenv()

# Replace the DATABASES section of your settings.py with this
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': tmpPostgres.path.replace('/', ''),
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
        'OPTIONS': dict(parse_qsl(tmpPostgres.query)),
    }
} -->


# chạy thử file test.py để test đọc database trên neon 

đccccccccmmmmm anh sơn thay đổi file setting py ít thôi , thay loạn lên nó thiếu thư viện chả đéo chạy, 
setting.py copy bên em chỉ thay đổi so với django gốc mỗi cái database_url thôi, 
thay đổi ồi tạo thêm API