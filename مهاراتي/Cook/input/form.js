// إضافة تأثير الكتابة على الحروف
const labels = document.querySelectorAll('.form-control label');

labels.forEach(label => {
    label.innerHTML = label.innerText
        .split('')
        .map((letter, idx) => `<span style="transition-delay:${idx * 50}ms">${letter}</span>`)
        .join('');
});

// دالة تسجيل الدخول
const loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', (e) => {
    e.preventDefault(); // منع إعادة تحميل الصفحة

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (email && password) {
        if (email.includes('@') && password === "123456") { // كلمة المرور الافتراضية للاختبار
            const username = email.split('@')[0]; // استخراج اسم المستخدم
            alert(`Welcome, ${username}! You have successfully logged in.`);
        } else {
            alert('Invalid email or password. Please try again.');
        }
    } else {
        alert('Please enter both email and password.');
    }
});