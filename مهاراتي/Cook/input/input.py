import tkinter as tk
from tkinter import messagebox

# دالة لمعالجة تسجيل الدخول
def login():
    email = entry_email.get()
    password = entry_password.get()

    if email and password:
        if "@" in email and password == "123456":  # كلمة المرور الافتراضية للاختبار
            # استخراج اسم المستخدم من البريد الإلكتروني (الجزء قبل @)
            username = email.split("@")[0]
            messagebox.showinfo("مرحبًا", f"مرحبًا {username}! تم تسجيل الدخول بنجاح.")
        else:
            messagebox.showerror("خطأ", "البريد الإلكتروني أو كلمة المرور غير صحيحة.")
    else:
        messagebox.showerror("خطأ", "يرجى إدخال البريد الإلكتروني وكلمة المرور.")


# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("نموذج تسجيل الدخول")

# إضافة عناصر الواجهة
label_email = tk.Label(root, text="البريد الإلكتروني:")
label_password = tk.Label(root, text="كلمة المرور:")
entry_email = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # إخفاء كلمة المرور
button_login = tk.Button(root, text="تسجيل الدخول", command=login)

# وضع العناصر في النافذة
label_email.grid(row=0, column=0, padx=10, pady=10)
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_email.grid(row=0, column=1, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
button_login.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# تشغيل الواجهة
root.mainloop()