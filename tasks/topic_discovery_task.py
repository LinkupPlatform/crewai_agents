from crewai import Task
from agents.research_agent import create_research_agent
from tools.linkup_tool import LinkupSearchTool
from typing import Optional


def create_topic_discovery_task(general_area: Optional[str] = None) -> Task:
    """
    Create a task for discovering the 5 hottest topics for LinkedIn content.
    
    Args:
        general_area: Optional general area to focus on (e.g. "AI", "enterprise tech", etc.)
    """
    # Handle different types of user requests
    if general_area:
        # Check if this is a custom instruction like "more funny" or "real life related"
        custom_instructions = ["funny", "humor", "real life", "viral", "drama", "entertainment", 
                              "cultural", "social", "personal", "human interest", "bizarre", 
                              "weird", "surprising", "shocking", "emotional", "trending", "moment"]
        
        is_custom_request = any(word in general_area.lower() for word in custom_instructions)
        
        if is_custom_request:
            search_focus = f"trending viral moments {general_area}"
            search_description = f"viral trending topics that are {general_area} and can be connected to Linkup's expertise"
        else:
            search_focus = general_area
            search_description = f"trending topics in {general_area}"
    else:
        search_focus = "viral trending moments"
        search_description = "viral trending topics and real-time trending content"
    
    return Task(
        description=(
            f"""## Discover the 5 hottest, most viral {search_description} for LinkedIn content creation. 
            Your research should uncover VIRAL trending topics that are getting massive social media attention 
            and would make engaging LinkedIn content.
            
            ### VIRAL DISCOVERY STRATEGY:
            1. REAL-TIME TRENDING: Current events, political developments, viral social media moments
            2. CULTURAL PHENOMENA: Sports, entertainment, cultural events, social movements
            3. BREAKING NEWS: Recent developments getting massive attention on social media
            4. GEOPOLITICAL EVENTS: International relations, diplomatic developments, regional conflicts
            5. BUSINESS & ECONOMICS: Market movements, trade developments, economic policies
            6. SOCIAL MOVEMENTS: Public demonstrations, policy changes, social trends
            
            ### SEARCH EXAMPLES FOR REAL TRENDING CONTENT:
            - 'latest news [topic]' - Recent developments in any area
            - 'trending [topic]' - What's currently popular in any field
            - 'breaking news [topic]' - Current events and developing stories
            - 'recent developments [topic]' - Latest updates in any area
            - '[topic] news today' - Current headlines in any subject
            
            ### CRITICAL REQUIREMENTS:
            - Find GENUINELY VIRAL topics that people are actively sharing and talking about
            - Look for recent incidents, moments, or stories getting social media traction
            - Prioritize topics with high shareability and discussion potential
            - Focus on real-time, current viral moments not generic subjects
            - Find topics with natural professional relevance for LinkedIn audiences
            - Look for stories that would make people stop scrolling and engage
            - Find content with genuine viral momentum and social media buzz
            - Search for specific incidents, moments, or stories people are actually discussing"""
        ).strip(),
        expected_output=(
            """## EXACTLY 5 numbered trending topics based on the search results:
            Format:
            {number}. **{ENGAGING TOPIC TITLE}**
            📰 **Context:** {What's happening - include names, companies, details when available}
            📊 **Key Details:** {Important facts, numbers, or specifics from search results}
            🔥 **Why It's Hot:** {Why this topic is trending or engaging}
            🔗 **Professional Angle:** {Why this matters to professionals and business leaders}
            
            ### SPECIFICITY GUIDELINES (Use when available):
            - Include names of people, companies, CEOs, or organizations when mentioned
            - Add specific numbers, percentages, or metrics if found in the search results
            - Reference news sources when they appear in the content
            - Include dates or timeframes when available
            - Focus on concrete incidents and developments rather than generic trends
            
            ### EXAMPLES OF GOOD APPROACH:
            ✅ 'Trump's AI Action Plan focuses on strengthening U.S. tech capabilities' (specific policy/person)
            ✅ 'Taiwan political gridlock affects tech supply chain concerns' (specific situation/impact)
            ✅ 'Thailand-Cambodia border conflict disrupts regional business' (specific event/business angle)
            ❌ 'Political tensions rise globally' (too vague)
            ❌ 'Tech companies face challenges' (no specifics)
            
            ### CORE REQUIREMENT:
            Create 5 engaging topics based on whatever is trending in the search results, using whatever details are available. Focus on making compelling LinkedIn content rather than forcing specific themes.
            
            ### TOPIC VARIETY GOALS:
            - Mix of whatever is trending: politics, business, culture, sports, geopolitics
            - Include any topics that would interest professional audiences
            - Cover different regions, industries, and sectors when possible
            - Focus on topics that would generate LinkedIn engagement and discussion
            - Each topic should be relevant to professionals regardless of industry"""
        ).strip(),
        agent=create_research_agent(),
        tools=[LinkupSearchTool()]
    ) 