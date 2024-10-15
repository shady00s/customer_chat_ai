import json
import csv
import ast

def json_to_csv(json_file_path, csv_file_path):
    # Read JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Extract the list of question-answer pairs
    qa_pairs = data.get('data', [])
    
    # Prepare CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write header
        csv_writer.writerow(['question', 'answer'])
        
        # Write data rows
        for qa in qa_pairs:
            question = qa.get('question', '')
            answer = qa.get('answer', '')
            
            # Check if answer is a string representation of an object
            try:
                answer_obj = ast.literal_eval(answer)
                if isinstance(answer_obj, dict):
                    answer = json.dumps(answer_obj)
            except (ValueError, SyntaxError):
                pass  # If it's not a valid Python literal, keep it as is
            
            csv_writer.writerow([question, answer])
    
    print(f"CSV file has been created at {csv_file_path}")