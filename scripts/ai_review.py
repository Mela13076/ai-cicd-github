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
Code diff to review:
{diff_text}
Provide your review in a clear, structured format."""

    # Send the prompt to the model and get a response
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    # Return just the text from the response
    return response.text

# Main function that takes a diff file as input and prints the review
if __name__ == "__main__":
    if len(sys.argv) > 1: # If a diff file is provided, read it
        diff_file = sys.argv[1] # Get the diff file from the command line
        with open(diff_file, "r") as f: # Read the diff file
            diff_content = f.read()
    else:
        diff_content = sys.stdin.read() # Read the diff from stdin

    review = review_code(diff_content) # Review the code
    print(review) # Print the review
