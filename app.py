import streamlit as st
from deep_translator import GoogleTranslator

# --- 初始化 ---
# 设置页面配置（标题、图标、布局）
st.set_page_config(
    page_title="专属免费翻译工具",
    page_icon="🌐",
)

# 初始化翻译器实例
translator = GoogleTranslator(source='auto', target='ru')

# 语言列表
lang_list = ["russian", "english", "chinese (simplified)", "japanese", "korean"]

# --- 界面布局 ---
st.title("🌐 你的专属免费翻译工具")
st.markdown("---")

# 创建两列布局：左侧为输入，右侧为输出
col1, col2 = st.columns(2)

with col1:
    st.subheader("源语言")
    src_lang_name = st.selectbox("选择输入语言：", ["auto"] + lang_list, index=0)
    input_text = st.text_area("在此输入需要翻译的文本：", height=300, placeholder="Start typing...")

with col2:
    st.subheader("目标语言")
    try:
        default_dest_index = lang_list.index("russian")
    except ValueError:
        default_dest_index = 0
    dest_lang_name = st.selectbox("选择目标语言：", lang_list, index=default_dest_index)

    # 翻译
