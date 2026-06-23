import os

# 1. Define the updated HTML template for Milestone 3 (Options A & B completed)
html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    @page {
        size: A4;
        margin: 18mm 15mm;
        background-color: #f4f7f6;
        @bottom-right { content: "Page " counter(page) " of " counter(pages); font-family: Arial; font-size: 8pt; color: #718096; }
        @bottom-left { content: "🌲 PFI-LMS Project Ledger v2"; font-family: Arial; font-size: 8pt; color: #718096; }
    }
    body { font-family: Arial, sans-serif; color: #2d3748; line-height: 1.5; font-size: 10.5pt; }
    .header-banner { background-color: #1a4332; color: #ffffff; margin: -18mm -15mm 25px -15mm; padding: 25px 15mm; border-bottom: 4px solid #2f855a; }
    .header-banner h1 { margin: 0; font-size: 20pt; }
    .status-badge { display: inline-block; background-color: #c6f6d5; color: #22543d; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 9pt; margin-bottom: 20px; }
    h2 { color: #1a4332; font-size: 14pt; border-left: 4px solid #2f855a; padding-left: 10px; margin-top: 25px; }
    .card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 15px; margin-bottom: 15px; }
    pre { background-color: #1a202c; color: #edf2f7; padding: 12px; border-radius: 6px; font-size: 9pt; white-space: pre-wrap; word-wrap: break-word; font-family: monospace; }
    .highlight { font-weight: 600; color: #2f855a; }
</style>
</head>
<body>
<div class="header-banner">
    <h1>🌲 Pakistan Forest Institute (PFI) LMS Tracker</h1>
    <p>Backend System Infrastructure & Cloud Database Architecture Ledger</p>
</div>
<div class="status-badge">[STATUS] Milestone 3 Achieved Successfully (Option A & B Verified)</div>
<p>This architectural ledger outlines the exact state of your backend application developed for the PFI-LMS.</p>

<h2>🚀 1. Milestone Achievements Realized Today</h2>
<div class="card">
    <ul>
        <li><span class="highlight">Cloud Database Provisioning (Option A):</span> Deployed a zero-cost production cluster on MongoDB Atlas running on AWS. Connected securely via <code>src/config/db.js</code>.</li>
        <li><span class="highlight">User Blueprint Schema Definition (Option B):</span> Created the data modeling template layer inside <code>src/models/User.js</code> to handle unified login parameters separating <code>admin</code>, <code>instructor</code>, and <code>trainee</code> account tiers.</li>
        <li><span class="highlight">Runtime Compile Verification:</span> Successfully verified system startup execution via terminal with active environment variable injections.</li>
    </ul>
</div>

<h2>📂 2. Current Directory & File System Map</h2>
<pre>D:\python\PFI-LMS\\backend/
├── src/
│   ├── config/
│   │   └── db.js         [ACTIVE] -> Handles async MongoDB connections
│   ├── models/
│   │   └── User.js       [ACTIVE] -> Dynamic core schema for roles mapping
│   ├── controllers/      (Empty -> Targeted for secure Authentication handlers)
│   ├── middleware/       (Empty -> Reserved for JWT verification guards)
│   └── routes/           (Empty -> Reserved for routing gateways)
├── .env                  [ACTIVE] -> Secure environmental key store
└── server.js             [ACTIVE] -> Main central application engine runtime
</pre>

<h2>📄 3. Production Source Code Repository State</h2>
<h3>File Path: <code>backend/.env</code></h3>
<pre>PORT=5000\nMONGO_URI=mongodb+srv://abdurrehman03175026_db_user:yOkgDwV0G9HMfG6P@cluster0.5dmvigr.mongodb.net/pfiLMS?retryWrites=true&w=majority&appName=Cluster0</pre>

<h3>File Path: <code>backend/src/models/User.js</code></h3>
<pre>const mongoose = require('mongoose');\nconst UserSchema = new mongoose.Schema({\n    name: { type: String, required: true, trim: true },\n    email: { type: String, required: true, unique: true, lowercase: true, trim: true },\n    password: { type: String, required: true, minlength: 6 },\n    role: { type: String, enum: ['admin', 'instructor', 'trainee'], default: 'trainee' }\n}, { timestamps: true });\nmodule.exports = mongoose.model('User', UserSchema);</pre>
</body>
</html>
"""

# 2. Save the HTML asset locally
with open("temp_checkpoint.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# 3. Use WeasyPrint library to compile it directly to PDF
try:
    from weasyprint import HTML
    HTML("temp_checkpoint.html").write_pdf("PFI_LMS_Project_Updated_Checkpoint.pdf")
    print("\\n[SUCCESS] Your updated PDF file 'PFI_LMS_Project_Updated_Checkpoint.pdf' was created perfectly in this folder!")
except ImportError:
    print("\\n[NOTE] Installing 'weasyprint' library first to compile the PDF...")
    os.system("pip install weasyprint")
    from weasyprint import HTML
    HTML("temp_checkpoint.html").write_pdf("PFI_LMS_Project_Updated_Checkpoint.pdf")
    print("\\n[SUCCESS] Your updated PDF file has been generated successfully!")