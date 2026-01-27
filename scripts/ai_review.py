from google import genai
import sys

client = genai.Client()

#review_code takes a code diff as input and returns a review of the code
def review_code(diff_text):
    # Write a multi-line f-string prompt that includes {diff_text}
    # Tell Gemini to act as a code reviewer and focus on security, bugs, performance
    prompt = f"""You are an expert code reviewer. Review the following code diff and provide feedback.

Focus on:
1. Security vulnerabilities
2. Bug risks
3. Performance issues
4. Best practice violations

For each issue found, provide:
- Severity: HIGH / MEDIUM / LOW
- Description of the issue
- Suggested fix

If the code looks good, say so.

IMPORTANT: At the very end of your review, add a severity summary line in exactly this format:
SEVERITY_SUMMARY: <level>
Where <level> is one of: CRITICAL, WARNING, GOOD

Use CRITICAL if any HIGH severity issues exist.
Use WARNING if only MEDIUM or LOW severity issues exist.
Use GOOD if no issues found.

Code diff to review:

{diff_text}


Provide your review in a clear, structured format, ending with the SEVERITY_SUMMARY line."""


    # Send the prompt to the model and get a response
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    # Return just the text from the response
    return response.text

#parse_severity extracts the severity level from the review output
def parse_severity(review_text):
    """Extract severity level from the review output."""
    for line in review_text.strip().split("\n"): # Split the review text into lines
        if line.strip().startswith("SEVERITY_SUMMARY:"): # If the line starts with "SEVERITY_SUMMARY:"
            level = line.split(":", 1)[1].strip().upper() # Split the line into key and value and get the value
            if level in ("CRITICAL", "WARNING", "GOOD"): # If the level is in the list of valid levels
                return level # Return the level
    return "WARNING"  # Default to WARNING if parsing fails


# Main function that takes a diff file as input and prints the review
if __name__ == "__main__":
    if len(sys.argv) > 1: # If a diff file is provided, read it
        diff_file = sys.argv[1] # Get the diff file from the command line
        with open(diff_file, "r") as f: # Read the diff file
            diff_content = f.read()
    else:
        diff_content = sys.stdin.read() # Read the diff from stdin

    review = review_code(diff_content) # Review the code
    severity = parse_severity(review) # Extract the severity level

    print(review) # Print the review

    # Write the severity level to a file
    with open("severity.txt", "w") as f:
        f.write(severity)

    '''The review goes to stdout (captured by the workflow for the PR comment), and the severity
    goes to a file (read by the labeling step)'''

