import os
import pandas as pd
from Detector import ml_based, rule_based

def combined_prediction(ml_pred, rule_pred):
    if ml_pred == rule_pred:
        return ml_pred
    if rule_pred == "phishing":
        return "phishing"
    return ml_pred

def log_misclassifications(df, output_path):
    mismatches = df[df['combined_label'] != df['label']]
    mismatch_path = output_path.replace('.csv', '_misclassified.csv')
    mismatches.to_csv(mismatch_path, index=False)
    print(f"\nMisclassifications saved to {mismatch_path}")

    # Log event summary
    event_summary_path = output_path.replace('.csv', '_event_summary.txt')
    with open(event_summary_path, 'w') as f:
        phishing_misclassified = mismatches[mismatches['label'] == 'phishing']
        legit_misclassified = mismatches[mismatches['label'] == 'legit']
        f.write(f"Phishing Misclassified as Legit: {len(phishing_misclassified)}\n")
        f.write(f"Legit Misclassified as Phishing: {len(legit_misclassified)}\n")
        f.write(f"Total Misclassifications: {len(mismatches)}\n")
    print(f"\nEvent summary saved to {event_summary_path}")

def main():
    data_path = os.path.join('data', 'sample_emails.csv')
    output_path = os.path.join('data', 'classified_emails.csv')

    df = pd.read_csv(data_path)
    #Fill empty with NaN so data will still populate, without this the ML column is blank
    df['subject'] = df['subject'].fillna("")
    df['body'] = df['body'].fillna("")

    # x is the input, y is the classification flag from the csv file
    x, y = ml_based.load_data(data_path)

    # Model is trained on input and flags
    model = ml_based.train_model(x, y)
    
    # Example prediction
    test_subject = "Important Notice"
    test_body = "Your account has been compromised. Click the link to secure it."
    ml_result = ml_based.predict(model, test_subject, test_body)
    rule_result = rule_based.predict(test_subject, test_body)
    combined_result = combined_prediction(ml_result, rule_result)
    print(f"ML Predicted label: {ml_result}")
    print(f"Rule-Based label: {rule_result}")
    print(f"Combined label: {combined_result}")
    
    # Batch prediction on all emails
    df = pd.read_csv(data_path)
    ml_predictions = [ml_based.predict(model, row['subject'], row['body']) for _, row in df.iterrows()]
    rule_predictions = [rule_based.predict(row['subject'], row['body']) for _, row in df.iterrows()]
    combined_predictions = [combined_prediction(ml, rule) for ml, rule in zip(ml_predictions, rule_predictions)]
    df['ml_predicted_label'] = ml_predictions
    df['rule_predicted_label'] = rule_predictions
    df['combined_label'] = combined_predictions
    print("\nBatch Classification Results:")
    print(df[['subject', 'label', 'ml_predicted_label', 'rule_predicted_label', 'combined_label']])
    
    # Save results to new CSV
    df.to_csv(output_path, index=False)
    print(f"\nResults saved to {output_path}")
    
    # Log misclassifications and summary
    log_misclassifications(df, output_path)

if __name__ == "__main__":
    main()
