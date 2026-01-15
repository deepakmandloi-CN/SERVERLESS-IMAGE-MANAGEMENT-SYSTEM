import streamlit as st
import boto3
from botocore.exceptions import ClientError

AWS_REGION = "us-east-1"
BUCKET = "deepak-image-scaling"
s3 = boto3.client("s3", region_name=AWS_REGION)

st.set_page_config(page_title="Image Resize & Restore", layout="centered")
st.title(" Image Resize & Restore UI")

tab1, tab2 = st.tabs(["Resize Image (Upload Original)", "Restore Image (Upload Resized)"])

with tab1:
    st.header("Upload ORIGINAL Image → Resize Automatically")
    uploaded_file = st.file_uploader(
        "Choose an image to resize",
        type=["jpg", "jpeg", "png", "webp", "gif"],
        key="original"
    )

    col1, col2 = st.columns(2)
    with col1:
        width = st.number_input("Width (px)", min_value=50, value=300)
    with col2:
        height = st.number_input("Height (px)", min_value=50, value=300)

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Preview Original", use_column_width=True)
        if st.button("Upload & Resize Original"):
            try:

                s3.put_object(
                    Bucket=BUCKET,
                    Key=f"original/{uploaded_file.name}",
                    Body=uploaded_file.read(),
                    ContentType=uploaded_file.type,
                    Metadata={"width": str(width), "height": str(height)}
                )
                st.success(f" Uploaded to original/{uploaded_file.name}\n"
                           f"Lambda will resize it automatically → resized/{uploaded_file.name}")
            except ClientError as e:
                st.error(f"AWS Error: {e}")

with tab2:
    st.header("Upload RESIZED Image → Restore Original Automatically")
    uploaded_file2 = st.file_uploader(
        "Choose a resized image",
        type=["jpg", "jpeg", "png", "webp", "gif"],
        key="resized"
    )

    if uploaded_file2 is not None:
        st.image(uploaded_file2, caption="Preview Resized", use_column_width=True)
        if st.button("Upload & Restore Original"):
            try:
                s3.put_object(
                    Bucket=BUCKET,
                    Key=f"resized/{uploaded_file2.name}",
                    Body=uploaded_file2.read(),
                    ContentType=uploaded_file2.type
                )
                st.success(f" Uploaded to resized/{uploaded_file2.name}\n"
                           f"Lambda will restore the original → restored/{uploaded_file2.name}")
            except ClientError as e:
                st.error(f"AWS Error: {e}")
