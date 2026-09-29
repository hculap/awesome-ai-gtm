# Contributing Guidelines

Thank you for considering contributing to the Awesome AI GTM Stack! Your contributions help make this resource more valuable for the community.

## How to Contribute

### Adding a New AI Agent/Tool

1. **Fork the repository** and create a new branch for your contribution
2. **Follow the format**: `- [Tool Name](https://example.com/) - Brief description of what it does`
3. **Place in the correct category** based on the GTM funnel stage
4. **Use the canonical URL** and keep entries alphabetical within their category
5. **Ensure quality**: Only suggest tools that are:
   - Actually AI-powered (not just regular software)
   - Relevant to GTM/sales/marketing workflows
   - Currently available and functional
   - Provide clear value for building autonomous business processes

### Updating Existing Entries

- **Pricing changes**: Update if pricing model has significantly changed
- **Feature updates**: Add new AI features that enhance the tool's capabilities
- **Broken links**: Fix any non-functional URLs
- **Better descriptions**: Improve clarity and accuracy of descriptions
- **Category corrections**: Place tools where their primary GTM workflow fits best
- **Workflow examples**: Add new integration examples or use cases

### Guidelines for Descriptions

- Keep descriptions concise (1-2 lines max, ≤ 100 characters)
- Focus on the AI capabilities and business value
- Mention key differentiators and unique features
- Use consistent formatting and tone
- Avoid marketing language - be factual and helpful
- Describe released, documented capabilities and avoid unsupported performance claims
- Highlight GTM-specific use cases when applicable

## Quality Standards

### What to Include
✅ AI agents that automate GTM workflows  
✅ Tools with significant AI/ML capabilities  
✅ Solutions that integrate well with business processes  
✅ Platforms that provide clear ROI for GTM activities  
✅ Open-source AI tools with commercial viability  
✅ Emerging AI technologies with proven GTM applications  

### What NOT to Include
❌ Generic AI tools without specific GTM use cases  
❌ Tools that are discontinued or in beta without clear launch plans  
❌ Overly expensive enterprise-only solutions without clear value  
❌ Tools that duplicate existing entries without clear differentiation  
❌ AI tools that are purely research/academic without business applications  
❌ Tools with poor user reviews or significant reliability issues  

## Submission Process

1. **Check for duplicates** - Make sure the tool isn't already listed
2. **Test the tool** - Ensure it works as described (at least the free tier)
3. **Write a clear description** - Follow the format of existing entries
4. **Regenerate the dashboard** - Run `python3 scripts/update_dashboard.py` and include `DASHBOARD.md` in your PR
5. **Submit a pull request** with:
   - Clear title describing what you're adding/changing
   - Brief explanation of why this tool should be included
   - Evidence of the tool's effectiveness (if available)
   - Any workflow examples or integration use cases
   - Your affiliation with the product, if any

Before submitting, run:

```sh
python3 scripts/update_dashboard.py
python3 scripts/update_dashboard.py --check
git diff --check
```

The dashboard check runs in CI. Keep the generated statistics consistent with your README changes.

## Categories

Make sure to place entries in the correct category:

- **Genesis Stage**: Ideation, market research, business planning
- **Attraction Stage**: SEO, content creation, marketing
- **Conversion Stage**: Lead generation, outreach, scheduling
- **Closing Stage**: Pipeline management, customer support

## Review Process

- All submissions are reviewed for quality and relevance
- We may request changes or additional information
- Reviews typically take 1-3 days
- We appreciate your patience and constructive feedback

## Code of Conduct

- Be respectful and constructive in all interactions
- Focus on helping others discover valuable AI tools
- Avoid promotional language or spam
- Report any issues or concerns to the maintainers

## Questions?

Feel free to open an issue if you have questions about contributing or need clarification on any guidelines.

Thank you for helping build the most comprehensive resource for AI-powered GTM tools! 🚀 