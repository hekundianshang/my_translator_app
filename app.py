import streamlit as st
from deep_translator import GoogleTranslator
from PIL import Image
import pytesseract
import io

# 页面配置
st.set_page_config(page_title="Ozon商品图转俄文工具", page_icon="📸", layout="wide")
# 初始化翻译器，固定目标语言为俄语
translator = GoogleTranslator(source="zh-CN", target="ru")
# 配置Tesseract路径适配Streamlit Cloud
pytesseract.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'

st.title("📸 Ozon商品图文字转俄文工具")
st.markdown("上传带中文的商品图，自动识别并翻译成俄文")
st.markdown("---")

# 图片上传模块
uploaded_img = st.file_uploader("上传商品图片", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

if uploaded_img:
    # 读取并展示图片
    img_byte = io.BytesIO(uploaded_img.read())
    raw_img = Image.open(img_byte)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("原图识别结果")
        st.image(raw_img, use_column_width=True)
        # 识别图片中的中文
        extracted_text = pytesseract.image_to_string(raw_img, lang="chi_sim")
        st.text_area("提取的中文文本", value=extracted_text, height=300)
    
    with col2:
        st.subheader("俄文翻译结果")
        if extracted_text.strip():
            with st.spinner("正在翻译..."):
                try:
                    ru_text = translator.translate(extracted_text)
                    st.success("翻译完成")
                    st.text_area("可直接复制到Ozon", value=ru_text, height=300)
                except Exception as e:
                    st.error(f"翻译失败：{str(e)}")
        else:
            st.warning("未从图片中识别到有效中文，请尝试上传更清晰的图片")

# 页脚说明
st.markdown("---")
st.markdown("<div style='text-align:center; color:#666;'>专为Ozon卖家优化 | 支持中文印刷体识别</div>", unsafe_allow_html=True)
