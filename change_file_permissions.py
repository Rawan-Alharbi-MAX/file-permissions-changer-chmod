# This script changes file permissions to rwxrwxr-x (775) using chmod

import os

# اسم الملف اللي تبغى تغيّر صلاحياته
file_path = "example.txt"  # غيّر الاسم الي الملف عندك

# صلاحيات rwxrwxr-x = 775
permissions = 0o775  

# الحين يغير الصلاحيات 
try:
    os.chmod(file_path, permissions)
    print(f"تم تغيير صلاحيات الملف '{file_path}' إلى 775 (rwxrwxr-x).")
except FileNotFoundError:
    print(f"الملف '{file_path}' غير موجود.")
except PermissionError:
    print(f"ليس لديك صلاحية لتعديل الملف '{file_path}'.")
except Exception as e:
    print(f"حدث خطأ: {e}")
