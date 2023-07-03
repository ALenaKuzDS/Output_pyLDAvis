from streamlit import components

with open('data/lda.html', 'r') as f:
    html_string = f.read()
left, middle, right = stl.columns((2, 5, 2))
with middle:
components.v1.html(html_string, width=1024 , height=768, scrolling=False)


