
import streamlit as st
from deep_translator import GoogleTranslator
from PIL import Image
import pytesseract
import io

st.set_page_config(page_title="Ozon商品图批量转俄文", page_icon="📸", layout="wide")
translator = GoogleTranslator(source="zh-CN", target="ru")
pytesseract.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'

st.title("📸 Ozon商品图批量转俄文工具")
st.markdown("一次上传多张带中文的商品图，自动识别并批量翻译成俄文")
st.markdown("---")

# 开启批量上传功能
uploaded_imgs = st.file_uploader("批量上传商品图片", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_imgs:
    st.success(f"已上传{len(uploaded_imgs)}张图片，正在处理...")
    for idx, img_file in enumerate(uploaded_imgs, 1):
        st.markdown(f"### 第{idx}张图片处理结果")
        img_byte = io.BytesIO(img_file.read())
        raw_img = Image.open(img_byte)
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("原图与识别文本")
            st.image(raw_img, use_column_width=True)
            extracted_text = pytesseract.image_to_string(raw_img, lang="chi_sim")
            st.text_area(f"第{idx}张图的中文文本", value=extracted_text, height=200)
        
        with col2:
            st.subheader("俄文翻译结果")
            if extracted_text.strip():
                with st.spinner(f"正在翻译第{idx}张图..."):
                    try:
                        ru_text = translator.translate(extracted_text)
                        st.success(f"第{idx}张图翻译完成")
                        st.text_area(f"第{idx}张图的俄文文案", value=ru_text, height=200)
                    except Exception as e:
                        st.error(f"第{idx}张图翻译失败：{str(e)}")
            else:
                st.warning(f"第{idx}张图未识别到有效中文")
        st.markdown("---")

st.markdown("<div style='text-align:center; color:#666;'>支持批量上传 | 自动识别中文并生成俄文商品文案</div>", unsafe_allow
