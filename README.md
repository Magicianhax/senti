# SentientAGI Twitter Agent 🤖

An intelligent Twitter bot with deep knowledge of SentientAGI's GRID ecosystem, designed for authentic community engagement and education about open-source AGI.

## 🎯 What This Agent Does

- **Posts hourly** about SentientAGI and GRID (110+ partners network)
- **Monitors team members** and responds to their tweets within 30 minutes  
- **Answers mentions** with comprehensive knowledge about open-source AGI
- **Educates community** about $SENT tokenomics and Sentient Chat

## 🧠 Knowledge Base

The agent has deep understanding of:
- **GRID**: Global Research and Intelligence Directory with 110+ partners
- **Partners**: Napkin, Exa, Caldo, Kaito, Messari Co-Pilot, The Graph, EigenLayer
- **Products**: Sentient Chat, Dobby LLM, Model Fingerprinting, Open Deep Search
- **Mission**: Open-source AGI competing with OpenAI, Anthropic, Google
- **Token Economy**: $SENT staking, yield farming, revenue to builders

## 🚀 Quick Start

### 1. Setup Environment
```bash
git clone https://github.com/Magicianhax/senti.git
cd senti
pip install -r requirements.txt
```

### 2. Configure API Keys
Create `.env` file:
```env
MODEL_API_KEY=your_fireworks_ai_key
TWITTER_CONSUMER_KEY=your_key
TWITTER_CONSUMER_SECRET=your_secret  
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_TOKEN_SECRET=your_token_secret
TWITTER_BEARER_TOKEN=your_bearer_token
```

### 3. Get Twitter API Access
1. Visit [Twitter Developer Portal](https://developer.x.com/en/portal/dashboard)
2. Create app with "Read and write" permissions
3. Set app type to "Web App, Automated App or Bot"
4. Generate all keys and add to `.env`

### 4. Run the Agent
```bash
python -m src.agent
```

## ⚙️ Configuration

### Monitored Accounts
- `@SentientAGI` - Main project account
- `@hstyagi` - Himanshu Tyagi (Co-founder)  
- `@0xsachi` - Miss Sentient
- `@oleg_golev` - Oleg Golev (Product Lead)
- `@vivekkolli` - Vivek Kolli

### Behavior Settings
- **Checks every**: 30 minutes (48 times/day)
- **Posts tweets**: Every hour (24 posts/day)
- **Max responses**: 1 per check
- **Rate limit**: Built-in protection

## 📊 Example Interactions

**Original Post**: *"GRID isn't just another AI model - it's a network of 110+ specialized intelligences working together. Queries get split, routed to the right tools, then merged for AGI-level results. This is how open-source AGI actually scales."*

**Team Reply**: *"Exactly! While OpenAI builds in closed rooms, GRID reflects work of thousands of open-source developers. Revenue flows back to builders, not shareholders."*

**Mention Response**: *"@user GRID has 50+ specialized agents, 50+ data providers, and 6 AI models. Partners include Exa for web search, Kaito for crypto data, and The Graph for blockchain indexing. All accessible through Sentient Chat!"*

## 🔧 Customization

Edit `src/agent/agent_tools/twitter/twitter_config.py` to:
- Change monitored users
- Adjust posting frequency  
- Modify response prompts
- Add custom knowledge

## ⚠️ API Limits

**Twitter Free Tier**: 100 reads/month, 500 writes/month
**Agent Usage**: ~1440 reads/month, ~720 writes/month  
**Recommendation**: Upgrade to Twitter Basic plan ($100/month)

## 🤝 Contributing

1. Fork this repository
2. Add your own knowledge and prompts
3. Test with your Twitter account
4. Submit pull request with improvements

## 🌟 About SentientAGI

Building the world's first open and community-built AGI.

- **Website**: [sentient.xyz](https://sentient.xyz/)
- **GRID**: [grid.sentient.xyz](https://grid.sentient.xyz/)  
- **Chat**: [chat.sentient.xyz](https://chat.sentient.xyz/)
- **Twitter**: [@SentientAGI](https://twitter.com/SentientAGI)

---

*Built for the open-source AGI community 🚀*