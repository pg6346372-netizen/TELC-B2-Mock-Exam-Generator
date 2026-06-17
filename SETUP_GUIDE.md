# TELC B2 Mock Exam Generator - Setup & Deployment Guide

## ✅ What You Have Now

Your complete mock exam generator system is ready with:

- ✅ **3 Pre-Generated Sample Exams** (exam_*.html)
- ✅ **3 Corresponding Answer Keys** (exam_*_answers.html)  
- ✅ **Python Script** for unlimited exam generation
- ✅ **Web Interface** (web/index.html)
- ✅ **Question Database** (data/questions.json) with 80+ questions
- ✅ **Deployment Ready** (vercel.json, package.json configured)
- ✅ **Complete Documentation** (README.md)

---

## 🚀 Quick Start (3 Steps)

### Step 1: Test Locally
```bash
cd mock-exam-generator
python3 generate_exam.py
```
This creates 3 new exams in the `exams/` folder. Open any HTML file in your browser.

### Step 2: Generate New Exams Anytime
```bash
python3 generate_exam.py
```
Run this command whenever you want new exams. Each run creates different question sets!

### Step 3: Deploy to Vercel/Netlify
[See Deployment Section Below](#-deploy-to-vercel-or-netlify)

---

## 📂 File Structure Explained

```
mock-exam-generator/
├── generate_exam.py           # ⭐ Run this to generate exams
├── README.md                  # Full documentation
├── SETUP_GUIDE.md            # This file
│
├── data/
│   └── questions.json        # 📚 Question database (edit to add your questions)
│
├── web/
│   └── index.html            # 🌐 Web interface
│
├── exams/
│   ├── exam_*.html           # 📄 Generated exams (print-ready)
│   └── exam_*_answers.html   # 📋 Answer keys with explanations
│
├── requirements.txt          # Python dependencies
├── package.json              # Node.js config
├── vercel.json              # Vercel deployment config
└── .gitignore               # Git ignore settings
```

---

## 💻 Local Usage (Your Computer)

### Installation

```bash
# Ensure Python 3.7+ is installed
python3 --version

# Navigate to project
cd mock-exam-generator

# Install dependencies
pip install -r requirements.txt
```

### Generate Exams

```bash
# Generate 3 exams (default)
python3 generate_exam.py

# Output: 6 HTML files in exams/ folder
# - exam_[timestamp]_1.html (exam 1)
# - exam_[timestamp]_1_answers.html (answer key 1)
# - exam_[timestamp]_2.html (exam 2)
# - exam_[timestamp]_2_answers.html (answer key 2)
# - exam_[timestamp]_3.html (exam 3)
# - exam_[timestamp]_3_answers.html (answer key 3)
```

### View & Download as PDF

1. Open HTML file in browser: `open exams/exam_*.html`
2. Click "Print / Download as PDF" button
3. Save as PDF

### Customize Questions

Edit `data/questions.json` to add your own questions:

```json
{
  "lesen": {
    "medium": [
      {
        "id": "L_M_999",
        "text": "Your question here",
        "options": ["Option A", "Option B", "Option C"],
        "answer": "B",
        "explanation": "Why B is correct...",
        "difficulty": "medium",
        "source": "your_exam"
      }
    ]
  }
}
```

After editing, run `python3 generate_exam.py` again to include new questions.

---

## 🌐 Deploy to Vercel or Netlify

### Option A: Deploy to Vercel (Recommended)

#### Method 1: Using GitHub (Easiest)

1. Create GitHub account at github.com
2. Create new repository (name it `telc-b2-mock-exam-generator`)
3. Push your files to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: TELC B2 Mock Exam Generator"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/telc-b2-mock-exam-generator
   git push -u origin main
   ```

4. Go to [vercel.com](https://vercel.com)
5. Click "Add New Project"
6. Import your GitHub repository
7. Select Python as framework
8. Deploy!

#### Method 2: Using Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy from project directory
cd mock-exam-generator
vercel
```

### Option B: Deploy to Netlify

1. Push to GitHub (same as above)
2. Go to [netlify.com](https://netlify.com)
3. Click "New site from Git"
4. Select GitHub repository
5. Build settings:
   - Build command: `python3 generate_exam.py`
   - Publish directory: `web`
6. Deploy!

### Option C: Deploy to Heroku (Free Alternative)

```bash
# Install Heroku CLI
brew install heroku/brew/heroku

# Login
heroku login

# Create app
heroku create your-app-name

# Deploy
git push heroku main

# View
heroku open
```

---

## 📊 Exam Structure Breakdown

### Each Generated Exam Includes:

**LESEN (Reading)** - 45 minutes
- 20 questions (mix of easy/medium/hard)
- Multiple choice and matching formats
- Real-world professional texts

**SCHREIBEN (Writing)** - 60 minutes
- 2 writing tasks
- Email, letter, or proposal writing
- Professional communication scenarios

**HÖREN (Listening)** - 30 minutes
- 7 listening comprehension tasks
- Conversations, presentations, announcements
- Multiple choice and completion formats

**SPRECHEN (Speaking)** - 15 minutes
- 1 presentation topic
- 2-4 minutes speaking time
- Real-world business scenarios

**Total Time:** ~3.5 hours

---

## 🎯 Tips for Best Results

### For Exam Generation
- Run `python3 generate_exam.py` multiple times to get different question sets
- Start with "easy" exams, progress to "hard"
- Use answer keys to understand explanations

### For Deployment
- Keep GitHub repository up-to-date
- Share Vercel/Netlify link with others
- Monitor analytics to see exam usage

### For Question Database
- Add 5-10 questions per week to expand database
- Focus on areas you find difficult
- Include real exam questions from TELC
- Write detailed explanations for each answer

---

## 🔧 Troubleshooting

### Problem: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Problem: Empty exams folder
```bash
# Ensure data/questions.json exists and is valid
cat data/questions.json | python3 -m json.tool
```

### Problem: Vercel deployment fails
- Check Python version: 3.9+
- Verify `requirements.txt` exists
- Check `vercel.json` configuration
- Review Vercel build logs

### Problem: Questions not appearing
- Verify `data/questions.json` is valid JSON
- Check section names: lesen, schreiben, horen, sprechen
- Check difficulty levels: easy, medium, hard
- Restart Python script

---

## 📈 Publishing Your Exams

### Share Your Vercel Link
```
https://your-app.vercel.app/
```
Anyone with this link can generate exams!

### Create a Promo Link
Share on:
- Social media (Twitter, LinkedIn, Facebook)
- Email lists
- Language learning forums
- Study groups
- Your website/blog

### GitHub Repository
Make it public so others can fork and customize:
```
https://github.com/YOUR_USERNAME/telc-b2-mock-exam-generator
```

---

## 🎓 Next Steps

1. **Test Locally** - Generate 3 exams and review them
2. **Customize Questions** - Add your own questions to data/questions.json
3. **Deploy** - Choose Vercel or Netlify
4. **Share** - Tell others about your exam generator
5. **Expand** - Add more questions and features over time

---

## 📞 Support Resources

- **Full Docs**: See README.md
- **Python Script**: generate_exam.py has detailed comments
- **Question Format**: See data/questions.json for examples
- **Web Interface**: web/index.html is HTML/CSS/JavaScript

---

## ✨ You're All Set!

Your TELC B2 Mock Exam Generator is ready to use. 

**Next command to run:**
```bash
python3 generate_exam.py
```

Good luck with your exam preparation! 🎓📚

