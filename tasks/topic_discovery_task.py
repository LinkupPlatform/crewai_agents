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
            f"Discover the 5 hottest, most viral {search_description} for LinkedIn content creation. "
            "Your research should uncover VIRAL trending topics that are getting massive social media attention "
            "and would make engaging LinkedIn content.\n\n"
            
            "VIRAL DISCOVERY STRATEGY:\n"
            "1. REAL-TIME TRENDING: Current events, political developments, viral social media moments\n"
            "2. CULTURAL PHENOMENA: Sports, entertainment, cultural events, social movements\n"
            "3. BREAKING NEWS: Recent developments getting massive attention on social media\n"
            "4. GEOPOLITICAL EVENTS: International relations, diplomatic developments, regional conflicts\n"
            "5. BUSINESS & ECONOMICS: Market movements, trade developments, economic policies\n"
            "6. SOCIAL MOVEMENTS: Public demonstrations, policy changes, social trends\n\n"
            
            "SEARCH EXAMPLES FOR REAL TRENDING CONTENT:\n"
            "- 'latest news [topic]' - Recent developments in any area\n"
            "- 'trending [topic]' - What's currently popular in any field\n"
            "- 'breaking news [topic]' - Current events and developing stories\n"
            "- 'recent developments [topic]' - Latest updates in any area\n"
            "- '[topic] news today' - Current headlines in any subject\n\n"
            
            "CRITICAL REQUIREMENTS:\n"
            "- Find GENUINELY VIRAL topics that people are actively sharing and talking about\n"
            "- Look for recent incidents, moments, or stories getting social media traction\n"
            "- Prioritize topics with high shareability and discussion potential\n"
            "- Focus on real-time, current viral moments not generic subjects\n"
            "- Find topics with natural professional relevance for LinkedIn audiences\n"
            "- Look for stories that would make people stop scrolling and engage\n"
            "- Find content with genuine viral momentum and social media buzz\n"
            "- Search for specific incidents, moments, or stories people are actually discussing"
        ),
        expected_output=(
            "EXACTLY 5 numbered trending topics based on the search results:\n\n"
            "Format:\n"
            "{number}. **{ENGAGING TOPIC TITLE}**\n"
            "   📰 **Context:** {What's happening - include names, companies, details when available}\n"
            "   📊 **Key Details:** {Important facts, numbers, or specifics from search results}\n"
            "   🔥 **Why It's Hot:** {Why this topic is trending or engaging}\n"
            "   🔗 **Professional Angle:** {Why this matters to professionals and business leaders}\n\n"
            
            "SPECIFICITY GUIDELINES (Use when available):\n"
            "- Include names of people, companies, CEOs, or organizations when mentioned\n"
            "- Add specific numbers, percentages, or metrics if found in the search results\n"
            "- Reference news sources when they appear in the content\n"
            "- Include dates or timeframes when available\n"
            "- Focus on concrete incidents and developments rather than generic trends\n\n"
            
            "EXAMPLES OF GOOD APPROACH:\n"
            "✅ 'Trump's AI Action Plan focuses on strengthening U.S. tech capabilities' (specific policy/person)\n"
            "✅ 'Taiwan political gridlock affects tech supply chain concerns' (specific situation/impact)\n"
            "✅ 'Thailand-Cambodia border conflict disrupts regional business' (specific event/business angle)\n"
            "❌ 'Political tensions rise globally' (too vague)\n"
            "❌ 'Tech companies face challenges' (no specifics)\n\n"
            
            "CORE REQUIREMENT:\n"
            "Create 5 engaging topics based on whatever is trending in the search results, using whatever details are available. Focus on making compelling LinkedIn content rather than forcing specific themes.\n\n"
            
            "TOPIC VARIETY GOALS:\n"
            "- Mix of whatever is trending: politics, business, culture, sports, geopolitics\n"
            "- Include any topics that would interest professional audiences\n"
            "- Cover different regions, industries, and sectors when possible\n"
            "- Focus on topics that would generate LinkedIn engagement and discussion\n"
            "- Each topic should be relevant to professionals regardless of industry"
        ),
        agent=create_research_agent(),
        tools=[LinkupSearchTool()]
    ) 