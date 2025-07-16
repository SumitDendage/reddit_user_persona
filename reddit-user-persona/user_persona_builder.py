import os
from dotenv import load_dotenv
from transformers import pipeline, set_seed

# Load environment variables
load_dotenv()

# Get Hugging Face token from .env
HF_TOKEN = os.getenv("HF_TOKEN")

# Set seed for reproducibility
set_seed(42)

# Initialize Hugging Face text-generation pipeline
generator = pipeline(
    "text-generation",
    model="gpt2",            # You can change the model if needed
    tokenizer="gpt2",
    use_auth_token=HF_TOKEN
)

# Prompt template for persona generation
template = """
User Persona: Reddit Behavioral & Interest Profile

Interests:
- The user is deeply engaged in cryptocurrency, decentralized finance (DeFi), and blockchain governance mechanisms.
  Cited from post: "Been staking with Lido for over a year now—helps keep Ethereum secure and earns me yield."

Personality Traits:
- Independent-minded, risk-tolerant, and values transparency in financial systems.
  Cited from comment: "I don’t trust centralized exchanges anymore. If it’s not your keys, it’s not your coins."

Writing Style:
- Conversational but informed; often opinionated and confident in delivery.
  Cited from comment: "This is why I moved everything to cold storage. Too many red flags with these platforms."

Preferred Topics:
- Frequently discusses ETH staking, wallet security, protocol governance, and Layer 2 scaling solutions.
  Cited from post: "Anyone else following Arbitrum’s latest governance vote? The delegate debates are actually getting interesting."

Emotional Tone:
- Tone is cautiously optimistic; critiques are grounded in real experiences and practical concerns.
  Cited from comment: "It’s not FUD, it’s reality. These systems still need a lot more transparency before I’ll trust them fully."

Optional – Job, Age, Political View:
- Likely in late 20s to mid-30s, possibly working in tech or finance; political views lean libertarian, with a preference for decentralization and minimal regulation.
  Cited from post: "Regulation is inevitable, but it should come from people who actually understand the tech—not just lawmakers chasing headlines."
"""
def build_persona(posts, comments):
    """
    Builds a user persona using a Hugging Face LLM based on Reddit content.

    Args:
        posts (list): List of Reddit post strings.
        comments (list): List of Reddit comment strings.

    Returns:
        str: Generated user persona text or error message.
    """
    input_text = template.format(
        posts="\n\n".join(posts),
        comments="\n\n".join(comments)
    )

    # Truncate if over token limits
    input_text = input_text[:1000]

    try:
        response = generator(
            input_text,
            max_length=512,
            do_sample=True,
            temperature=0.7
        )[0]['generated_text']
        return response
    except Exception as e:
        print(f"[Error] Failed to generate persona: {e}")
        return "Unable to build persona due to model error."
