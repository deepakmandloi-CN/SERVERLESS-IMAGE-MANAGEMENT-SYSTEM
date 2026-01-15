# SERVERLESS-IMAGE-MANAGEMENT-SYSTEM
📸 Image Resize & Restore System (AWS + Streamlit + Lambda)

This project provides a complete image resize and restore workflow using Streamlit (UI), AWS S3, and AWS Lambda.

Users can:

Upload an original image → it is resized automatically.

Upload a resized image → the original image is restored automatically.

All processing is event-driven using S3 triggers.

🧩 Architecture Overview User (Streamlit UI) | v Amazon S3 ┌───────────────┐ │ original/ │ ──▶ Lambda (resize) ──▶ resized/ │ resized/ │ ──▶ Lambda (restore) ─▶ restored/ └───────────────┘

📁 S3 Folder Structure deepak-image-scaling/ │ ├── original/ # User uploads original images ├── resized/ # Lambda stores resized images └── restored/ # Lambda restores original images

⚙️ Workflow Logic 🔹 Resize Flow

User uploads original image from Streamlit UI.

Image is stored in original/ folder.

S3 event triggers Lambda.

Lambda:

Reads width and height from metadata.

Resizes the image.

Saves resized image to resized/.

🔹 Restore Flow

User uploads a resized image from Streamlit UI.

Image is stored in resized/.

S3 event triggers Lambda.

Lambda:

Finds the matching image in original/.

Copies it into restored/.

🛠️ Tech Stack

Frontend: Streamlit (Python)

Backend: AWS Lambda (Python 3.10)

Storage: Amazon S3

Image Processing: Pillow (PIL)

Cloud SDK: Boto3

🔐 AWS Requirements 1️⃣ IAM Permissions (Lambda Role) { "Effect": "Allow", "Action": [ "s3:GetObject", "s3:PutObject", "s3:ListBucket" ], "Resource": [ "arn:aws:s3:::deepak-image-scaling", "arn:aws:s3:::deepak-image-scaling/*" ] }

2️⃣ S3 Event Notifications

Configure two triggers on the S3 bucket:

Event Type Prefix Target Lambda PUT original/ resize logic PUT resized/ restore logic

✔️ Use "All object create events"

🧠 Lambda Function Behavior

Triggered automatically by S3 uploads.

No API Gateway required.

Handles both resize and restore in a single function.

🖥️ Streamlit UI Features

Two tabs:

Resize Image (Upload Original)

Restore Image (Upload Resized)

Preview images before upload.

User-defined width & height.

Automatically triggers Lambda via S3 events.

▶️ How to Run Locally 1️⃣ Install Dependencies pip install streamlit boto3 pillow

2️⃣ Configure AWS Credentials aws configure

3️⃣ Run Streamlit App streamlit run app.py

🧪 Testing ✔ Manual Testing

Upload directly to S3 → Lambda triggers correctly.

✔ UI Testing

Upload from Streamlit → S3 event triggers Lambda automatically.

🚨 Common Issues & Fixes Issue Reason Fix Lambda not triggered S3 event missing Configure event notification Restored folder empty Original image missing Ensure same filename exists Timeout error Low memory Increase Lambda memory to 512MB Works manually, not UI File stream read twice Read file only once 🚀 Future Improvements

Image hashing instead of filename mapping

Multiple image formats support

User download links

CloudFront integration

Versioning support

👨‍💻 Author

Deepak Mandloi Cloud & Data Engineering Project Built with ❤️ using AWS & Python
