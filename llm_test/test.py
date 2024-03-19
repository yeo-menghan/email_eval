import re

# Function to simulate invoking the model and capturing the output
def invoke_model_with_email(email):
    # Simulated response for demonstration; replace this with actual model invocation
    response = """
1. Personalization: The email lacks personalization as it does not address the recipient by name or reference any specific details about the recipient's site or work. It feels generic and could be sent to anyone. Score: 0.100

2. Clear and Concise: The email is relatively clear in its purpose of requesting a text link placement, but it could be more concise. It includes unnecessary details and could be more direct. Score: 0.600

3. Value Proposition: The email briefly mentions the value proposition by stating that the client's website allows exchanging electronic products for cash, which could be relevant to the recipient's site. However, it could be more explicit in highlighting the benefits for the recipient. Score: 0.500

4. Professional Tone: The email maintains a professional tone with no major grammar or spelling errors. However, it could be improved by being more formal and structured. Score: 0.800

5. Call-to-Action: The email includes a clear call-to-action by requesting a response regarding the text link placement opportunity. Score: 1.000

6. Subject Line: No subject line provided. Score: 0.000

7. Sentiment analysis: The tone of the email is neutral and business-focused. It lacks warmth or enthusiasm that could make it more engaging. Score: 0.400

Overall score: (0.100 + 0.600 + 0.500 + 0.800 + 1.000 + 0.000 + 0.400) / 7 = 0.500
"""
    return response

eval_email = """
Hi,

I am just emailing to ask whether you are open to any potential text link placement? I have been looking for relevant sites to use for my client and this campaign, as well as building relationships with webmasters.  Your site would be a good match and I’d like to discuss some opportunities with you.

I am actually looking to place a text link within a recent, relevant article on your site. This will link back to my clients site, and will be placed within a short sentence at the end of the article. My client is a website where you can exchange electronic products for cash, therefore I feel that this is highly relevant to your site.

If this would be possible, then please let me know and I will send you the details, including costs. I would really appreciate it if you could get back to me regarding this opportunity as soon as possible.

Looking forward to hearing back from you.

Kind Regards.
"""

# Placeholder for model outputs
model_outputs = []

# Simulate invoking the model 3 times
for _ in range(3):
    output = invoke_model_with_email(eval_email)
    model_outputs.append(output)

# Initialize lists to hold scores for each category and total scores
category_scores = [[] for _ in range(7)]  # 7 categories
total_scores = []

# Process each model output
for output in model_outputs:
    # Find all scores in the output
    scores = re.findall(r'Score: ([0-9.]+)', output)
    scores = [float(score) for score in scores]
    for score in scores:
        print("test", score)
    print("end test")

    total = 0
    for i, score in enumerate(scores):
        category_scores[i].append(score)
        total += score

    total = total / 7
    total_scores.append(total)

# Calculate average scores for each category and overall
average_category_scores = [sum(scores)/len(scores) if len(scores) > 0 else 0 for scores in category_scores]
average_total_score = sum(total_scores) / len(total_scores) if len(total_scores) > 0 else 0

# Print the averages
for i, score in enumerate(average_category_scores, start=1):
    print(f"Category {i} Average Score: {score:.3f}")

print(f"Average Overall Score: {average_total_score:.3f}")
