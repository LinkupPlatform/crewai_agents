from crewai import Task


def create_research_task(agent, topic: str = None):
    """
    Creates a research task for finding trending topics and content insights
    
    Args:
        agent: The research agent to assign this task to
        topic: Optional specific topic to research. If None, will search for general trends
    """
    search_query = topic if topic else "latest professional trends linkedin content strategy"
    
    return Task(
        description=(
            f"Research and analyze current trends and engaging content ideas using Linkup search. "
            f"Search for: '{search_query}'. "
            "Your research should find VIRAL content opportunities and professional insights:\n"
            "1. TRENDING TOPICS: Current stories, news, or cultural moments (ANY subject)\n"
            "2. PROFESSIONAL RELEVANCE: Why these topics matter to business professionals\n"
            "3. CURRENT DEVELOPMENTS: Recent events, changes, or announcements\n"
            "4. REAL EXAMPLES: Specific people, organizations, incidents, or developments\n"
            "5. TIMELY HOOKS: Breaking news or trending topics that provide engagement opportunities\n"
            "6. PROFESSIONAL ANGLES: How to make any topic relevant to LinkedIn audiences\n"
            "7. CULTURAL MOMENTS: Popular discussions that professionals would find interesting\n"
            "8. ENGAGEMENT POTENTIAL: Topics that will get shares, comments, and discussions\n\n"
            "CONTENT REQUIREMENTS:\n"
            "- Find trending topics from ANY area that would interest professionals\n"
            "- Look for viral news, cultural moments, political developments, or popular discussions\n"
            "- Identify professional angles for any trending content\n"
            "- Balance viral engagement potential with professional relevance\n"
            "- Find topics that will get shares and comments from LinkedIn audiences\n"
            "- Look for recent events that professionals would discuss or care about\n"
            "- Prioritize timely, trending content that creates natural conversation starters\n\n"
            "Provide a comprehensive content brief that includes:\n"
            "- Key trending topics found\n"
            "- Specific angles or perspectives to explore\n"
            "- Target audience insights\n"
            "- Recommended tone and style\n"
            "- Potential engagement hooks"
        ),
        expected_output=(
            "A viral-potential content brief containing:\n"
            "1. VIRAL TOPICS: 2-3 trending topics from ANY area (tech, culture, news, business) "
            "that are currently getting attention and engagement\n"
            "2. PROFESSIONAL CONNECTIONS: Creative ways to make these trending topics "
            "relevant to business professionals and LinkedIn audiences\n"
            "3. ENGAGEMENT HOOKS: Timely angles that will get people to share, comment, and discuss\n"
            "4. CURRENT EVENTS: Recent developments, viral moments, or trending discussions "
            "that provide natural conversation starters\n"
            "5. CLEVER BRIDGES: How to naturally make any topic professionally relevant "
            "without forced connections\n"
            "6. PROFESSIONAL ANGLES: Business insights or implications of trending topics\n"
            "7. SHAREABILITY FACTORS: Elements that make content likely to be shared and discussed\n"
            "8. SPECIFIC EXAMPLES: Real companies, people, events, or incidents that are trending now"
        ),
        agent=agent
    ) 