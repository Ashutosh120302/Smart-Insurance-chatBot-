# Smart-Insurance-chatBot-
 **🧾 Smart Medical Claim Approval Bot**

This project is an intelligent end-to-end system that automates the process of analyzing and approving medical claim invoices using OCR, NLP, and machine learning. Users can upload scanned or digital invoice images, which are processed using **pytesseract** to extract key textual information such as the **invoice amount, patient name, and billing date**.

The extracted features are then passed to a pre-trained **machine learning model** (e.g., Random Forest) that predicts whether the medical claim should be **approved or rejected** based on learned patterns. A simple **chatbot interface built with Streamlit** interacts with users, showing extracted data and providing real-time approval decisions, making the claim assessment process faster, more accurate, and user-friendly.


