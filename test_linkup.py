#!/usr/bin/env python3
"""
Test script to verify Linkup API connection and GPT-4.1 configuration
"""

import os
from dotenv import load_dotenv
from tools.linkup_tool import LinkupSearchTool

# Load environment variables
load_dotenv()

def test_linkup_api():
    """Test the Linkup API connection"""
    print("🔧 Testing Linkup API Connection...")
    print("=" * 50)
    
    # Check if API key is set
    api_key = os.getenv("LINKUP_API_KEY")
    if not api_key:
        print("❌ LINKUP_API_KEY not found in environment variables")
        print("Please set your Linkup API key in the .env file")
        return False
    
    print(f"✅ API Key found: {api_key[:8]}...{api_key[-4:]}")
    
    # Test the SDK import first
    try:
        from linkup import LinkupClient
        print("✅ Linkup SDK imported successfully")
    except ImportError:
        print("❌ Linkup SDK not installed")
        print("Please run: pip install linkup-sdk")
        return False
    
    # Test direct SDK usage
    try:
        print("🔧 Testing direct SDK connection...")
        client = LinkupClient(api_key=api_key)
        
        # Simple test query
        test_query = "latest professional trends 2025"
        print(f"🔍 Testing search for: '{test_query}'")
        
        response = client.search(
            query=f"Find current professional and business trends about: {test_query}. Focus on 2025 developments and avoid outdated 2024 information.",
            depth="standard",
            output_type="sourcedAnswer",
            include_images=False,
        )
        
        print("✅ Direct SDK test successful")
        
        if hasattr(response, 'answer'):
            answer_preview = response.answer[:200] + "..." if len(response.answer) > 200 else response.answer
            print(f"📋 Answer preview: {answer_preview}")
        
    except Exception as e:
        print(f"❌ Direct SDK test failed: {str(e)}")
        return False
    
    # Test the tool
    tool = LinkupSearchTool()
    print(f"🛠️  Tool initialized: {tool.name}")
    
    # Test with a simple query
    test_query = "AI trends in business 2025"
    print(f"🔍 Testing tool search for: '{test_query}'")
    print("-" * 30)
    
    result = tool._run(test_query)
    
    print("📋 LINKUP TOOL RESPONSE:")
    print("-" * 30)
    print(result[:500] + "..." if len(result) > 500 else result)
    print("-" * 30)
    
    if "Error:" in result:
        print("❌ Linkup tool test failed")
        return False
    else:
        print("✅ Linkup tool test successful")
        return True

def test_openai_config():
    """Test OpenAI configuration"""
    print("\n🤖 Testing OpenAI Configuration...")
    print("=" * 50)
    
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("❌ OPENAI_API_KEY not found in environment variables")
        return False
    
    print(f"✅ OpenAI API Key found: {openai_key[:8]}...{openai_key[-4:]}")
    
    # Check model configuration
    model = os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")
    print(f"🧠 Model configured: {model}")
    
    if "gpt-4" in model:
        print("✅ GPT-4 model configured correctly")
        return True
    else:
        print("⚠️  Warning: Not using GPT-4 model")
        print("Set OPENAI_MODEL_NAME=gpt-4-turbo-preview in your .env file for best results")
        return False

def main():
    """Main test function"""
    print("🚀 LinkedIn Content Agent - API Testing")
    print("=" * 60)
    
    linkup_ok = test_linkup_api()
    openai_ok = test_openai_config()
    
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY:")
    print("=" * 60)
    print(f"Linkup API: {'✅ WORKING' if linkup_ok else '❌ FAILED'}")
    print(f"OpenAI Config: {'✅ CONFIGURED' if openai_ok else '❌ NEEDS SETUP'}")
    
    if linkup_ok and openai_ok:
        print("\n🎉 All systems ready! You can now run the crew.")
        print("Run: python crew.py")
    else:
        print("\n⚠️  Please fix the issues above before running the crew.")
        
        if not linkup_ok:
            print("\nLinkup API Issues:")
            print("- Check your LINKUP_API_KEY in .env file")
            print("- Verify your Linkup account has API access")
            print("- Check your internet connection")
        
        if not openai_ok:
            print("\nOpenAI Configuration:")
            print("- Set OPENAI_API_KEY in .env file")
            print("- Set OPENAI_MODEL_NAME=gpt-4-turbo-preview for GPT-4.1")

if __name__ == "__main__":
    main() 