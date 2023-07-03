from streamlit import components
with open('data/lda.html', 'r') as f:
    html_string = f.read()
components.v1.html(html_string, width=1366, height=800, scrolling=False)

