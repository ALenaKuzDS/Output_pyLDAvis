from streamlit import components
with open('data/lda.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=1600, height=720, scrolling=False)


