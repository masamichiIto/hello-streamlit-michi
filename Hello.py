# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    import numpy as np
    np.random.seed(123)
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write('# :balloon: Welcome to Streamlit')

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

    st.write("# Added block")
    st.markdown(
        """
        # TOPIC
        (write some topic here.)  
        (aaaa)  
        (bbbb)
        """
        )
    st.latex('Factor\space model:\space x = \Lambda f + \Psi^{1/2}u')

    import pandas as pd
    import numpy as np
    st.write('## 1. dfを表示する')
    df = pd.DataFrame({
        'first column': [1,2,3,4],
        'second column': [10, 20, 30, 40]
    })

    df # streamlitはこのような形での変数呼び出しをst.write(df)のようにst.write()されたものとして読み替えてくれる

    dataframe = pd.DataFrame(
        np.random.randn(10, 20),
        columns = ['col {}'.format(i) for i in range(20)]
    )
    st.write("st.dataframe ↓")
    st.dataframe(dataframe.style.highlight_max(axis=0))

    st.write('st.table ↓')
    st.table(dataframe)

    st.write("# draw charts and maps")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )
    st.line_chart(chart_data)

    map_data = pd.DataFrame(
        np.random.randn(1000, 2)/[50,50] + [37.76, -122.4],
        columns = ['lat', 'lon']
    )

    st.map(map_data)
    st.write('## 新宿近辺の場合')
    map_data2 = pd.DataFrame(
        np.random.randn(30, 2)/[100,100] + [35.69, 139.70],
        columns = ['lat', 'lon']
    )
    st.map(map_data2)

    st.write('# Widgets')
    x = st.slider('x') # this is a widget
    st.write(x, 'squared is', x * x)

    st.text_input('Your name', key='name')
    
    # we can access the value at any point with:
    st.session_state.name

    st.write('## use checkboxes to show/hide data')
    if st.checkbox('show dataframe'): # 切り替えるたびにdfの値が変わる→チェックボックスのon/offでapp.pyが再読み込みされる
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns = ['a', 'b', 'c']
        )

        chart_data
    
    st.write('## use a selectbox for options')
    df = pd.DataFrame({
        'first column': [1,2,3,4],
        'second column': [10, 20, 30, 40]
    })
    option = st.selectbox(
        'Which number do you like the best?',
        df['first column']
    )

    'you selected: ', option
    '## Layout'
    
    # add a select box to a sidebar
    add_selectbox = st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')
    )
    
    # add a slider to a sidebar
    add_slider = st.sidebar.slider(
        'select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )

    left_column, right_column = st.columns(2)
    # you can use a column just like st.sidebar:
    left_column.button('Press me!')

    # or even better, call streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'sorting hat',
            ('Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin')
        )
        st.write(f'You are in {chosen} house!')

    st.write('## show progress')
    import time

    'starting a long computation...'
    # add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # update the progress bar with each iteration
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i+1)
        time.sleep(0.1)

    '...and now we\'re done!'

    st.write('# Caching')
    st.code(body = """
                    @st.cache_data # streamlitが以下の関数の結果をキャッシュに乗せてくれるようにするデコレータ
                    def  long_running_function(param1, param2):
                        return ...

                    @st.cache_resource # MLモデルやDB connectionのような直列化されていない何度も読み込むのは手間なオブジェクトをキャッシュに乗せる際に利用する
                    ml_model = LogisticRegression(C = 0.8, random_state=123)
                    """,
                    language='python')

if __name__ == "__main__":
    run()
