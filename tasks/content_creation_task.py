from crewai import Task


def create_content_creation_task(agent, research_output):
    """
    Creates a content creation task for writing LinkedIn posts based on research
    
    Args:
        agent: The content creator agent to assign this task to
        research_output: The output from the research task
    """
    return Task(
        description=(
            "Create a thoughtful LinkedIn post that demonstrates professional insight and perspective. "
            "Write with the depth and authority of someone who understands current events and their "
            "implications for business and professional audiences:\n\n"
            "SIMPLE STRUCTURE:\n"
            "1. POWERFUL HOOK: Start with a shocking fact, surprising number, or bold statement that stops scrolling\n"
            "2. CLEAR EXPLANATION: Explain what's happening using simple words\n"
            "3. REAL INSIGHTS: Share what you know that others don't\n"
            "4. PRACTICAL IMPLICATIONS: What this means for readers\n"
            "5. SIMPLE CONCLUSION: End with a clear takeaway or question\n\n"
            "PROFESSIONAL INSIGHT REQUIREMENTS:\n"
            "- Reveal non-obvious insights that demonstrate deep understanding of the topic\n"
            "- Bridge current events with broader implications using simple, clear language\n"
            "- Share perspectives that show thoughtful analysis of trends and developments\n"
            "- Demonstrate understanding of how current events affect business and professionals\n"
            "- Write content that other professionals would want to engage with and share\n"
            "- Use plain English to communicate sophisticated insights. Never use em dashes or complex punctuation\n\n"
            "POWERFUL HOOK EXAMPLES:\n"
            "- '47% of companies missed their Q4 targets because of one trade route.'\n"
            "- 'The CEO meeting lasted 12 minutes. It changed everything.'\n"
            "- 'Three words just cost this company $2 billion.'\n"
            "- 'Nobody saw this coming. Except the data.'\n"
            "- '15,000 employees found out through a tweet.'\n"
            "- 'The contract was signed. Then this happened.'\n\n"
            "SIMPLE LANGUAGE RULES:\n"
            "- NO FLUFF: Avoid phrases like 'landscape of', 'sea of', 'striking reality', 'often goes unnoticed'\n"
            "- NO METAPHORS: Don't use sailing, journey, landscape, or any fancy comparisons\n"
            "- NO DRAMATIC LANGUAGE: Avoid 'remarkable', 'fascinating', 'striking', 'profound'\n"
            "- NO AI LANGUAGE: Never use 'spark', 'ignite', 'catalyst', 'paradigm', 'ecosystem', 'synergy'\n"
            "- NO BUSINESS JARGON: Skip 'pivot', 'scale', 'optimize', 'streamline', 'innovate', 'dynamic'\n"
            "- NO CLICHES: Avoid 'at the end of the day', 'think outside the box', 'move the needle'\n"
            "- NO AI PATTERNS: Never write 'It's not just about X anymore; it's about Y' - this sounds robotic\n"
            "- NO SEMICOLONS: Don't use semicolons in LinkedIn posts - they sound too formal and AI-like\n"
            "- NO 'ANYMORE' PHRASES: Avoid 'It's no longer about...' or 'Gone are the days when...'\n"
            "- STRONG HOOK REQUIRED: Start with a powerful sentence, shocking fact, or attention-grabbing statement\n"
            "- USE EVERYDAY WORDS: Say 'use' not 'leverage', 'help' not 'facilitate', 'start' not 'spark'\n"
            "- SHORT SENTENCES: Keep most sentences under 20 words\n"
            "- DIRECT COMMUNICATION: Say what you mean without extra words\n"
            "- REAL EXAMPLES: Use specific companies, numbers, and concrete facts\n"
            "- NO MARKETING SPEAK: Write like you're explaining to a colleague, not selling something\n"
            "- HUMAN TONE: Sound like a real person, not a robot or marketing copy"
        ),
        expected_output=(
            "A simple, direct LinkedIn post that provides real value:\n\n"
            "1. POWERFUL HOOK: Start with a shocking fact, specific number, or bold statement that stops scrolling\n"
            "2. CLEAR EXPLANATION: Explain what's happening in simple terms\n"
            "3. REAL INSIGHTS: Share specific knowledge that provides genuine value\n"
            "4. CONCRETE EXAMPLES: Use real companies, numbers, or specific situations\n"
            "5. PRACTICAL TAKEAWAY: What readers should know or do\n"
            "6. SIMPLE ENDING: Clear conclusion or relevant question\n"
            "7. RELEVANT HASHTAGS: 3-4 simple, relevant tags\n\n"
            "The post must sound like a knowledgeable person explaining something clearly to a colleague. "
            "No fancy language, no AI patterns like 'It's not just about X anymore; it's about Y'. "
            "No semicolons or formal language. Start with a hook that grabs attention immediately. "
            "Use everyday words to communicate sophisticated insights. The value comes from what you say, not how fancy you say it."
        ),
        agent=agent,
        context=[research_output] if research_output else []
    ) 