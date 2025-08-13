import os
from dotenv import load_dotenv
from crewai import Crew, Process

# Import agents and tasks
from agents.research_agent import create_research_agent
from agents.content_creator_agent import create_content_creator_agent
from tasks.research_task import create_research_task
from tasks.content_creation_task import create_content_creation_task
from tasks.topic_discovery_task import create_topic_discovery_task

# Load environment variables
load_dotenv()

if not os.getenv("OPENAI_MODEL_NAME"):
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4.1-2025-04-14"


class LinkedInContentCrew:
    """
    LinkedIn Content Creation Crew using Linkup for research
    """
    
    def __init__(self):
        """Initialize the crew with agents"""
        self.research_agent = create_research_agent()
        self.content_creator_agent = create_content_creator_agent()
    
    def get_hot_topics(self, general_area: str = None):
        """Get the 5 hottest topics for content creation"""
        
        # Create the research agent
        research_agent = create_research_agent()
        
        # Create the topic discovery task
        topic_task = create_topic_discovery_task(general_area)
        
        # Create a crew for topic discovery
        topic_crew = Crew(
            agents=[research_agent],
            tasks=[topic_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute the crew and return results
        return topic_crew.kickoff()

    def create_linkedin_post(self, topic: str = None):
        """
        Create a LinkedIn post based on research findings
        
        Args:
            topic: Optional specific topic to research. If None, will search for general trends
            
        Returns:
            The final LinkedIn post content
        """
        # Create tasks
        research_task = create_research_task(self.research_agent, topic)
        content_task = create_content_creation_task(self.content_creator_agent, research_task)
        
        # Create crew
        crew = Crew(
            agents=[self.research_agent, self.content_creator_agent],
            tasks=[research_task, content_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute the workflow
        result = crew.kickoff()
        return result
    
    def research_only(self, topic: str = None):
        """
        Perform research only without creating content
        
        Args:
            topic: Optional specific topic to research
            
        Returns:
            Research findings
        """
        research_task = create_research_task(self.research_agent, topic)
        
        crew = Crew(
            agents=[self.research_agent],
            tasks=[research_task],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        return result


def main():
    """
    Main function to demonstrate the LinkedIn content creation workflow
    """
    # Check if required environment variables are set
    if not os.getenv("LINKUP_API_KEY"):
        print("⚠️  Warning: LINKUP_API_KEY environment variable not set")
        print("Please set your Linkup API key in a .env file or as an environment variable")
        return
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY environment variable not set")
        print("Please set your OpenAI API key in a .env file or as an environment variable")
        return
    
    # Initialize the crew
    crew = LinkedInContentCrew()
    
    # Example usage
    print("🚀 Starting LinkedIn Content Creation Workflow...")
    print("=" * 60)
    
    # Ask user for workflow preference
    print("Choose your workflow:")
    print("1. Get 5 hottest topics and choose one")
    print("2. Enter a specific topic directly")
    print("3. Let AI choose from general trends")
    
    choice = input("\nEnter your choice (1, 2, or 3): ").strip()
    
    try:
        if choice == "1":
            # Get hot topics workflow with feedback loop
            print("\n🔍 Discovering the hottest topics...")
            general_area = input("Enter a general area (e.g., 'AI', 'enterprise tech') or press Enter for default: ").strip()
            general_area = general_area if general_area else None
            
            while True:
                hot_topics = crew.get_hot_topics(general_area)
                
                print("\n" + "=" * 60)
                print("🔥 HOTTEST TOPICS:")
                print("=" * 60)
                print(hot_topics)
                
                # Let user choose or request new topics
                print("\n" + "=" * 60)
                print("Options:")
                print("• Enter 1-5 to create a post about that topic")
                print("• Enter 'new' to get different topics")
                print("• Enter 'refresh' to search again with custom instructions")
                
                user_input = input("\nYour choice: ").strip().lower()
                
                if user_input in ["1", "2", "3", "4", "5"]:
                    # Extract the chosen topic title from the response
                    lines = str(hot_topics).split('\n')
                    topic_line = None
                    for line in lines:
                        if line.strip().startswith(f"{user_input}."):
                            topic_line = line
                            break
                    
                    if topic_line:
                        # Extract topic title (remove number and clean up)
                        topic = topic_line.split('.', 1)[1].strip()
                        topic = topic.split('\n')[0].strip()  # Get just the title
                        print(f"\n✅ Creating post about: {topic}")
                        break
                    else:
                        topic = "AI infrastructure trends"
                        print(f"\n⚠️  Could not parse topic, using default: {topic}")
                        break
                        
                elif user_input == "new":
                    print("\n🔄 Searching for different topics...")
                    continue
                    
                elif user_input == "refresh":
                    print("\n🎯 What kind of topics would you like?")
                    print("Examples: 'more funny', 'real life related', 'viral moments', 'business drama', etc.")
                    custom_instruction = input("Describe what you want: ").strip()
                    
                    if custom_instruction:
                        # Use custom instruction as the general area
                        general_area = custom_instruction
                        print(f"\n🔍 Searching for topics that are: {custom_instruction}")
                    continue
                    
                else:
                    print("❌ Invalid choice. Using default topic.")
                    topic = "AI infrastructure trends"
                    break
                
        elif choice == "2":
            # Direct topic entry
            topic = input("Enter a specific topic to research: ").strip()
            topic = topic if topic else None
            
        elif choice == "3":
            # General trends
            topic = None
            print("\n🎯 Letting AI choose from general trends...")
            
        else:
            print("❌ Invalid choice. Using general trends.")
            topic = None
        
        # Create a LinkedIn post
        print(f"\n🔍 Researching and creating LinkedIn post...")
        result = crew.create_linkedin_post(topic)
        
        print("\n" + "=" * 60)
        print("📝 FINAL LINKEDIN POST:")
        print("=" * 60)
        print(result)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Please check your API keys and try again.")


if __name__ == "__main__":
    main()

