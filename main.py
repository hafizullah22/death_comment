import streamlit as st
import pandas as pd

# Set wide layout
st.set_page_config(layout="wide")

# Load CSV
data = pd.read_csv('new_death_comment_4K.csv', encoding='utf-8')

# Title
st.markdown("<h1 style='color:#1877f2;text-align:center;> <a href='https://www.facebook.com/hashtag/sb_qna_2025' style='text-decoration:none;'>মৃত্যুর মুহূর্তে মানুষ কি বুঝতে পারে তার মৃত্যু হচ্ছে?</a></h3>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#1877f2; text-align:center;'><a href='https://www.facebook.com/hashtag/sb_qna_2025' style='text-decoration:none;'>#sb_qna_2025</a></h3>", unsafe_allow_html=True)
# Sort data by likesCount descending


# Select columns
selected_columns = ['profileName','profilePicture', 'text', 'likesCount']
data = data[selected_columns]

# Pagination setup
items_per_page = 30
total_pages = (len(data) - 1) // items_per_page + 1

if 'page_number' not in st.session_state:
    st.session_state.page_number = 1

start_idx = (st.session_state.page_number - 1) * items_per_page
end_idx = start_idx + items_per_page
paginated_data = data.iloc[start_idx:end_idx]

# Inject custom CSS for cards
st.markdown(
    """
    <style>
    
    .card {
        background-color: #f9f9f9;
        padding: 15px 20px;
        margin: 10px 5px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.2s;
    }
    .card:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    }
    .profileName {
        font-weight: 700;
        font-size: 1.2rem;
        color: #2c3e50;
        margin-bottom: 5px;
        text-align:center;
    }
    
    
    .likes {
        font-weight: 600;
        color: #ff0000;
        margin-bottom: 10px;
        text-align:center;
    }
   
    .text {
        font-size: 1rem;
        color: #34495e;
        white-space: pre-wrap;
        line-height: 1.4;
        
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display data in 3 columns per row with card style
for i in range(0, len(paginated_data), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(paginated_data):
            row = paginated_data.iloc[i + j]
            with cols[j]:
                st.markdown(
                    f"""
                    <div class="card">
                        <div class="profileName">{row['profileName']}</div>   
                     <div style="text-align:center; margin-bottom:10px;">
                            <img src="{row['profilePicture']}" alt="Profile Image" style="width:50px; height:50px; border-radius:50%; object-fit:cover;">
                        </div>
                        <div class="likes">  {row['likesCount']} Reactions</div>
                        <div style="text-align:justify; color:#333;">
                            {row['text']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# Pagination controls at bottom with styling
col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅️ আগের পৃষ্ঠা"):
        if st.session_state.page_number > 1:
            st.session_state.page_number -= 1

with col2:
    st.markdown(
        f"<div style='text-align:center; font-weight:bold; font-size:1.1rem;'>পৃষ্ঠা: {st.session_state.page_number} / {total_pages}</div>",
        unsafe_allow_html=True,
    )

with col3:
    if st.button("➡️ পরের পৃষ্ঠা"):
        if st.session_state.page_number < total_pages:
            st.session_state.page_number += 1


st.text("একান্তাই আমার ইচ্ছা")