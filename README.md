# TELC B2 Mock Exam Generator

A comprehensive system for generating unlimited, balanced mock exams for TELC B2 German language certification preparation.

## Features

✅ **Balanced Difficulty** - Exams blend easy, medium, and hard questions (25% easy, 50% medium, 25% hard)  
✅ **Complete Structure** - All 4 skills: Lesen (Reading), Schreiben (Writing), Hören (Listening), Sprechen (Speaking)  
✅ **Randomized Questions** - Different question sets each time you generate  
✅ **Professional Formatting** - HTML with print-to-PDF capability  
✅ **Detailed Answer Keys** - Separate answer keys with explanations for each answer  
✅ **Easy Deployment** - Ready for Vercel or Netlify  
✅ **Customizable** - Add your own questions to the database  

## Quick Start

### Option 1: Run Locally (Recommended for Testing)

```bash
# Install Python 3.7+
# Navigate to project directory
cd mock-exam-generator

# Install dependencies
pip install -r requirements.txt

# Generate 3 exams
python3 generate_exam.py
```

**Output:** 
- 6 HTML files in `exams/` directory (3 exams + 3 answer keys)
- Open in browser or print to PDF

### Option 2: Deploy to Vercel/Netlify

#### Vercel Deployment

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel
```

**Or use Vercel web interface:**
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Environment: Set Python 3.9
5. Deploy

#### Netlify Deployment

1. Go to [netlify.com](https://netlify.com)
2. Click "Add new site"
3. Select "Import an existing project"
4. Choose your GitHub repository
5. Build command: `python3 generate_exam.py`
6. Publish directory: `web`
7. Deploy

## Directory Structure

```
mock-exam-generator/
├── generate_exam.py          # Main Python script
├── requirements.txt          # Python dependencies
├── package.json             # Node.js configuration
├── vercel.json              # Vercel deployment config
├── README.md                # This file
├── data/
│   └── questions.json       # Question database (edit to add questions)
├── web/
│   └── index.html          # Web interface
├── exams/                   # Generated exams (created after running script)
│   ├── exam_20250616_120000_1.html
│   ├── exam_20250616_120000_1_answers.html
│   └── ...
└── api/                     # Optional: API endpoints (future expansion)
```

## How It Works

### 1. Question Database (`data/questions.json`)

The system stores questions organized by:
- **Section**: lesen, schreiben, horen, sprechen
- **Difficulty**: easy, medium, hard
- **Metadata**: id, source, explanation, answer options

**Example structure:**
```json
{
  "lesen": {
    "easy": [
      {
        "id": "L_E_001",
        "text": "Question text here",
        "options": ["A", "B", "C"],
        "answer": "B",
        "explanation": "Why B is correct...",
        "difficulty": "easy",
        "source": "practice_test_1"
      }
    ]
  }
}
```

### 2. Exam Generation Process

**Step 1:** Load questions from `data/questions.json`  
**Step 2:** For each skill, select balanced questions:
- 25% from easy questions
- 50% from medium questions  
- 25% from hard questions

**Step 3:** Randomly shuffle selected questions (different each generation)  
**Step 4:** Generate HTML files with:
- Professional formatting
- Section headers with time limits
- Print-to-PDF functionality
- Answer keys with explanations

### 3. Output Files

Each exam generation creates:
- **Exam File**: `exam_[timestamp]_[number].html` - The actual exam
- **Answer Key**: `exam_[timestamp]_[number]_answers.html` - Solutions with explanations

## Customization

### Adding Your Own Questions

Edit `data/questions.json` to add more questions:

```json
{
  "lesen": {
    "medium": [
      {
        "id": "L_M_006",
        "text": "Your question text",
        "options": ["Option A", "Option B", "Option C"],
        "answer": "A",
        "explanation": "Detailed explanation of why A is correct",
        "difficulty": "medium",
        "source": "your_source"
      }
    ]
  }
}
```

### Adjusting Difficulty Balance

Edit `generate_exam.py`, line ~40:

```python
# Change this dictionary to adjust difficulty distribution
difficulty_dist = {'easy': 0.25, 'medium': 0.5, 'hard': 0.25}
```

Examples:
- **Easier exams**: `{'easy': 0.4, 'medium': 0.4, 'hard': 0.2}`
- **Harder exams**: `{'easy': 0.15, 'medium': 0.4, 'hard': 0.45}`

### Changing Question Counts

Edit `generate_exam.py` in the `generate_exam()` method:

```python
# Change these numbers to include more/fewer questions per section
exam['sections']['lesen']['questions'] = self._select_balanced_questions('lesen', 20, difficulty_dist)
exam['sections']['schreiben']['questions'] = self._select_balanced_questions('schreiben', 2, difficulty_dist)
exam['sections']['horen']['questions'] = self._select_balanced_questions('horen', 7, difficulty_dist)
exam['sections']['sprechen']['questions'] = self._select_balanced_questions('sprechen', 1, difficulty_dist)
```

## Using Generated Exams

### View in Browser
```bash
# Open the generated HTML file
open exams/exam_*.html
```

### Download as PDF
1. Open exam in browser
2. Click "Print / Download as PDF" button
3. In print dialog, select "Save as PDF"
4. Choose location and filename

### Print Directly
1. Open exam in browser
2. Click "Print / Download as PDF" button
3. Select your printer
4. Print

## API Reference (Python)

### TelcExamGenerator Class

#### Initialize
```python
from generate_exam import TelcExamGenerator

generator = TelcExamGenerator(data_file='data/questions.json')
```

#### Generate Single Exam
```python
exam = generator.generate_exam(exam_number=1)
# Returns: dict with exam structure
```

#### Generate Multiple Exams
```python
exams = generator.generate_multiple_exams(count=5)
# Returns: list of 5 exam dicts
```

#### Export to HTML
```python
html_content = generator.export_exam_to_html(exam, include_answers=True)
# Returns: HTML string
```

#### Save Exam to File
```python
filepath = generator.save_exam(exam, output_dir='exams', include_answers=False)
# Saves HTML file and returns filepath
```

## Deployment Checklist

- [ ] Clone/fork the repository
- [ ] Customize `data/questions.json` with your questions
- [ ] Test locally: `python3 generate_exam.py`
- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Connect to Vercel or Netlify
- [ ] Configure Python version (3.9+)
- [ ] Set build command: `python3 generate_exam.py`
- [ ] Deploy
- [ ] Test generated exams online
- [ ] Share your exam generator URL

## Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### Exams not generating
Check that `data/questions.json` exists and is valid JSON:
```bash
python3 -c "import json; json.load(open('data/questions.json'))"
```

### HTML files won't open
Ensure you're using a modern web browser (Chrome, Firefox, Safari, Edge)

### PDF download not working
Try a different browser. Some browser settings may restrict downloads.

### Questions appearing in every exam
This is normal - the algorithm randomly selects from the pool. To ensure variety:
- Add more questions to `data/questions.json`
- Adjust difficulty distribution if too few medium/hard questions

## Examples

### Generate 3 balanced exams
```bash
python3 generate_exam.py
```

### Generate 10 exams for a class
Modify `main()` function:
```python
exams = generator.generate_multiple_exams(count=10)
```

### Generate with custom difficulty (all medium)
```python
difficulty_dist = {'easy': 0, 'medium': 1.0, 'hard': 0}
```

## Publishing Options

### Share Your Exams

**Option 1: Vercel/Netlify Link**
- Deploy to Vercel/Netlify
- Share deployment URL
- Anyone can generate exams online

**Option 2: GitHub Repository**
- Push to GitHub public repository
- Others can clone and run locally
- Include comprehensive instructions

**Option 3: Downloadable Package**
- Create ZIP with web interface + exams
- Share via email/Drive/Dropbox
- Users open `index.html` in browser

### Monetization (Optional)

If you want to offer premium features:
- Premium question packs
- Detailed progress tracking
- Video explanations
- One-on-one tutoring integration
- Spaced repetition scheduling

## Future Enhancements

- [ ] User accounts and progress tracking
- [ ] Adaptive difficulty based on performance
- [ ] Audio files for listening section
- [ ] Video explanations for answers
- [ ] Mobile app version
- [ ] Spaced repetition scheduler
- [ ] Community question sharing
- [ ] Practice statistics and analytics
- [ ] AI-generated explanations
- [ ] Multiple exam templates

## Support

For issues or questions:
1. Check this README
2. Review the code comments
3. Test with a simple exam generation
4. Check `data/questions.json` for formatting errors

## License

MIT License - Feel free to use, modify, and share!

## Contributing

To improve this tool:
1. Add more questions to `data/questions.json`
2. Improve HTML formatting in `generate_exam.py`
3. Add new features or fix bugs
4. Share feedback and suggestions

---

**Happy studying! Good luck with your TELC B2 exam! 🎓**
