# LinkedIn Content Agent 🚀

A CrewAI-powered system that researches trending topics using Linkup and creates engaging LinkedIn posts automatically.

## Overview

This project uses CrewAI to orchestrate two specialized AI agents:

1. **Research Agent** - Uses Linkup API to find trending topics and industry insights
2. **Content Creator Agent** - Transforms research findings into engaging LinkedIn posts

## Features

- 🔍 **Real-time Research**: Uses Linkup API to find current trends and professional insights
- 📝 **AI-Powered Content Creation**: Generates engaging LinkedIn posts optimized for the platform
- 🤖 **Multi-Agent Workflow**: Specialized agents work together seamlessly
- 🎯 **Targeted Content**: Option to research specific topics or discover general trends
- 📊 **Professional Quality**: Content optimized for LinkedIn's algorithm and audience

## Setup

### Prerequisites

- Python 3.9 or higher
- Linkup API key ([Get one here](https://linkup.so))
- OpenAI API key ([Get one here](https://platform.openai.com))

### Installation

1. **Clone and navigate to the project**:
```bash
cd linkedin-content-agent
```

2. **Create and activate virtual environment**:
```bash
uv venv
source .venv/bin/activate
```

3. **Install dependencies**:
```bash
uv sync  
```

4. **Set up environment variables**:
```bash
# Copy the example file and edit it with your real API keys
cp .env.example .env
```

5. **Test your setup**:
```bash
uv run test_linkup.py
```

## Usage

### Basic Usage

Run the interactive workflow:

```bash
uv run crew.py
```

You'll be prompted to enter a specific topic or press Enter to research general trends.

### Programmatic Usage

```python
from crew import LinkedInContentCrew

# Initialize the crew
crew = LinkedInContentCrew()

# Create a LinkedIn post about a specific topic
result = crew.create_linkedin_post("artificial intelligence in healthcare")

# Or research without creating content
research = crew.research_only("remote work trends 2024")
```

### Example Output

The system will generate a complete LinkedIn post like this:

```
🎯 The future of work isn't just remote—it's hyper-personalized.

I've been analyzing the latest workplace trends, and here's what's fascinating: 
Companies that customize work experiences to individual employee needs see 40% 
higher retention rates.

💡 Key insights:
→ Flexible schedules aren't enough anymore
→ Personalized learning paths drive engagement
→ Micro-feedback systems beat annual reviews
→ Purpose-driven projects increase productivity by 23%

The question isn't whether your workplace adapts—it's how quickly you can 
make it personal.

What's one way your organization personalizes the work experience?

#FutureOfWork #EmployeeEngagement #WorkplaceTrends #Leadership #PersonalizedWork
```

## Project Structure

```
linkedin-content-agent/
├── agents/
│   ├── research_agent.py         # Linkup research agent
│   └── content_creator_agent.py  # LinkedIn content creator
├── tasks/
│   ├── research_task.py          # Research task definition
│   └── content_creation_task.py  # Content creation task
├── tools/
│   └── linkup_tool.py            # Linkup API integration
├── crew.py                       # Main orchestration file
├── .env.example                  # Environment variables template
└── README.md                     # This file
```

## Workflow

1. **Research Phase**: The Research Agent uses Linkup to find trending topics and insights
2. **Analysis Phase**: The agent analyzes findings and creates a content brief
3. **Creation Phase**: The Content Creator Agent transforms research into an engaging LinkedIn post
4. **Optimization**: The post is formatted and optimized for LinkedIn's platform

## Customization

### Modify Agent Behavior

Edit the agent files in the `agents/` directory to customize:
- Agent personalities and expertise
- Research focus areas
- Content style and tone

### Adjust Task Parameters

Modify task files in the `tasks/` directory to:
- Change research criteria
- Adjust content requirements
- Modify output formats

### Extend Functionality

- Add more tools in the `tools/` directory
- Create additional agents for specialized tasks
- Implement different content formats (Twitter, blog posts, etc.)

### Debug Mode

Set `verbose=True` in the crew configuration for detailed logging:

```python
crew = Crew(
    agents=[self.research_agent, self.content_creator_agent],
    tasks=[research_task, content_task],
    process=Process.sequential,
    verbose=True  # Enable debug mode
)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues:
1. Check the troubleshooting section above
2. Review the [CrewAI documentation](https://docs.crewai.com)
3. Check [Linkup API documentation](https://docs.linkup.so)
4. Open an issue in this repository 