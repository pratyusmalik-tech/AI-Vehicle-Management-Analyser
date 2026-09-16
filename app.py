import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API Configuration
# Replace "YOUR_API_KEY_HERE" with your actual Google Gemini API key
API_KEY = "AQ.Ab8RN6Lz7bJx8_3fu2Wxm2JZNG0GbLKVL8_K6vAwLlk1Xj6fvw"
genai.configure(api_key=API_KEY)

# 2. Page Configuration
st.set_page_config(
    page_title="Vehicle Damage Analyzer", 
    page_icon="🚗", 
    layout="wide"
)

st.title("🚗 AI Vehicle Damage Analyzer")
st.markdown("Upload a clear photo of a vehicle to instantly analyze visible exterior damage using AI computer vision.")

# 3. System Prompt
SYSTEM_PROMPT = """
You are an AI visual vehicle-inspection assistant.

Analyze the uploaded vehicle image and identify visible exterior damage.

Your analysis must be limited to what can be observed from the image.

Identify:
1. Vehicle type
2. Visible body components
3. Scratches
4. Dents
5. Cracks
6. Broken components
7. Paint damage
8. Misalignment that is visibly apparent
9. Approximate location of each issue
10. Apparent severity

Severity categories:
- Minor
- Moderate
- Severe
- Cannot determine

Also identify:
11. Components that may require professional inspection
12. Potential safety concerns visible from the image

OUTPUT FORMAT:

## 🚗 Vehicle
...

## 🔍 Visible Damage

| Area | Damage Type | Severity | Evidence |
|---|---|---|---|
| | | | |

## ⚠️ Potential Safety Concerns
- ...

## 🔧 Areas Requiring Inspection
- ...

## 📋 Overall Visual Assessment
...

IMPORTANT:
Do not provide a definitive mechanical diagnosis.
Do not estimate repair costs.
Do not claim hidden damage.
Only describe visible evidence.
"""

# 4. Main Application Interface
uploaded_file = st.file_uploader("Upload Vehicle Image (JPG, PNG, JPEG)", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image using the stable container width parameter
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Vehicle Image", use_container_width=True)
    
    # 5. Analysis Trigger
    if st.button("Analyze Damage", type="primary"):
        with st.spinner("AI is analyzing the vehicle using Gemini 3.6 Flash..."):
            try:
                # Pass the prompt and image to the stable Gemini 3.6 Flash model
                model = genai.GenerativeModel('gemini-3.6-flash')
                response = model.generate_content([SYSTEM_PROMPT, image])
                
                # Display results
                st.success("Analysis Complete!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")