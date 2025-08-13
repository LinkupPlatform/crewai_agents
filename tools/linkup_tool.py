import os
from crewai.tools import BaseTool
from typing import Type, Any
from pydantic import BaseModel, Field
import asyncio
import concurrent.futures
from datetime import datetime


class LinkupSearchInput(BaseModel):
    """Input schema for Linkup Search Tool."""
    query: str = Field(description="The search query to find relevant content")


class LinkupSearchTool(BaseTool):
    name: str = "Linkup Search Tool"
    description: str = (
        "Searches for relevant content and trends using Linkup API. "
        "Use this tool to find current industry insights, trending topics, "
        "and professional content that can be used for LinkedIn posts."
    )
    args_schema: Type[BaseModel] = LinkupSearchInput

    def _run(self, query: str) -> str:
        """
        Search for content using Linkup API with enhanced trending topic discovery
        
        Args:
            query: The search query string
            
        Returns:
            String containing search results
        """
        try:
            api_key = os.getenv("LINKUP_API_KEY")
            if not api_key:
                return "Error: LINKUP_API_KEY environment variable not set"
            
            print(f"🔍 Searching for trending topics: '{query}'")
            
            try:
                from linkup import LinkupClient
            except ImportError:
                return "Error: linkup-sdk not installed. Please run: pip install linkup-sdk"
            
            client = LinkupClient(api_key=api_key)
            
            search_results = self._parallel_trending_search(client, query)
            
            print(f"✅ Linkup trending search completed successfully")
            return search_results
                
        except ImportError:
            return "Error: linkup-sdk not installed. Please run: pip install linkup-sdk"
        except Exception as e:
            error_msg = str(e)
            
            if "401" in error_msg or "unauthorized" in error_msg.lower():
                return "Error: Invalid Linkup API key. Please check your LINKUP_API_KEY."
            elif "403" in error_msg or "forbidden" in error_msg.lower():
                return "Error: Access forbidden. Please check your Linkup API permissions."
            elif "429" in error_msg or "rate limit" in error_msg.lower():
                return "Error: Rate limit exceeded. Please wait a moment and try again."
            elif "timeout" in error_msg.lower():
                return "Error: Request to Linkup API timed out. Please try again."
            elif "connection" in error_msg.lower():
                return "Error: Failed to connect to Linkup API. Please check your internet connection."
            else:
                return f"Error: Unexpected error occurred - {error_msg}"

    def _parallel_trending_search(self, client, query: str) -> str:
        """
        Execute multiple parallel searches to find trending content faster
        """
        if query and query.strip():
            search_queries = [
                f"latest news {query}",
                f"trending {query}",
                f"breaking news {query}",
                f"recent developments {query}",
                f"{query} news today"
            ]
            print(f"🎯 User-focused search for: '{query}'")
        else:
            search_queries = [
                "latest business news",
                "latest tech news", 
                "breaking news today",
                "latest CEO news",
                "trending news today"
            ]
            print("🔍 Default trending content search")
        
        all_results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            future_to_query = {
                executor.submit(self._execute_single_search, client, q): q 
                for q in search_queries[:3]
            }
            
            for future in concurrent.futures.as_completed(future_to_query):
                query_text = future_to_query[future]
                try:
                    result = future.result(timeout=10)  # 10 second timeout per search
                    if result and len(result) > 50: 
                        all_results.append(f"=== SEARCH: {query_text[:50]}... ===\n{result}\n")
                except Exception as e:
                    print(f"Search failed for '{query_text[:30]}...': {e}")
                    continue
        
        if len(all_results) < 2:
            for q in search_queries[3:]:
                try:
                    result = self._execute_single_search(client, q)
                    if result and len(result) > 50:
                        all_results.append(f"=== SEARCH: {q[:50]}... ===\n{result}\n")
                        if len(all_results) >= 3:  # Stop when we have enough
                            break
                except Exception as e:
                    continue
        
        if all_results:
            combined_results = "\n".join(all_results)
            
            analysis_prompt = """
            
=== TRENDING TOPIC ANALYSIS WITH SPECIFICITY REQUIREMENTS ===

The search results above contain various trending topics and viral moments. 

YOUR TASK: Identify trending topics from the search results that can be turned into engaging LinkedIn content.

USE AVAILABLE DETAILS:
1. NAMES: Include people, leaders, organizations, countries when mentioned
2. NUMBERS: Add specific figures, percentages, metrics when available
3. SOURCES: Reference news outlets or platforms when they appear
4. TIMING: Include dates or timeframes when mentioned
5. SPECIFICS: Focus on concrete incidents and developments

SEARCH FOR THESE SPECIFIC ELEMENTS:
- Names of leaders, politicians, business figures, organizations
- Specific numbers, statistics, financial figures, or metrics
- Social media engagement numbers (likes, shares, views)
- News outlet citations (Reuters, BBC, CNN, Bloomberg, etc.)
- Specific dates and timeline details
- Concrete developments and outcomes

EXAMPLES OF GOOD SPECIFICITY:
✅ "Lebanon's Prime Minister announced new economic reforms affecting 2M citizens, reported by Reuters"
✅ "UAE's trade with Asia increased 15% to $200B in 2024, according to government data"
✅ "Diplomatic meeting between Saudi Arabia and Iran drew 500K social media mentions, BBC coverage"

❌ AVOID VAGUE DESCRIPTIONS:
❌ "Middle East faces challenges"
❌ "Leaders make statements"
❌ "Tensions rise"

CONTENT APPROACH:
Extract trending topics exactly as they appear in the search results. Don't force connections to specific industries unless they naturally exist in the source material.

MAIN GOAL: Create engaging LinkedIn topics based on whatever trending content is found in the search results, whether it's geopolitics, business, culture, sports, or any other subject.
"""
            
            return combined_results + analysis_prompt
        else:
            fallback_content = """
=== FALLBACK TRENDING TOPICS (Search temporarily limited) ===

Based on typical trending business and tech patterns, here are example current topics:

1. AI Integration Challenges in Enterprise
2. Remote Work Policy Changes at Major Tech Companies  
3. Startup Funding Trends and Market Shifts
4. Executive Leadership Changes in Fortune 500
5. Technology Infrastructure and Security Developments

AGENT INSTRUCTION: Use these as starting points and apply your knowledge to create specific, engaging topics with:
- Real company names you know about
- Recent industry developments
- Current business challenges
- Technology trends making headlines
- Executive and leadership stories

Focus on creating specific, detailed topics even with limited real-time search results.
"""
            return fallback_content

    def _execute_single_search(self, client, search_query: str) -> str:
        """
        Execute a single optimized search query
        """
        try:
            print(f"📡 Linkup Query: '{search_query}'")
            response = client.search(
                query=search_query,
                depth="standard", 
                output_type="sourcedAnswer",
                include_images=False,
            )
            
            if hasattr(response, 'answer') and response.answer:
                result = response.answer
                if result and result.lower() not in ['undefined', 'none', '']:
                    return result
            elif hasattr(response, 'results') and response.results:
                return str(response.results)
            
            return ""
            
        except Exception as e:
            print(f"Single search error: {e}")
            return "" 