import streamlit as st

# プロジェクト内にpagesフォルダを作成して，その中に.pyファイルを置くだけでページが追加できる！

st.set_page_config(page_title="multiple page example", page_icon="❤️")
st.markdown("""
            # multiple page example
            I just created this page only for trying an example of attaching additional page. 
            """)
st.sidebar.header("my multiple page example")
st.write(
    """This demo shows how to add additional page to main page"""
)