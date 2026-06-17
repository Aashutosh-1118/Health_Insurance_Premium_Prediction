import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Cost Predictor", page_icon="🏥", layout="wide")

st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
    }
    .main .block-container {
        padding-top: 1.5rem;
        max-width: 1100px;
    }
    .app-header {
        background: linear-gradient(90deg, #0f2545 0%, #1d4e89 100%);
        padding: 2rem 2.5rem;
        border-radius: 12px;
        margin-bottom: 1.8rem;
        color: white;
    }
    .app-header h1 {
        margin: 0;
        font-size: 2rem;
        color: white;
    }
    .app-header p {
        margin: 0.4rem 0 0 0;
        color: #d6e2f0;
        font-size: 0.95rem;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #1a1f2b;
        border: 1px solid #2a3140;
        border-radius: 10px;
        padding: 0.5rem 1rem;
    }
    h3 {
        color: #e8edf5 !important;
    }
    label, .stMarkdown p {
        color: #c9d2e0 !important;
    }
    div.stButton > button[kind="primary"] {
        background-color: #1d4e89;
        border: none;
        color: white;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #2f6bb3;
    }
</style>

<div class="app-header">
    <h1>🏥 Health Insurance Cost Predictor</h1>
    <p>Get an instant, data-driven estimate of your health insurance premium based on age, lifestyle, and medical history.</p>
</div>
""", unsafe_allow_html=True)

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

st.subheader('👤 Personal Information')
personal_box = st.container(border=True)
with personal_box:
    row1 = st.columns(3)
    with row1[0]:
        age = st.number_input('Age', min_value=18, step=1, max_value=100)
    with row1[1]:
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with row1[2]:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])

    row2 = st.columns(3)
    with row2[0]:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
    with row2[1]:
        region = st.selectbox('Region', categorical_options['Region'])
    with row2[2]:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

st.write("")

st.subheader('🩺 Health Information')
health_box = st.container(border=True)
with health_box:
    row3 = st.columns(3)
    with row3[0]:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
    with row3[1]:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with row3[2]:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

    row4 = st.columns(3)
    with row4[0]:
        genetical_risk = st.number_input('Genetical Risk (0-5)', step=1, min_value=0, max_value=5)

st.write("")

st.subheader('💼 Financial & Policy Information')
financial_box = st.container(border=True)
with financial_box:
    row5 = st.columns(3)
    with row5[0]:
        income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)
    with row5[1]:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])

st.write("")

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    predict_clicked = st.button('🔍 Predict Premium', use_container_width=True, type="primary")

if predict_clicked:
    prediction = predict(input_dict)
    st.divider()
    st.success(f'Predicted Health Insurance Cost: ₹{prediction:,}')
# import streamlit as st
# from prediction_helper import predict

# st.set_page_config(page_title="Health Insurance Cost Predictor", page_icon="🏥", layout="wide")

# st.title('🏥 Health Insurance Cost Predictor')
# st.caption('Enter your details below to get an estimated health insurance premium based on a machine learning model.')

# st.divider()

# categorical_options = {
#     'Gender': ['Male', 'Female'],
#     'Marital Status': ['Unmarried', 'Married'],
#     'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
#     'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
#     'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
#     'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
#     'Medical History': [
#         'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
#         'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
#         'Diabetes & Heart disease'
#     ],
#     'Insurance Plan': ['Bronze', 'Silver', 'Gold']
# }

# st.subheader('👤 Personal Information')
# row1 = st.columns(3)
# with row1[0]:
#     age = st.number_input('Age', min_value=18, step=1, max_value=100)
# with row1[1]:
#     gender = st.selectbox('Gender', categorical_options['Gender'])
# with row1[2]:
#     marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])

# row2 = st.columns(3)
# with row2[0]:
#     number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
# with row2[1]:
#     region = st.selectbox('Region', categorical_options['Region'])
# with row2[2]:
#     employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

# st.divider()

# st.subheader('🩺 Health Information')
# row3 = st.columns(3)
# with row3[0]:
#     bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
# with row3[1]:
#     smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
# with row3[2]:
#     medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# row4 = st.columns(3)
# with row4[0]:
#     genetical_risk = st.number_input('Genetical Risk (0-5)', step=1, min_value=0, max_value=5)

# st.divider()

# st.subheader('💼 Financial & Policy Information')
# row5 = st.columns(3)
# with row5[0]:
#     income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)
# with row5[1]:
#     insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])

# st.divider()

# # Create a dictionary for input values
# input_dict = {
#     'Age': age,
#     'Number of Dependants': number_of_dependants,
#     'Income in Lakhs': income_lakhs,
#     'Genetical Risk': genetical_risk,
#     'Insurance Plan': insurance_plan,
#     'Employment Status': employment_status,
#     'Gender': gender,
#     'Marital Status': marital_status,
#     'BMI Category': bmi_category,
#     'Smoking Status': smoking_status,
#     'Region': region,
#     'Medical History': medical_history
# }

# col1, col2, col3 = st.columns([1, 1, 1])
# with col2:
#     predict_clicked = st.button('🔍 Predict Premium', use_container_width=True, type="primary")

# if predict_clicked:
#     prediction = predict(input_dict)
#     st.divider()
#     st.success(f'Predicted Health Insurance Cost: ₹{prediction:,}')

