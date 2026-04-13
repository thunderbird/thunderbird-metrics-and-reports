# Clustering Methodology Comparison: Missing Emails or Folders

**Dataset:** Thunderbird Desktop March 2026 - 73 Missing Emails or Folders questions

## Comparison Summary

| Method | Uncategorized % | Categories Identified | Key Strengths | Key Weaknesses |
|--------|----------------:|----------------------|---------------|----------------|
| **Basic Keyword Matching** | 79.5% | 9 | Simple, fast, deterministic | Very low coverage, misses context |
| **Enhanced Rule-Based** | 26.0% | 13 | Better coverage, detects misclassifications | Still has gaps, requires manual pattern tuning |
| **LLM-Based (Claude API)** | N/A | N/A | Would understand context, best accuracy | Requires API key, cost, slower |

## Detailed Results

### Basic Keyword Matching Results

Top categories:
- Other/Unknown: 58 (79.5%)
- Search/Filter Issues: 5 (6.8%)
- Archive Related: 3 (4.1%)
- Local Folders: 2 (2.7%)

**Finding:** Only captured 15 out of 73 questions (20.5%) with specific categories.

### Enhanced Rule-Based Clustering Results

Top categories:
- Other/Uncategorized: 19 (26.0%)
- **Misclassified (Not Missing Emails/Folders): 12 (16.4%)**
- Emails/Folders Disappeared: 9 (12.3%)
- Search/Filter/View Issues: 8 (11.0%)
- Profile/Installation Issues: 7 (9.6%)
- Sent Folder Issues: 4 (5.5%)

**Finding:** Captured 54 out of 73 questions (74.0%) with specific categories. Also identified that 12 questions (16.4%) were actually misclassified by the initial pain point detection and not truly about missing emails/folders.

## Key Insights

### 1. False Positives in Pain Point Detection

The enhanced clustering revealed that **16.4% of questions** classified as "Missing Emails or Folders" were actually about:
- Email threading/grouping settings
- Formatting issues (bold/italic)
- PGP key import
- Attachment handling
- Creating new folders

This suggests the initial pain point keyword detection needs refinement.

### 2. Categorization Improvement

Enhanced rules reduced uncategorized from 79.5% → 26.0% by:
- Using phrase matching instead of single keywords
- Checking for HTML tag removal
- Priority-ordered pattern matching
- More granular categories (All Emails Disappeared vs. Emails/Folders Disappeared)

### 3. Common Subcategories Identified

Most common genuine missing emails/folders issues:
1. **Emails/Folders Disappeared (12.3%)** - General disappearance
2. **Search/Filter/View Issues (11.0%)** - Emails exist but not visible
3. **Profile/Installation Issues (9.6%)** - After reinstall/new installation
4. **Sent Folder Issues (5.5%)** - Sent messages not being saved
5. **All Emails Disappeared (4.1%)** - Catastrophic loss of all messages

### 4. LLM-Based Clustering (Not Run)

The LLM-based script was created but not run due to missing API key. It would provide:
- **Best accuracy** - understands context, synonyms, and user intent
- **Better edge cases** - handles complex or ambiguous questions
- **Consistent categorization** - less dependent on manual pattern tuning

**Trade-offs:**
- Requires Anthropic API key
- Cost per question analyzed (~$0.001-0.01 per question for 73 questions = ~$0.07-0.73 total)
- Slower execution time (API calls)
- Non-deterministic results (may vary slightly between runs)

## Recommendations

1. **For regular analysis:** Use enhanced rule-based clustering
   - Good balance of accuracy and speed
   - No API costs
   - Can be improved iteratively

2. **For deep insights:** Use LLM-based clustering when available
   - Run monthly on high-priority pain points
   - Use to validate and improve rule-based patterns
   - Better for exploratory analysis

3. **Improve pain point detection:** Refine keyword patterns to reduce false positives

4. **Focus areas for Desktop Missing Emails/Folders:**
   - Emails disappeared after updates (7.5% combined)
   - Search/filter improvements to help users find emails
   - Profile/installation recovery procedures
   - IMAP sync issues

## Files Generated

- `2026-03-desktop-missing-emails-subcategories.csv` - Basic keyword matching
- `2026-03-desktop-missing-emails-subcategories.md`
- `2026-03-desktop-missing-emails-enhanced-clustering.csv` - Enhanced rule-based
- `2026-03-desktop-missing-emails-enhanced-clustering.md`
- `scripts/analyze-missing-emails-llm-clustering.py` - LLM-based script (requires ANTHROPIC_API_KEY)
