from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import re

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YourKey")

llm = ChatOpenAI(temperature=0.0,
                 openai_api_key=OPENAI_API_KEY,
                 model_name='gpt-3.5-turbo',
                #  model_name='gpt-4',
                )

email_eval_prompt = """
You are a master email evaluator. You are fair and consistent with your judgement. Assess the provided outreach email based on specified metrics and assign scores for each criterion. Calculate an overall score by averaging the individual scores.

This is an example of a good outreach email with a score above 0.80 out of 1 as it demonstrates strong elements of personalization, clarity, professionalism, and a clear call-to-action, but could improve in terms of articulating the value proposition and including a follow-up plan:
```
Subject Line: "Interested in Collaborating? Let's Grow Together!"

Email body:
Hey [Recipient's Name],I hope this email finds you well. I've been following your work at [Their Company/Blog] and have been truly impressed by [Specific Detail or Achievement]. Your insights have been invaluable to me, especially [Reference to a Specific Post or Work].I wanted to reach out because I believe there could be a great opportunity for collaboration between our brands. I have some exciting ideas that I think your audience at [Their Audience] would love, including topics like [Title 1], [Title 2], and [Title 3].To give you a sense of my style, here are two of my most popular posts: [Your Best Posts with Links].At [Your Company], we specialize in helping businesses like yours achieve [Specific Goal].

I'd love to discuss how we can work together to help you grow your business. Would you be open to a brief call to explore this further? I promise it won't take more than 15 minutes.Please let me know if you're available at:
[Date & Time]
[Date & Time]
[Date & Time]

Please let me know if any of these dates work for you, or if there's another time that might be more convenient. I'm looking forward to the possibility of collaborating and helping your business grow.

Looking forward to reconnecting and exploring the possibilities of collaboration.

Best regards,
[Your Name]
```

Task: Evaluate the outreach email on these metrics, giving a score from a scale of 0 to 1 (3 decimal place accuracy) for each metric:
1. Personalization: Personalized emails are more likely to be opened and read, as they show that the sender has taken the time to research and understand the recipient's needs and interests. Personalization can be achieved by using the recipient's name, referencing their work or interests, and tailoring the message to their specific needs
2. Clear and Concise: An effective outreach email should be clear and concise, with a well-defined purpose and a clear call-to-action. Avoid using jargon or overly complex language, and keep the message focused on the main point. It should not sound too gimmicky or a contest.
3. Value Proposition: The email should clearly communicate the value that the recipient will gain from engaging with the sender. This can be done by highlighting the benefits of the product, service, or opportunity being offered, and how it aligns with the recipient's goals or needs
4. Professional Tone: The email should be written in a professional tone, with proper grammar, spelling, and punctuation. Avoid using overly casual or informal language, as this can come across as unprofessional or insincere
5. Call-to-Action: The email should include a clear and compelling call-to-action, such as a request for a meeting, a phone call, or a response to a question. This helps to guide the recipient towards the next step in the process
6. Subject Line: A catchy and relevant subject line is crucial for getting the email opened. It should be short, clear, and engaging, and should accurately reflect the content of the email. If there is no subject line, return a 0
7: Sentiment analysis: evaluate the emotional tone and language used within the email itself. By analyzing the sentiment of the email content, you can gauge how the message is likely to be perceived by the recipient. Assign a higher score if the tone is positive.

Thereafter, calculate an overall score by dividing the scores by 7.

Outreach email:

"""

eval_email = """
Hi,

I am just emailing to ask whether you are open to any potential text link placement? I have been looking for relevant sites to use for my client and this campaign, as well as building relationships with webmasters.  Your site would be a good match and I’d like to discuss some opportunities with you.

I am actually looking to place a text link within a recent, relevant article on your site. This will link back to my clients site, and will be placed within a short sentence at the end of the article. My client is a website where you can exchange electronic products for cash, therefore I feel that this is highly relevant to your site.

If this would be possible, then please let me know and I will send you the details, including costs. I would really appreciate it if you could get back to me regarding this opportunity as soon as possible.

Looking forward to hearing back from you.

Kind Regards.
"""

def invoke_model_with_email(email):
    prompt = ChatPromptTemplate.from_messages([
        ("system", email_eval_prompt),
        ("user", "{input}")
    ])

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    response = chain.invoke({"input": eval_email})
    return response
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

    total = 0
    for i, score in enumerate(scores):
        category_scores[i].append(score)
        total += score

    total = total / 7
    print("total_score: ", total)
    total_scores.append(total)
    print("end test")


# Calculate average scores for each category and overall
average_category_scores = [sum(scores)/len(scores) if len(scores) > 0 else 0 for scores in category_scores]
average_total_score = sum(total_scores) / len(total_scores) if len(total_scores) > 0 else 0

# Print the averages
for i, score in enumerate(average_category_scores, start=1):
    print(f"Category {i} Average Score: {score:.3f}")

print(f"Average Overall Score: {average_total_score:.3f}")
