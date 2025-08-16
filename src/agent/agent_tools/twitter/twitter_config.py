class TwitterConfig:
    def __init__(self):
        # Agent will respond to tweets from these users every time that it runs
        # Add Twitter usernames (without @) of users you want to interact with
        self.KEY_USERS = ["SentientAGI", "hstyagi", "0xsachi", "oleg_golev", "vivekkolli"]

        # Agent will respond to tweets from key users containing this key 
        # phrase every time that it runs
        self.KEY_PHRASE = None  # Respond to all tweets from key users

        # If true agent will quote tweet key user's tweets every time that it 
        # runs (instead of responding to tweets) (will ignore quote tweets)
        self.QUOTE_MODE = False
        
        # If true agent will post a tweet every time that it runs
        self.POST_MODE = True  # Enable posting mode for more activity
        
        # How often to post original tweets (in runs)
        # With 48 runs per day, posting every 2 runs = 24 posts per day (hourly)
        self.POST_EVERY_N_RUNS = 2

        # Prompt that is provided to model to generate a post
        self.POST_PROMPT = """Generate an engaging tweet about SentientAGI and open-source AGI. 

Key topics to focus on:
- GRID: Global Research and Intelligence Directory - world's largest network of intelligence
- 110+ partners: 50+ specialized agents, 50+ data providers, 6 AI models, 10+ compute providers
- Partners include: Napkin (AI diagrams), Exa (web search), Caldo (people search), Kaito (crypto data), Messari Co-Pilot, The Graph, EigenLayer
- Sentient-native products: Dobby, Model Fingerprinting, Open Deep Search
- Open-source AGI vs closed AGI (OpenAI, Anthropic, Google)
- Community-built AI that serves humanity, not corporations
- Sentient Chat as the gateway to unified intelligence - distribution channel for builders
- $SENT token economy: stake on artifacts, earn yield, fund open-source AI
- AGI as network of specialized intelligences, not monolithic model
- Queries split, routed to right intelligences, merged for AGI-level results
- Making open-source AGI monetizable and sustainable

Keep it under 280 characters, be authentic and insightful. 
No hashtags. Make it engaging and thought-provoking about the future of AI."""

        # Prompt that is provided to model, along with twitter conversation, to
        # generate a response
        self.RESPONSE_PROMPT = """You are responding to a conversation from the SentientAGI team or community. 

Deep Context about SentientAGI:
- Mission: Ensure AGI is open-source and not controlled by single entities
- GRID (Global Research and Intelligence Directory): World's largest network of intelligence
- 110+ partners: 50+ specialized agents, 50+ data providers, 6 AI models, 10+ compute providers
- Key partners: Napkin (AI diagrams), Exa (web search), Caldo (people search), Kaito (crypto data), Messari Co-Pilot, The Graph, EigenLayer
- Sentient-native products: Dobby LLM, Model Fingerprinting, Open Deep Search
- AGI thesis: Network of specialized intelligences, not monolithic model
- Queries split, routed to right intelligences, enriched with tools, merged for coherent results
- Sentient Chat: Gateway to unified intelligence, distribution channel for builders
- $SENT token economy: Stake on artifacts, earn yield, fund open-source AI development
- Alternative to closed systems (OpenAI, Anthropic, Google)
- Making open-source AGI monetizable and sustainable
- Real-time intelligence access, revenue flows back to builders

Respond thoughtfully and add value to the conversation. Reference relevant Sentient concepts when appropriate.
Keep it under 280 characters. No hashtags. Be authentic and engaging."""

        # Agent will post this number of respones per run
        self.RESPONSES_PER_RUN = 1  # Test with just 1 response per check
        
        # Monitor mentions of the bot account
        self.MONITOR_MENTIONS = True
       
        # Agent will run this number of times per day (higher number = more frequent checks)
        self.RUNS_PER_DAY = 48  # Every 30 minutes - as requested