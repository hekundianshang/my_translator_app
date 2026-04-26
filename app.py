import streamlit as st
from deep_translator import GoogleTranslator

# --- 初始化 ---
# 设置页面配置（标题、图标、布局）
st.set_page_config(
    page_title="专属免费翻译工具",
    page_icon="🌐",
  translator = GoogleTranslator (source='auto', target='ru')
)

# 初始化翻译器实例
translator = GoogleTranslator (source='auto', target='ru')

# 将语言字典转换为列表，用于下拉菜单选择


# --- 界面布局 ---
st.title("🌐 你的专属免费翻译工具")
st.markdown("---")

# 创建两列布局：左侧为输入，右侧为输出
col1, col2 = st.columns(2)

with col1:
    st.subheader("源语言")
    # 源语言选择，默认为 "自动检测"
    src_lang_name = st.selectbox("选择输入语言：", ["auto"] + lang_list, index=0)
    
    # 文本输入区域
    input_text = st.text_area("在此输入需要翻译的文本：", height=300, placeholder="Start typing...")

with col2:
    st.subheader("目标语言")
    # 目标语言选择，默认为 "简体中文"
    try:
        default_dest_index = lang_list.index("russian)")
    except ValueError:
        default_dest_index = 0
    dest_lang_name = st.selectbox("选择目标语言：", lang_list, index=default_dest_index)
    
    # 翻译逻辑
    output_text = ""
    if st.button("开始翻译", type="primary") and input_text:
        with st.spinner("正在翻译中..."):
            try:
              result = translator.translate(input_text)
            output_text = result
                st.success("翻译完成！")
            except Exception as e:
                st.error(f"翻译出错，请重试。错误信息: {e}")
                output_text = ""

    # 翻译结果显示区域
    st.text_area("翻译结果：", value=output_text, height=300, key="output_area")

# --- 页脚 ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <p>powered by googletrans-free API</p>
        <p>仅供个人参考使用</p>
    </div>
    """,
    unsafe_allow_html=True
)
