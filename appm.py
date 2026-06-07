import streamlit as st

# =========================
# إعداد الصفحة
# =========================

st.set_page_config(
    page_title="Nasij Studio",
    page_icon="🧶",
    layout="wide"
)

# =========================
# التصميم العام
# =========================

st.markdown("""
<style>

.stApp{
    background-color:#0B0B0B;
}

h1,h2,h3{
    color:#D4AF37;
}

section[data-testid="stSidebar"]{
    background-color:#111827;
}

div[data-testid="metric-container"]{
    background:#1A1A1A;
    border:1px solid #D4AF37;
    border-radius:15px;
    padding:15px;
}

button{
    border-radius:15px !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# الأسعار
# =========================

prices = {
    "بوليستر":80,
    "نايلون":120,
    "صوف":220,
    "حرير":450
}

# =========================
# القائمة الجانبية
# =========================

st.sidebar.markdown("""
# 🧶 NASIJ STUDIO

### Premium Edition
""")

page = st.sidebar.radio(
    "القائمة الرئيسية",
    [
        "🏠 الرئيسية",
        "🎨 استوديو التصميم",
        "🧶 الخامات",
        "📚 الكاتالوج",
        "💰 التسعير",
        "⭐ مشاريع العملاء",
        "📞 التواصل"
    ]
)

# =========================
# الرئيسية
# =========================

if page == "🏠 الرئيسية":

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#111111,#1A1A1A);
    padding:40px;
    border-radius:20px;
    border:1px solid #D4AF37;
    text-align:center;
    ">
    <h1 style="color:#D4AF37;">
    🧶 NASIJ STUDIO
    </h1>

    <h3 style="color:white;">
    Smart Carpet Design Platform
    </h3>

    <p style="font-size:24px;color:white;">
    صمم سجادتك بالذكاء الاصطناعي
    </p>

    <p style="color:#cccccc;">
    من صورة • من وصف • أو من الاثنين معاً
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1,col2 = st.columns(2)

    with col1:
        st.button(
            "🚀 ابدأ التصميم",
            use_container_width=True
        )

    with col2:
        st.button(
            "📚 استعرض الكاتالوج",
            use_container_width=True
        )

    st.write("")
    st.subheader("📊 إحصائيات المنصة")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.metric("🎨 التصاميم","1250")

    with c2:
        st.metric("🛒 الطلبات","340")

    with c3:
        st.metric("⭐ العملاء","180")

    st.write("")
    st.subheader("⭐ أحدث التصاميم")

    a,b,c = st.columns(3)

    with a:
        st.info("🏆 سجاد عربي فاخر")

    with b:
        st.info("🏆 سجاد نجدي")

    with c:
        st.info("🏆 سجاد ملكي")

# =========================
# استوديو التصميم
# =========================

elif page == "🎨 استوديو التصميم":

    st.title("🎨 استوديو التصميم")

    uploaded_file = st.file_uploader(
        "📷 ارفع صورة",
        type=["jpg","jpeg","png"]
    )

    description = st.text_area(
        "✍️ وصف التصميم"
    )

    style = st.selectbox(
        "🎨 النمط",
        [
            "عربي",
            "نجدي",
            "إسلامي",
            "مودرن",
            "ملكي"
        ]
    )

    material = st.selectbox(
        "🧶 الخامة",
        list(prices.keys())
    )

    if uploaded_file:
        st.image(
            uploaded_file,
            use_container_width=True
        )

    if st.button("🚀 إنشاء التصميم"):

        st.success("تم إنشاء طلب التصميم بنجاح")

        st.write("### تفاصيل التصميم")

        st.write(f"النمط: {style}")

        st.write(f"الخامة: {material}")

        if description:
            st.write(description)

# =========================
# الخامات
# =========================

elif page == "🧶 الخامات":

    st.title("🧶 الخامات الفاخرة")

    col1,col2 = st.columns(2)

    with col1:
        st.success("""
🧶 بوليستر

80 ريال/م²

اقتصادي وسهل التنظيف
""")

    with col2:
        st.success("""
🧶 نايلون

120 ريال/م²

مقاومة عالية للاستخدام
""")

    st.write("")

    col3,col4 = st.columns(2)

    with col3:
        st.success("""
🧶 صوف طبيعي

220 ريال/م²

فخامة وعزل ممتاز
""")

    with col4:
        st.success("""
🧶 حرير فاخر

450 ريال/م²

أعلى درجات الفخامة
""")

# =========================
# الكاتالوج
# =========================
elif page == "📚 الكاتالوج":

    st.title("📚 كاتالوج نسيج الفاخر")

    st.subheader("🏜️ سجاد الجمل الصحراوي")

    st.image(
        "images/images/ChatGPT Image 7 م 19_37_07 يونيو 2026.png",
        use_container_width=True
    )

    st.markdown("""
    **سلسلة التراث العربي**

    تصميم مستوحى من الجمال العربية
    والصحراء الذهبية والزخارف الإسلامية الفاخرة.
    """)


# =========================
# التسعير
# =========================

elif page == "💰 التسعير":

    st.title("💰 التسعير الذكي")

    material = st.selectbox(
        "الخامة",
        list(prices.keys())
    )

    width = st.number_input(
        "العرض (متر)",
        min_value=1.0,
        value=4.0
    )

    height = st.number_input(
        "الطول (متر)",
        min_value=1.0,
        value=6.0
    )

    area = width * height

    total = area * prices[material]

    st.metric(
        "المساحة",
        f"{area:.2f} م²"
    )

    st.metric(
        "السعر التقديري",
        f"{total:,.0f} ريال"
    )

# =========================
# مشاريع العملاء
# =========================

elif page == "⭐ مشاريع العملاء":

    st.title("⭐ مشاريع العملاء")

    st.info("🏆 مجلس عربي فاخر")

    st.info("🏆 فيلا خاصة")

    st.info("🏆 قاعة استقبال")

    st.info("🏆 فندق فاخر")

# =========================
# التواصل
# =========================

elif page == "📞 التواصل":

    st.title("📞 التواصل")

    name = st.text_input("الاسم")

    phone = st.text_input("رقم الجوال")

    message = st.text_area("الرسالة")

    if st.button("إرسال"):
        st.success("تم إرسال الرسالة بنجاح")

# =========================
# Footer
# =========================

st.markdown("---")
st.caption("© Nasij Studio Premium 2026")
