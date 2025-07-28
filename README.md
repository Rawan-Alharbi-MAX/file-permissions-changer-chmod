# 🔐 change_file_permissions.py

سكربت بلغة Python لتغيير صلاحيات ملف إلى `rwxrwxr-x` (يعني 775) باستخدام الأمر `chmod`.

## 📌 Purpose | الهدف
This script is designed to modify file permissions in Linux/Unix systems using Python's `os.chmod()` function.

يحدد صلاحيات الملف بحيث:
- Owner = read, write, execute ✅
- Group = read, write, execute ✅
- Others = read, execute ❌✍️

## 📂 File Info | معلومات الملف
- **File Name:** `change_file_permissions.py`
- **Language:** Python 3.x
- **Required Module:** `os` (built-in)

## 🧪 How to Use | طريقة الاستخدام

1. تأكد أن الملف المطلوب موجود في نفس المجلد.
2. افتح التيرمنال (Terminal) .
3. شغّل السكربت:

```bash
python change_file_permissions.py

import os

file_path = "example.txt"     # اسم الملف المطلوب
permissions = 0o775           # rwxrwxr-x

os.chmod(file_path, permissions)
print(f"تم تغيير صلاحيات الملف '{file_path}' إلى 775.")


⚠️ Notes | ملاحظات
هذا السكربت يعمل بشكل أفضل على أنظمة Linux .

في Windows قد لا تكون صلاحيات الملفات بنفس التأثير.

تأكد أنك تملك صلاحيات كافية لتعديل الملفات.

👤من إعداد : روان الحربي 
