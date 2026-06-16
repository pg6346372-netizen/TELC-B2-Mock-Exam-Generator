#!/usr/bin/env python3
"""
TELC B2 Mock Exam Generator
Generates balanced, randomized mock exams from question database
"""

import json
import random
import os
from datetime import datetime
from pathlib import Path

class TelcExamGenerator:
    def __init__(self, data_file='data/questions.json'):
        self.data_file = data_file
        self.questions = self._load_questions()
        self.exam_count = 0

    def _load_questions(self):
        """Load questions from JSON data file"""
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Questions data file not found: {self.data_file}")

        with open(self.data_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _select_balanced_questions(self, section, count, difficulty_distribution):
        """
        Select balanced questions by difficulty
        difficulty_distribution: dict like {'easy': 0.3, 'medium': 0.4, 'hard': 0.3}
        """
        section_questions = self.questions.get(section, {})
        selected = []

        for difficulty, ratio in difficulty_distribution.items():
            available = section_questions.get(difficulty, [])
            if available:
                num_to_select = max(1, int(count * ratio))
                selected.extend(random.sample(available, min(num_to_select, len(available))))

        return selected[:count]

    def generate_exam(self, exam_number=None):
        """Generate a single balanced mock exam"""
        if exam_number is None:
            self.exam_count += 1
            exam_number = self.exam_count

        exam = {
            'exam_id': f"exam_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{exam_number}",
            'exam_number': exam_number,
            'generated_date': datetime.now().isoformat(),
            'sections': {}
        }

        # Balanced difficulty distribution (not too easy, not too hard)
        difficulty_dist = {'easy': 0.25, 'medium': 0.5, 'hard': 0.25}

        # LESEN: 20 questions (roughly from document)
        exam['sections']['lesen'] = {
            'title': 'LESEN (Reading)',
            'time_minutes': 45,
            'questions': self._select_balanced_questions('lesen', 20, difficulty_dist)
        }

        # SCHREIBEN: 2 writing tasks
        exam['sections']['schreiben'] = {
            'title': 'SCHREIBEN (Writing)',
            'time_minutes': 60,
            'questions': self._select_balanced_questions('schreiben', 2, difficulty_dist)
        }

        # HÖREN: 6-8 listening questions
        exam['sections']['horen'] = {
            'title': 'HÖREN (Listening)',
            'time_minutes': 30,
            'questions': self._select_balanced_questions('horen', 7, difficulty_dist)
        }

        # SPRECHEN: 1 speaking task
        exam['sections']['sprechen'] = {
            'title': 'SPRECHEN (Speaking)',
            'time_minutes': 15,
            'questions': self._select_balanced_questions('sprechen', 1, difficulty_dist)
        }

        return exam

    def generate_multiple_exams(self, count=3):
        """Generate multiple balanced exams"""
        exams = []
        for i in range(1, count + 1):
            exams.append(self.generate_exam(i))
        return exams

    def export_exam_to_html(self, exam, include_answers=False):
        """Generate HTML representation of exam"""
        html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TELC B2 Mock Exam {exam['exam_number']}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
            background-color: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        header {{
            text-align: center;
            border-bottom: 3px solid #0066cc;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        h1 {{
            color: #0066cc;
            margin: 0 0 10px 0;
        }}
        .exam-info {{
            color: #666;
            font-size: 14px;
        }}
        .section {{
            margin: 40px 0;
            page-break-inside: avoid;
        }}
        .section-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #0066cc;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        .section-header h2 {{
            margin: 0;
            color: #0066cc;
            font-size: 20px;
        }}
        .time-badge {{
            background-color: #0066cc;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: bold;
        }}
        .question {{
            margin: 20px 0;
            padding: 15px;
            border-left: 4px solid #0066cc;
            background-color: #f9f9f9;
        }}
        .question-number {{
            font-weight: bold;
            color: #0066cc;
            margin-bottom: 10px;
        }}
        .question-text {{
            margin: 10px 0;
        }}
        .options {{
            margin-top: 15px;
            padding-left: 20px;
        }}
        .option {{
            margin: 8px 0;
        }}
        .answer-key {{
            background-color: #e8f4f8;
            border-left: 4px solid #00a86b;
            padding: 10px;
            margin-top: 10px;
        }}
        .answer-key strong {{
            color: #00a86b;
        }}
        .footer {{
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
            color: #999;
            font-size: 12px;
        }}
        @media print {{
            body {{
                background: white;
            }}
            .container {{
                box-shadow: none;
            }}
            .no-print {{
                display: none;
            }}
        }}
        .print-button {{
            background-color: #0066cc;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            margin-bottom: 20px;
        }}
        .print-button:hover {{
            background-color: #0052a3;
        }}
    </style>
</head>
<body>
    <div class="container">
        <button class="print-button no-print" onclick="window.print()">🖨️ Print / Download as PDF</button>

        <header>
            <h1>TELC B2 Mock Exam {exam['exam_number']}</h1>
            <div class="exam-info">
                Generated: {exam['generated_date'].split('T')[0]} | Exam ID: {exam['exam_id']}
            </div>
        </header>
"""

        # Add sections
        for section_key, section_data in exam['sections'].items():
            html += f"""
        <div class="section">
            <div class="section-header">
                <h2>{section_data['title']}</h2>
                <div class="time-badge">⏱️ {section_data['time_minutes']} min</div>
            </div>
"""

            # Add questions
            for i, question in enumerate(section_data['questions'], 1):
                html += f"""
            <div class="question">
                <div class="question-number">Question {i}</div>
                <div class="question-text">{question.get('text', 'Question content')}</div>
"""

                if question.get('options'):
                    html += '<div class="options">'
                    for j, option in enumerate(question['options'], 1):
                        html += f'<div class="option">({chr(96+j)}) {option}</div>'
                    html += '</div>'

                if include_answers and question.get('answer'):
                    html += f"""
                <div class="answer-key">
                    <strong>Answer:</strong> {question['answer']}<br>
                    <strong>Explanation:</strong> {question.get('explanation', 'See answer key for detailed explanation.')}
                </div>
"""

                html += '</div>'

            html += '</div>'

        html += """
        <div class="footer">
            <p>TELC B2 Mock Exam Generator | Use for preparation purposes</p>
        </div>
    </div>
</body>
</html>
"""
        return html

    def save_exam(self, exam, output_dir='exams', include_answers=False):
        """Save exam as HTML file"""
        os.makedirs(output_dir, exist_ok=True)

        filename = f"{exam['exam_id']}.html"
        filepath = os.path.join(output_dir, filename)

        html_content = self.export_exam_to_html(exam, include_answers)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)

        return filepath


def main():
    try:
        # Initialize generator
        generator = TelcExamGenerator()

        print("🎓 TELC B2 Mock Exam Generator")
        print("=" * 50)

        # Generate 3 balanced exams
        print("\n📝 Generating 3 balanced mock exams...")
        exams = generator.generate_multiple_exams(count=3)

        # Save exams (without answers)
        exam_files = []
        for exam in exams:
            filepath = generator.save_exam(exam, output_dir='exams', include_answers=False)
            exam_files.append(filepath)
            print(f"✅ Exam {exam['exam_number']} saved: {filepath}")

        # Generate answer keys (with answers)
        print("\n📚 Generating answer keys...")
        for exam in exams:
            filepath = os.path.join('exams', f"{exam['exam_id']}_answers.html")
            html_content = generator.export_exam_to_html(exam, include_answers=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"✅ Answer key {exam['exam_number']} saved: {filepath}")

        print("\n" + "=" * 50)
        print("✨ Done! All exams have been generated.")
        print(f"\n📊 Summary:")
        print(f"   • {len(exam_files)} exams created")
        print(f"   • {len(exam_files)} answer keys created")
        print(f"\nTo generate new exams, run this script again.")
        print("To customize difficulty balance, edit the generate_exam() method.")

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("\nPlease ensure 'data/questions.json' exists in the same directory.")
        print("See README.md for instructions on setting up the questions database.")


if __name__ == '__main__':
    main()
