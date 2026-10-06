import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="College List",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎓 College List Search")
st.write(
    "Search and filter colleges based on location, course, "
    "fees and other details."
)

st.divider()

# --------------------------------------------------
# COLLEGE DATA
# --------------------------------------------------

college_data = [
    {
        "College Name": "Indian Institute of Science",
        "Location": "Bengaluru, Karnataka",
        "Course": "Engineering / Science",
        "Fees": "Varies by course",
        "Rating": 4.8,
        "Website": "https://iisc.ac.in/"
    },
    {
        "College Name": "National Institute of Technology Karnataka",
        "Location": "Surathkal, Karnataka",
        "Course": "Engineering",
        "Fees": "Varies by course",
        "Rating": 4.6,
        "Website": "https://www.nitk.ac.in/"
    },
    {
        "College Name": "Visvesvaraya Technological University",
        "Location": "Belagavi, Karnataka",
        "Course": "Engineering",
        "Fees": "Varies by course",
        "Rating": 4.4,
        "Website": "https://vtu.ac.in/"
    },
    {
        "College Name": "Christ University",
        "Location": "Bengaluru, Karnataka",
        "Course": "Engineering / Management / Science",
        "Fees": "Varies by course",
        "Rating": 4.5,
        "Website": "https://christuniversity.in/"
    },
    {
        "College Name": "Bangalore Institute of Technology",
        "Location": "Bengaluru, Karnataka",
        "Course": "Engineering",
        "Fees": "Varies by course",
        "Rating": 4.2,
        "Website": "https://bit-bangalore.edu.in/"
    },
    {
        "College Name": "Manipal Institute of Technology",
        "Location": "Manipal, Karnataka",
        "Course": "Engineering",
        "Fees": "Varies by course",
        "Rating": 4.5,
        "Website": "https://www.manipal.edu/mit.html"
    }
]

# --------------------------------------------------
# DATAFRAME
# --------------------------------------------------

df = pd.DataFrame(college_data)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("🔍 Search College")

college_search = st.sidebar.text_input(
    "College Name"
)

location_search = st.sidebar.text_input(
    "Location"
)

course_options = [
    "All Courses"
] + sorted(df["Course"].unique().tolist())

course = st.sidebar.selectbox(
    "Select Course",
    course_options
)

# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------

result = df.copy()

if college_search:
    result = result[
        result["College Name"].str.contains(
            college_search,
            case=False,
            na=False
        )
    ]

if location_search:
    result = result[
        result["Location"].str.contains(
            location_search,
            case=False,
            na=False
        )
    ]

if course != "All Courses":
    result = result[
        result["Course"] == course
    ]

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Colleges Found",
        len(result)
    )

with col2:
    st.metric(
        "Locations",
        result["Location"].nunique()
    )

with col3:
    st.metric(
        "Courses",
        result["Course"].nunique()
    )

st.divider()

# --------------------------------------------------
# DISPLAY COLLEGES
# --------------------------------------------------

st.subheader("🏫 College List")

if len(result) > 0:

    display_data = result.drop(
        columns=["Website"]
    )

    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning(
        "No colleges found for your search."
    )

# --------------------------------------------------
# INDIVIDUAL COLLEGE DETAILS
# --------------------------------------------------

if len(result) > 0:

    st.divider()

    st.subheader("🔎 College Details")

    selected_college = st.selectbox(
        "Select College",
        result["College Name"].unique()
    )

    selected = result[
        result["College Name"] == selected_college
    ].iloc[0]

    st.markdown(
        f"### 🎓 {selected['College Name']}"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            "**Location:**",
            selected["Location"]
        )

        st.write(
            "**Course:**",
            selected["Course"]
        )

        st.write(
            "**Fees:**",
            selected["Fees"]
        )

    with col2:

        st.write(
            "**Rating:**",
            selected["Rating"]
        )

    st.link_button(
        "🌐 Visit College Website",
        selected["Website"]
    )

# --------------------------------------------------
# DOWNLOAD
# --------------------------------------------------

st.divider()

st.subheader("📥 Download College List")

csv_data = result.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download College Data",
    data=csv_data,
    file_name="college_list.csv",
    mime="text/csv"
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "College information is provided for educational purposes. "
    "Verify current courses, fees and admission details "
    "with the respective college."
)
