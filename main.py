import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit')
st.write('Progress Barの表示')

latest_interation = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

expander = st.beta_expander('問い合わせ1')
expander.write('問い合わせ回答')
expander = st.beta_expander('問い合わせ2')
expander.write('問い合わせ回答')
expander = st.beta_expander('問い合わせ3')
expander.write('問い合わせ回答')



# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は',0,100,50)
# 'あなたの趣味',text
# 'コンディション', condition

# st.write('Display Image')

# option = st.selectbox(
#     'あなたが好きな数字を入れてください、',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、',option,'です'

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img,caption = 'AAA', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )

# st.map(df)

# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd

# """