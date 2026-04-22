# code-camp
A modern online pizza store web application built using python and the streamlit framework
<div align="center">

<img src="https://images.unsplash.com/photo-1513104890138-7c749659a591?q=80&w=200&auto=format&fit=crop" width="150" style="border-radius: 50%;">

# 🍕 PizzaHub Streamlit Web App

**تطبيق متكامل لطلب البيتزا، المعكرونة، والمشروبات مدعوم بواجهة مستخدم عصرية ونظام تسجيل دخول.**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)

</div>

---

## 📖 نظرة عامة (Overview)
PizzaHub هو تطبيق ويب تم بناؤه باستخدام مكتبة **Streamlit**. يتيح للمستخدمين استعراض قائمة الطعام، اختيار الأحجام والكميات، وإتمام الطلبات بعد تسجيل الدخول. يتميز التطبيق بنظام تنقل (Navigation) سهل وواجهات تفاعلية.

## ✨ المميزات الرئيسية
* **🏡 الصفحة الرئيسية:** واجهة ترحيبية مع أزرار اختصار للتنقل السريع.
* **🔒 نظام المصادقة:** صفحات مخصصة للـ Sign In و Sign Up لحماية قائمة الطلبات.
* **📝 قائمة طعام تفاعلية:** تقسيم المنيو إلى (بيتزا، باستا، مشروبات) باستخدام نظام التبويبات (Tabs).
* **🛒 ملخص الطلب:** حساب تلقائي لإجمالي السعر بناءً على الكميات والأحجام المختارة.
* **📱 متجاوب:** يعمل بشكل رائع على المتصفحات المختلفة وأجهزة الكمبيوتر.

---

## 🛠️ التكنولوجيا المستخدمة
<table align="center">
  <tr>
    <td align="center"><b>المكتبة</b></td>
    <td><b>الوصف</b></td>
  </tr>
  <tr>
    <td>Streamlit</td>
    <td>لبناء واجهة المستخدم والتنقل بين الصفحات</td>
  </tr>
  <tr>
    <td>Pandas</td>
    <td>لإدارة ملخص الطلبات وعرضها في جداول</td>
  </tr>
  <tr>
    <td>Session State</td>
    <td>لإدارة بيانات المستخدم وحالة تسجيل الدخول</td>
  </tr>
</table>

---

## 🚀 كيفية التشغيل (Installation)

1. **قم بتحميل الكود:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/pizzahub-streamlit.git](https://github.com/YOUR_USERNAME/pizzahub-streamlit.git)
   cd pizzahub-streamlit
