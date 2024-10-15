import csv
import json
import ast

def json_object_to_csv_file(json_object, output_file_path):
    # Extract the list of question-answer pairs
    qa_pairs = json_object.get('data', [])
    
    # Open the CSV file for writing
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
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
    
    print(f"CSV file has been created at {output_file_path}")