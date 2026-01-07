"""
Sample data for MindDump mock API.
Contains 50+ notes, folders, concepts, statuses, and purposes.
"""

import uuid
from datetime import datetime, timedelta
from typing import Optional
import random

# ============================================================================
# Helper Functions
# ============================================================================

def generate_uuid() -> str:
    return str(uuid.uuid4())

def iso_date(days_ago: int = 0, hours_ago: int = 0) -> str:
    dt = datetime.now() - timedelta(days=days_ago, hours=hours_ago)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

# ============================================================================
# Statuses
# ============================================================================

STATUS_ACTIVE_ID = generate_uuid()
STATUS_ARCHIVED_ID = generate_uuid()
STATUS_DELETED_ID = generate_uuid()

statuses = [
    {"id": STATUS_ACTIVE_ID, "name": "active"},
    {"id": STATUS_ARCHIVED_ID, "name": "archived"},
    {"id": STATUS_DELETED_ID, "name": "deleted"},
]

# ============================================================================
# Purposes
# ============================================================================

PURPOSE_WORK_ID = generate_uuid()
PURPOSE_PERSONAL_ID = generate_uuid()
PURPOSE_LEARNING_ID = generate_uuid()
PURPOSE_IDEAS_ID = generate_uuid()
PURPOSE_TASKS_ID = generate_uuid()

purposes = [
    {"id": PURPOSE_WORK_ID, "name": "work", "description": "Work-related notes"},
    {"id": PURPOSE_PERSONAL_ID, "name": "personal", "description": "Personal notes and reflections"},
    {"id": PURPOSE_LEARNING_ID, "name": "learning", "description": "Learning and study notes"},
    {"id": PURPOSE_IDEAS_ID, "name": "ideas", "description": "Creative ideas and brainstorming"},
    {"id": PURPOSE_TASKS_ID, "name": "tasks", "description": "Tasks and to-do items"},
]

# ============================================================================
# Concepts
# ============================================================================

CONCEPT_IDS = {
    "project_management": generate_uuid(),
    "software_development": generate_uuid(),
    "design": generate_uuid(),
    "productivity": generate_uuid(),
    "personal_growth": generate_uuid(),
    "health": generate_uuid(),
    "finance": generate_uuid(),
    "travel": generate_uuid(),
    "startup_ideas": generate_uuid(),
    "ai_ml": generate_uuid(),
    "mobile_apps": generate_uuid(),
    "web_development": generate_uuid(),
}

concepts = [
    {
        "id": CONCEPT_IDS["project_management"],
        "concept_text": "Project Management",
        "normalized_name": "project_management",
        "weight": 0.85,
        "creation_date": iso_date(180),
        "last_update": iso_date(5),
        "notes_count": 12,
    },
    {
        "id": CONCEPT_IDS["software_development"],
        "concept_text": "Software Development",
        "normalized_name": "software_development",
        "weight": 0.92,
        "creation_date": iso_date(180),
        "last_update": iso_date(2),
        "notes_count": 18,
    },
    {
        "id": CONCEPT_IDS["design"],
        "concept_text": "Design",
        "normalized_name": "design",
        "weight": 0.75,
        "creation_date": iso_date(150),
        "last_update": iso_date(10),
        "notes_count": 8,
    },
    {
        "id": CONCEPT_IDS["productivity"],
        "concept_text": "Productivity",
        "normalized_name": "productivity",
        "weight": 0.68,
        "creation_date": iso_date(120),
        "last_update": iso_date(3),
        "notes_count": 15,
    },
    {
        "id": CONCEPT_IDS["personal_growth"],
        "concept_text": "Personal Growth",
        "normalized_name": "personal_growth",
        "weight": 0.72,
        "creation_date": iso_date(160),
        "last_update": iso_date(7),
        "notes_count": 10,
    },
    {
        "id": CONCEPT_IDS["health"],
        "concept_text": "Health & Wellness",
        "normalized_name": "health",
        "weight": 0.55,
        "creation_date": iso_date(140),
        "last_update": iso_date(14),
        "notes_count": 6,
    },
    {
        "id": CONCEPT_IDS["finance"],
        "concept_text": "Finance",
        "normalized_name": "finance",
        "weight": 0.48,
        "creation_date": iso_date(100),
        "last_update": iso_date(20),
        "notes_count": 4,
    },
    {
        "id": CONCEPT_IDS["travel"],
        "concept_text": "Travel",
        "normalized_name": "travel",
        "weight": 0.35,
        "creation_date": iso_date(90),
        "last_update": iso_date(45),
        "notes_count": 3,
    },
    {
        "id": CONCEPT_IDS["startup_ideas"],
        "concept_text": "Startup Ideas",
        "normalized_name": "startup_ideas",
        "weight": 0.78,
        "creation_date": iso_date(80),
        "last_update": iso_date(5),
        "notes_count": 9,
    },
    {
        "id": CONCEPT_IDS["ai_ml"],
        "concept_text": "AI & Machine Learning",
        "normalized_name": "ai_ml",
        "weight": 0.88,
        "creation_date": iso_date(60),
        "last_update": iso_date(1),
        "notes_count": 14,
    },
    {
        "id": CONCEPT_IDS["mobile_apps"],
        "concept_text": "Mobile Apps",
        "normalized_name": "mobile_apps",
        "weight": 0.82,
        "creation_date": iso_date(70),
        "last_update": iso_date(3),
        "notes_count": 11,
    },
    {
        "id": CONCEPT_IDS["web_development"],
        "concept_text": "Web Development",
        "normalized_name": "web_development",
        "weight": 0.65,
        "creation_date": iso_date(110),
        "last_update": iso_date(8),
        "notes_count": 7,
    },
]

# ============================================================================
# Folders
# ============================================================================

FOLDER_IDS = {
    "work": generate_uuid(),
    "projects": generate_uuid(),
    "meetings": generate_uuid(),
    "personal": generate_uuid(),
    "goals": generate_uuid(),
    "ideas": generate_uuid(),
    "learning": generate_uuid(),
    "books": generate_uuid(),
    "courses": generate_uuid(),
}

folders = [
    # Level 1 - Root folders
    {
        "id": FOLDER_IDS["work"],
        "user_id": "user-1",
        "parent_folder_id": None,
        "category_level": 1,
        "concept": {
            "id": CONCEPT_IDS["project_management"],
            "concept_text": "Work",
            "weight": 0.85,
        },
        "percentage": 0.45,
        "creation_date": iso_date(180),
        "last_update": iso_date(1),
        "children_count": 2,
    },
    {
        "id": FOLDER_IDS["personal"],
        "user_id": "user-1",
        "parent_folder_id": None,
        "category_level": 1,
        "concept": {
            "id": CONCEPT_IDS["personal_growth"],
            "concept_text": "Personal",
            "weight": 0.72,
        },
        "percentage": 0.25,
        "creation_date": iso_date(160),
        "last_update": iso_date(5),
        "children_count": 1,
    },
    {
        "id": FOLDER_IDS["ideas"],
        "user_id": "user-1",
        "parent_folder_id": None,
        "category_level": 1,
        "concept": {
            "id": CONCEPT_IDS["startup_ideas"],
            "concept_text": "Ideas",
            "weight": 0.78,
        },
        "percentage": 0.15,
        "creation_date": iso_date(80),
        "last_update": iso_date(3),
        "children_count": 0,
    },
    {
        "id": FOLDER_IDS["learning"],
        "user_id": "user-1",
        "parent_folder_id": None,
        "category_level": 1,
        "concept": {
            "id": CONCEPT_IDS["ai_ml"],
            "concept_text": "Learning",
            "weight": 0.88,
        },
        "percentage": 0.15,
        "creation_date": iso_date(100),
        "last_update": iso_date(2),
        "children_count": 2,
    },
    # Level 2 - Work subfolders
    {
        "id": FOLDER_IDS["projects"],
        "user_id": "user-1",
        "parent_folder_id": FOLDER_IDS["work"],
        "category_level": 2,
        "concept": {
            "id": CONCEPT_IDS["software_development"],
            "concept_text": "Projects",
            "weight": 0.92,
        },
        "percentage": 0.60,
        "creation_date": iso_date(150),
        "last_update": iso_date(1),
        "children_count": 0,
    },
    {
        "id": FOLDER_IDS["meetings"],
        "user_id": "user-1",
        "parent_folder_id": FOLDER_IDS["work"],
        "category_level": 2,
        "concept": {
            "id": CONCEPT_IDS["project_management"],
            "concept_text": "Meetings",
            "weight": 0.75,
        },
        "percentage": 0.40,
        "creation_date": iso_date(140),
        "last_update": iso_date(2),
        "children_count": 0,
    },
    # Level 2 - Personal subfolders
    {
        "id": FOLDER_IDS["goals"],
        "user_id": "user-1",
        "parent_folder_id": FOLDER_IDS["personal"],
        "category_level": 2,
        "concept": {
            "id": CONCEPT_IDS["productivity"],
            "concept_text": "Goals",
            "weight": 0.68,
        },
        "percentage": 1.0,
        "creation_date": iso_date(120),
        "last_update": iso_date(7),
        "children_count": 0,
    },
    # Level 2 - Learning subfolders
    {
        "id": FOLDER_IDS["books"],
        "user_id": "user-1",
        "parent_folder_id": FOLDER_IDS["learning"],
        "category_level": 2,
        "concept": {
            "id": CONCEPT_IDS["personal_growth"],
            "concept_text": "Books",
            "weight": 0.65,
        },
        "percentage": 0.50,
        "creation_date": iso_date(90),
        "last_update": iso_date(10),
        "children_count": 0,
    },
    {
        "id": FOLDER_IDS["courses"],
        "user_id": "user-1",
        "parent_folder_id": FOLDER_IDS["learning"],
        "category_level": 2,
        "concept": {
            "id": CONCEPT_IDS["ai_ml"],
            "concept_text": "Courses",
            "weight": 0.88,
        },
        "percentage": 0.50,
        "creation_date": iso_date(85),
        "last_update": iso_date(5),
        "children_count": 0,
    },
]

# ============================================================================
# Notes (50+ varied notes)
# ============================================================================

USER_ID = "user-1"

# Helper to create note
def create_note(
    title: str,
    content: str,
    days_ago: int,
    priority: int = 0,
    status_id: str = STATUS_ACTIVE_ID,
    language: str = "en",
    concept_ids: list = None,
    purpose_ids: list = None,
    processed_data: dict = None,
) -> dict:
    note_id = generate_uuid()
    word_count = len(content.split())

    concepts_list = None
    if concept_ids:
        concepts_list = [
            {
                "id": cid,
                "concept_text": next((c["concept_text"] for c in concepts if c["id"] == cid), "Unknown"),
                "weight": round(random.uniform(0.5, 0.95), 2),
            }
            for cid in concept_ids
        ]

    purposes_list = None
    if purpose_ids:
        purposes_list = [
            {
                "id": pid,
                "name": next((p["name"] for p in purposes if p["id"] == pid), "unknown"),
                "weight": random.randint(3, 10),
            }
            for pid in purpose_ids
        ]

    status = next((s for s in statuses if s["id"] == status_id), None)

    return {
        "id": note_id,
        "user_id": USER_ID,
        "title": title,
        "creation_date": iso_date(days_ago),
        "last_update": iso_date(max(0, days_ago - random.randint(0, 5))),
        "last_open": iso_date(max(0, days_ago - random.randint(0, 3))) if random.random() > 0.3 else None,
        "original_text": content,
        "processed_data": processed_data,
        "language": language,
        "priority": priority,
        "status": {"id": status["id"], "name": status["name"]} if status else None,
        "word_count": word_count,
        "concepts": concepts_list,
        "purposes": purposes_list,
        "folder_id": None,
    }

# Work/Projects Notes (15)
notes = [
    create_note(
        title="Q1 Planning Meeting Notes",
        content="""Discussed Q1 objectives with the team. Key points:

1. Launch new mobile app by end of February
2. Hire 2 senior developers
3. Migrate database to new infrastructure
4. Implement CI/CD pipeline improvements

Action items assigned to team leads. Follow-up meeting scheduled for next Monday.
Budget approved for cloud infrastructure upgrades.""",
        days_ago=45,
        priority=3,
        concept_ids=[CONCEPT_IDS["project_management"], CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_WORK_ID],
        processed_data={
            "summary": "Q1 planning meeting covering app launch, hiring, and infrastructure",
            "key_points": ["App launch February", "Hire 2 developers", "Database migration", "CI/CD improvements"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="Code Review: Authentication Module",
        content="""Reviewed the new authentication module implementation.

Positives:
- Clean separation of concerns
- Good use of dependency injection
- Comprehensive unit tests

Areas for improvement:
- Token refresh logic could be simplified
- Add retry mechanism for network failures
- Consider using Keychain for token storage instead of UserDefaults

Overall: Approved with minor changes requested.""",
        days_ago=12,
        priority=2,
        concept_ids=[CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_WORK_ID],
        processed_data={
            "summary": "Authentication module code review - approved with minor changes",
            "key_points": ["Clean architecture", "Good tests", "Token refresh needs work"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="Sprint Retrospective - Week 48",
        content="""What went well:
- Completed all planned stories
- Good collaboration between frontend and backend teams
- New testing framework saved us significant debugging time

What could be improved:
- Too many meetings on Wednesdays
- Need better documentation for API changes
- Deployment process still has manual steps

Action items:
- Move some meetings to async updates
- Implement API changelog automation
- Script remaining deployment steps""",
        days_ago=8,
        priority=1,
        concept_ids=[CONCEPT_IDS["project_management"]],
        purpose_ids=[PURPOSE_WORK_ID],
    ),
    create_note(
        title="API Design Discussion",
        content="""Met with backend team to discuss new API design.

REST vs GraphQL debate:
- REST: Simpler, better caching, team familiarity
- GraphQL: Flexible queries, reduced over-fetching

Decision: Use REST for MVP, evaluate GraphQL for v2.

Pagination approach: Cursor-based for better performance with large datasets.
Authentication: JWT with refresh tokens.
Rate limiting: 100 req/min for authenticated users.""",
        days_ago=20,
        priority=2,
        concept_ids=[CONCEPT_IDS["software_development"], CONCEPT_IDS["web_development"]],
        purpose_ids=[PURPOSE_WORK_ID],
        processed_data={
            "summary": "API design decisions - REST for MVP, cursor pagination, JWT auth",
            "key_points": ["REST over GraphQL for MVP", "Cursor-based pagination", "JWT authentication"],
            "sentiment": "neutral",
        },
    ),
    create_note(
        title="Performance Optimization Results",
        content="""Completed performance audit of the iOS app.

Before optimization:
- App launch: 3.2 seconds
- List scroll: 45 FPS average
- Memory usage: 180MB

After optimization:
- App launch: 1.4 seconds (56% faster)
- List scroll: 60 FPS constant
- Memory usage: 95MB (47% reduction)

Key changes:
1. Lazy loading of images
2. View model caching
3. Background data prefetching
4. Memory pool for cell reuse""",
        days_ago=5,
        priority=3,
        concept_ids=[CONCEPT_IDS["mobile_apps"], CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_WORK_ID],
        processed_data={
            "summary": "iOS app performance improved by 56% launch time and 47% memory reduction",
            "key_points": ["Launch time: 3.2s to 1.4s", "Constant 60 FPS", "Memory: 180MB to 95MB"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="Team Standup Notes - December",
        content="""Daily standup summary for the week:

Monday: Sprint planning, assigned new features
Tuesday: Blocked on API changes, waiting for backend
Wednesday: API ready, resumed development
Thursday: Demo preparation, bug fixes
Friday: Sprint demo, stakeholder feedback positive

Velocity this sprint: 34 points (target: 30)
Carried over: 2 minor bugs to next sprint""",
        days_ago=3,
        priority=1,
        concept_ids=[CONCEPT_IDS["project_management"]],
        purpose_ids=[PURPOSE_WORK_ID],
    ),
    create_note(
        title="Architecture Decision Record: State Management",
        content="""ADR-005: State Management Approach

Context:
Need consistent state management for iOS app with SwiftUI.

Decision:
Use @Observable macro (iOS 17+) with MVVM pattern.

Rationale:
- Native SwiftUI integration
- Fine-grained reactivity
- Simpler than Combine
- No third-party dependencies

Consequences:
- Minimum iOS 17 required
- Team needs training on new patterns
- Migration from ObservableObject needed""",
        days_ago=30,
        priority=2,
        concept_ids=[CONCEPT_IDS["software_development"], CONCEPT_IDS["mobile_apps"]],
        purpose_ids=[PURPOSE_WORK_ID],
        processed_data={
            "summary": "Architecture decision to use @Observable for state management",
            "key_points": ["@Observable macro", "MVVM pattern", "iOS 17 minimum"],
            "sentiment": "neutral",
        },
    ),
    create_note(
        title="Client Feedback - Beta Testing",
        content="""Collected feedback from beta testers:

Positive:
- "Love the clean interface"
- "Voice dictation works great"
- "Fast and responsive"

Issues reported:
- Dark mode requested (5 users)
- Search not finding partial matches (3 users)
- Want to organize notes in folders (7 users)

Priority for next release:
1. Folder organization (high demand)
2. Improved search
3. Dark mode support""",
        days_ago=7,
        priority=3,
        concept_ids=[CONCEPT_IDS["design"], CONCEPT_IDS["mobile_apps"]],
        purpose_ids=[PURPOSE_WORK_ID],
        processed_data={
            "summary": "Beta feedback: positive reception, folder organization most requested",
            "key_points": ["Clean interface praised", "Folder organization requested", "Dark mode wanted"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="Database Migration Plan",
        content="""Migration from SQLite to PostgreSQL for backend.

Phase 1 (Week 1-2):
- Set up PostgreSQL infrastructure
- Create migration scripts
- Parallel write to both databases

Phase 2 (Week 3):
- Verify data consistency
- Switch read operations to PostgreSQL
- Monitor performance

Phase 3 (Week 4):
- Decommission SQLite
- Clean up migration code
- Document new architecture

Rollback plan: Keep SQLite backup for 30 days.""",
        days_ago=15,
        priority=2,
        concept_ids=[CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_WORK_ID],
    ),
    create_note(
        title="Security Audit Findings",
        content="""Third-party security audit completed.

Critical (0 issues) -
High (1 issue):
- API tokens stored in UserDefaults instead of Keychain
  Status: Fixed in v1.2.1

Medium (3 issues):
- Missing rate limiting on some endpoints
- Debug logs contain sensitive data
- Certificate pinning not implemented

Low (5 issues):
- Various minor improvements

Timeline: All high/medium issues to be resolved by end of month.""",
        days_ago=10,
        priority=4,
        concept_ids=[CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_WORK_ID],
        processed_data={
            "summary": "Security audit: 0 critical, 1 high (fixed), 3 medium issues",
            "key_points": ["Token storage fixed", "Rate limiting needed", "Certificate pinning pending"],
            "sentiment": "neutral",
        },
    ),
    create_note(
        title="Feature Spec: Voice Commands",
        content="""Voice Commands Feature Specification

User Story:
As a user, I want to control the app with voice commands so I can use it hands-free.

Commands to support:
- "New note" - Create blank note
- "Save" - Save current note
- "Read note" - Text-to-speech
- "Search for [term]" - Search notes

Technical approach:
- Use Speech framework for recognition
- Local processing only (privacy)
- Fallback to touch for complex operations

MVP scope: New note and Save commands only.""",
        days_ago=25,
        priority=2,
        concept_ids=[CONCEPT_IDS["mobile_apps"], CONCEPT_IDS["ai_ml"]],
        purpose_ids=[PURPOSE_WORK_ID, PURPOSE_IDEAS_ID],
    ),
    create_note(
        title="Deployment Checklist v1.3",
        content="""Pre-deployment:
[ ] All tests passing
[ ] Code review approved
[ ] QA sign-off received
[ ] Release notes prepared
[ ] App Store screenshots updated

Deployment:
[ ] Create release branch
[ ] Bump version number
[ ] Archive and upload to App Store Connect
[ ] Submit for review

Post-deployment:
[ ] Monitor crash reports
[ ] Check analytics
[ ] Respond to user reviews
[ ] Update documentation""",
        days_ago=2,
        priority=3,
        concept_ids=[CONCEPT_IDS["software_development"], CONCEPT_IDS["project_management"]],
        purpose_ids=[PURPOSE_WORK_ID, PURPOSE_TASKS_ID],
    ),
    create_note(
        title="Meeting: Product Roadmap Review",
        content="""Quarterly roadmap review with stakeholders.

Current quarter achievements:
- MVP launched successfully
- 10K downloads first month
- 4.5 star average rating

Next quarter priorities:
1. Collaboration features
2. Cloud sync
3. iPad app
4. Premium subscription

Budget approved for additional developer.
Marketing push planned for February.""",
        days_ago=14,
        priority=2,
        concept_ids=[CONCEPT_IDS["project_management"]],
        purpose_ids=[PURPOSE_WORK_ID],
        processed_data={
            "summary": "Roadmap review: MVP success, focusing on collaboration and cloud sync next",
            "key_points": ["10K downloads", "4.5 star rating", "Collaboration next priority"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="Technical Debt Inventory",
        content="""Current technical debt items:

High priority:
- Refactor NotesViewModel (too many responsibilities)
- Remove deprecated API calls
- Update to latest Swift concurrency patterns

Medium priority:
- Consolidate duplicate networking code
- Improve error handling consistency
- Add missing unit tests for edge cases

Low priority:
- Code style inconsistencies
- Unused imports
- Documentation gaps

Estimate: 2 sprints to address high priority items.""",
        days_ago=18,
        priority=2,
        concept_ids=[CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_WORK_ID],
    ),
    create_note(
        title="Interview Notes: Senior iOS Developer",
        content="""Candidate: Alex M.
Position: Senior iOS Developer

Technical assessment:
- Strong Swift knowledge
- Good understanding of SwiftUI
- Experience with large-scale apps
- Clean coding style

Culture fit:
- Collaborative attitude
- Good communication
- Interested in mentoring

Concerns:
- Limited experience with our tech stack
- Salary expectations above budget

Recommendation: Strong hire, negotiate on salary.""",
        days_ago=6,
        priority=2,
        concept_ids=[CONCEPT_IDS["project_management"]],
        purpose_ids=[PURPOSE_WORK_ID],
    ),
]

# Personal Notes (10)
notes.extend([
    create_note(
        title="2024 Goals Reflection",
        content="""Looking back at this year's goals:

Achieved:
- Read 24 books (goal was 20)
- Ran first half marathon
- Learned SwiftUI
- Saved emergency fund

Partially achieved:
- Meditation habit (inconsistent)
- Side project (started but not finished)

Missed:
- Learn a new language
- Travel to Japan

Overall: Good year! Focus on consistency next year.""",
        days_ago=35,
        priority=2,
        concept_ids=[CONCEPT_IDS["personal_growth"], CONCEPT_IDS["productivity"]],
        purpose_ids=[PURPOSE_PERSONAL_ID],
        processed_data={
            "summary": "2024 goal reflection - most goals achieved, focus on consistency for 2025",
            "key_points": ["24 books read", "Half marathon completed", "Learned SwiftUI"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="Morning Routine Experiment",
        content="""Testing new morning routine for 30 days.

5:30 - Wake up
5:35 - 10 min meditation
5:45 - 30 min exercise
6:15 - Shower
6:30 - Healthy breakfast
7:00 - Planning/journaling
7:30 - Deep work begins

Week 1 observations:
- Hard to wake up early first 3 days
- More productive mornings
- Energy dip around 2pm
- Going to bed earlier naturally

Will continue and adjust.""",
        days_ago=22,
        priority=1,
        concept_ids=[CONCEPT_IDS["productivity"], CONCEPT_IDS["health"]],
        purpose_ids=[PURPOSE_PERSONAL_ID],
    ),
    create_note(
        title="Journal: Career Thoughts",
        content="""Feeling restless about career direction lately.

Things I enjoy:
- Building products people use
- Solving complex problems
- Mentoring junior developers
- Learning new technologies

Things draining me:
- Too many meetings
- Slow decision-making
- Limited growth opportunities

Options to consider:
1. Talk to manager about role change
2. Look for new opportunities
3. Start building side projects more seriously

Need to reflect more on what I truly want.""",
        days_ago=40,
        priority=2,
        concept_ids=[CONCEPT_IDS["personal_growth"]],
        purpose_ids=[PURPOSE_PERSONAL_ID],
        processed_data={
            "summary": "Career reflection - enjoying building products, considering changes",
            "key_points": ["Enjoys building products", "Too many meetings", "Considering options"],
            "sentiment": "neutral",
        },
    ),
    create_note(
        title="Gratitude List - December",
        content="""Things I'm grateful for this month:

1. Health and energy to pursue my goals
2. Supportive family and friends
3. Meaningful work that challenges me
4. Cozy home during winter
5. Good books that inspire me
6. Morning coffee ritual
7. Weekend hikes with friends
8. Progress on personal projects
9. Learning opportunities at work
10. The ability to help others

Focusing on gratitude helps perspective.""",
        days_ago=5,
        priority=0,
        concept_ids=[CONCEPT_IDS["personal_growth"]],
        purpose_ids=[PURPOSE_PERSONAL_ID],
    ),
    create_note(
        title="Book Notes: Atomic Habits",
        content="""Key takeaways from Atomic Habits by James Clear:

1. Habits are compound interest of self-improvement
2. Focus on systems, not goals
3. Four laws of behavior change:
   - Make it obvious
   - Make it attractive
   - Make it easy
   - Make it satisfying

4. Identity-based habits > outcome-based habits
5. Environment design matters more than motivation
6. Habit stacking: attach new habits to existing ones

Favorite quote: "You do not rise to the level of your goals. You fall to the level of your systems."

Will apply: Habit stacking for morning routine.""",
        days_ago=55,
        priority=1,
        concept_ids=[CONCEPT_IDS["personal_growth"], CONCEPT_IDS["productivity"]],
        purpose_ids=[PURPOSE_PERSONAL_ID, PURPOSE_LEARNING_ID],
        processed_data={
            "summary": "Atomic Habits book notes - focus on systems and identity-based habits",
            "key_points": ["Four laws of behavior change", "Systems over goals", "Environment design"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="Fitness Progress Tracker",
        content="""Weekly fitness log:

Week of Dec 15:
- Mon: 5K run (27:30)
- Tue: Upper body strength
- Wed: Rest day
- Thu: 7K run (38:45)
- Fri: Lower body strength
- Sat: 10K run (54:20) - new PR!
- Sun: Active recovery (yoga)

Notes:
- Feeling stronger on hills
- Need to stretch more post-run
- Sleep affecting recovery

Next week: Focus on speed work.""",
        days_ago=8,
        priority=0,
        concept_ids=[CONCEPT_IDS["health"]],
        purpose_ids=[PURPOSE_PERSONAL_ID],
    ),
    create_note(
        title="Budget Review - Q4",
        content="""Quarterly budget analysis:

Income: $12,000
Expenses breakdown:
- Housing: $2,400 (20%)
- Food: $800 (6.7%)
- Transportation: $400 (3.3%)
- Utilities: $200 (1.7%)
- Entertainment: $300 (2.5%)
- Savings: $4,800 (40%)
- Investments: $2,400 (20%)
- Misc: $700 (5.8%)

Observations:
- Exceeded savings goal by 5%
- Food spending higher than planned
- Good progress on investment contributions

Q1 adjustments: Reduce dining out, increase emergency fund.""",
        days_ago=12,
        priority=1,
        concept_ids=[CONCEPT_IDS["finance"]],
        purpose_ids=[PURPOSE_PERSONAL_ID],
    ),
    create_note(
        title="Reflexiones del año",
        content="""Este año ha sido de mucho crecimiento personal y profesional.

Logros principales:
- Ascenso en el trabajo
- Completé maratón
- Aprendí nuevas tecnologías
- Mejoré relaciones familiares

Áreas de mejora:
- Balance trabajo-vida
- Constancia en hábitos
- Paciencia con el proceso

Palabra del año próximo: CONSISTENCIA

Estoy emocionado por lo que viene.""",
        days_ago=3,
        priority=2,
        language="es",
        concept_ids=[CONCEPT_IDS["personal_growth"]],
        purpose_ids=[PURPOSE_PERSONAL_ID],
        processed_data={
            "summary": "Reflexión anual - año de crecimiento, enfoque en consistencia",
            "key_points": ["Ascenso laboral", "Maratón completado", "Palabra 2025: Consistencia"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="Travel Planning: Japan 2025",
        content="""Planning trip to Japan for spring 2025.

Dates: March 25 - April 10 (cherry blossom season)

Itinerary draft:
- Tokyo (5 nights)
  - Shibuya, Shinjuku, Akihabara
  - Day trip to Kamakura
- Kyoto (4 nights)
  - Temples, geisha district
  - Day trip to Nara
- Osaka (3 nights)
  - Food tour
  - Day trip to Hiroshima

Budget estimate: $4,500
- Flights: $1,200
- Hotels: $1,800
- Food/Activities: $1,500

To research: JR Pass, pocket WiFi, money exchange.""",
        days_ago=28,
        priority=1,
        concept_ids=[CONCEPT_IDS["travel"]],
        purpose_ids=[PURPOSE_PERSONAL_ID],
    ),
    create_note(
        title="Weekend Trip Notes",
        content="""Quick getaway to the mountains.

Highlights:
- Beautiful sunrise hike
- Found a great coffee shop
- Finished reading my book
- Good disconnect from screens

Lessons:
- Pack lighter next time
- Bring backup battery
- Book accommodations earlier

Want to do more of these short trips. Good for mental reset.""",
        days_ago=16,
        priority=0,
        concept_ids=[CONCEPT_IDS["travel"], CONCEPT_IDS["health"]],
        purpose_ids=[PURPOSE_PERSONAL_ID],
    ),
])

# Ideas Notes (10)
notes.extend([
    create_note(
        title="App Idea: Habit Tracker with AI",
        content="""Concept: AI-powered habit tracking app

Core features:
- Track daily habits
- AI analyzes patterns and suggests optimizations
- Predicts habit streaks at risk
- Personalized tips based on behavior

Differentiators:
- Machine learning for predictions
- Integration with health data
- Smart notifications (learns best time)
- Gamification with meaning

Monetization: Freemium with AI features as premium

Competition: Habitify, Streaks, HabitBull
Our edge: Predictive AI and personalization

Next steps: Build prototype, test with 10 users.""",
        days_ago=50,
        priority=3,
        concept_ids=[CONCEPT_IDS["startup_ideas"], CONCEPT_IDS["ai_ml"], CONCEPT_IDS["mobile_apps"]],
        purpose_ids=[PURPOSE_IDEAS_ID],
        processed_data={
            "summary": "AI habit tracker app idea with predictive features",
            "key_points": ["AI pattern analysis", "Streak predictions", "Freemium model"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="Blog Post Ideas",
        content="""Technical blog post ideas to write:

1. "SwiftUI Performance: Lessons from Building a Real App"
   - Practical optimization tips
   - Before/after benchmarks

2. "From ObservableObject to @Observable: Migration Guide"
   - Step-by-step process
   - Common pitfalls

3. "Building a Design System in Swift"
   - Tokens, components, theming
   - Code examples

4. "Local-First Architecture for iOS Apps"
   - Offline-first design
   - Sync strategies

5. "Voice Input: Beyond Basic Dictation"
   - Speech framework deep dive
   - Real-time transcription

Priority: Start with #2, most timely.""",
        days_ago=20,
        priority=1,
        concept_ids=[CONCEPT_IDS["software_development"], CONCEPT_IDS["mobile_apps"]],
        purpose_ids=[PURPOSE_IDEAS_ID],
    ),
    create_note(
        title="Product Feature Brainstorm",
        content="""Brainstorming session for MindDump v2:

Organization:
- Nested folders
- Smart folders (auto-categorized)
- Custom tags with colors
- Pin notes to top

Productivity:
- Focus mode (one note at a time)
- Pomodoro timer integration
- Quick capture widget
- Apple Watch companion

AI Features:
- Auto-summarization
- Related notes suggestions
- Sentiment tracking over time
- Voice note transcription improvements

Collaboration:
- Share individual notes
- Collaborative editing
- Comment threads

Voting results from team:
1. Smart folders (8 votes)
2. Focus mode (7 votes)
3. Auto-summarization (6 votes)""",
        days_ago=18,
        priority=2,
        concept_ids=[CONCEPT_IDS["startup_ideas"], CONCEPT_IDS["design"]],
        purpose_ids=[PURPOSE_IDEAS_ID, PURPOSE_WORK_ID],
        processed_data={
            "summary": "MindDump v2 feature brainstorm - smart folders and focus mode top voted",
            "key_points": ["Smart folders top priority", "Focus mode requested", "AI features wanted"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="SaaS Idea: Developer Tools Platform",
        content="""Concept: Unified developer productivity platform

Problem:
- Developers use too many disconnected tools
- Context switching kills productivity
- Hard to track work across tools

Solution: All-in-one platform with:
- Code snippets library
- API testing (like Postman)
- Documentation wiki
- Task management
- Team chat

Integration first approach:
- Connect existing tools (GitHub, Jira, Slack)
- Unified search across all
- AI assistant for common tasks

Target: Small to mid-size dev teams (5-50)
Pricing: $15/user/month

Risk: Too broad, might need to niche down.""",
        days_ago=42,
        priority=2,
        concept_ids=[CONCEPT_IDS["startup_ideas"], CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_IDEAS_ID],
    ),
    create_note(
        title="Idea: AI Writing Assistant for Developers",
        content="""Writing assistant specifically for technical content.

Use cases:
- Documentation generation from code
- README file creation
- Commit message suggestions
- Pull request descriptions
- Technical blog posts

Features:
- Understands code context
- Maintains technical accuracy
- Follows style guides
- Multi-language support

Integrations:
- VS Code extension
- GitHub App
- CLI tool

Competitive advantage:
- Trained specifically on technical content
- Code-aware context
- Developer workflow integration

Market size: 27M developers worldwide
Potential: B2B and individual subscriptions""",
        days_ago=32,
        priority=3,
        concept_ids=[CONCEPT_IDS["startup_ideas"], CONCEPT_IDS["ai_ml"]],
        purpose_ids=[PURPOSE_IDEAS_ID],
        processed_data={
            "summary": "AI writing assistant for developers - documentation and technical content",
            "key_points": ["Code-aware context", "VS Code integration", "B2B potential"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="Design System Ideas",
        content="""Thoughts on improving our design system:

Current pain points:
- Inconsistent spacing across features
- Color tokens too granular
- Typography scale not flexible enough
- Dark mode as afterthought

Proposed improvements:

1. Semantic spacing:
   - compact, default, spacious variants
   - Context-aware (forms, cards, lists)

2. Color simplification:
   - Primary, secondary, tertiary
   - Status colors (success, warning, error)
   - Surface colors only

3. Typography:
   - Three scales: compact, default, large
   - Automatic dark mode adjustments

4. Component library:
   - Atomic design approach
   - Storybook-like previews
   - Usage documentation

Priority: Start with color and spacing refactor.""",
        days_ago=15,
        priority=2,
        concept_ids=[CONCEPT_IDS["design"], CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_IDEAS_ID],
    ),
    create_note(
        title="Idea para app de meditación",
        content="""Concepto: App de meditación para desarrolladores

Características únicas:
- Sesiones cortas (3-5 min) para pausas de código
- Integración con Pomodoro
- Temas relacionados con trabajo: estrés, bloqueos creativos
- Ambiente sonoro de oficina relajante

Diferenciadores:
- Dirigida específicamente a tech workers
- Contenido sobre síndrome del impostor
- Comunidad de developers

Modelo de negocio:
- Gratis: 5 sesiones básicas
- Premium: $4.99/mes - todo el contenido

Validación necesaria: encuesta a 50 developers.""",
        days_ago=38,
        priority=1,
        language="es",
        concept_ids=[CONCEPT_IDS["startup_ideas"], CONCEPT_IDS["mobile_apps"]],
        purpose_ids=[PURPOSE_IDEAS_ID],
    ),
    create_note(
        title="Open Source Project Ideas",
        content="""Open source projects I want to contribute to or create:

Create:
1. SwiftUI component library
   - Common UI patterns
   - Well-documented
   - Accessible by default

2. iOS app template
   - MVVM setup
   - Networking layer
   - Design system scaffold

3. CLI tool for project scaffolding
   - Like create-react-app for iOS
   - Customizable templates

Contribute to:
- SwiftLint (add custom rules)
- Swift Markdown (improve parsing)
- Vapor (documentation)

Goal: Build reputation in Swift community
Timeline: Start with component library in January""",
        days_ago=25,
        priority=1,
        concept_ids=[CONCEPT_IDS["software_development"], CONCEPT_IDS["mobile_apps"]],
        purpose_ids=[PURPOSE_IDEAS_ID],
    ),
    create_note(
        title="Monetization Strategies Comparison",
        content="""Comparing monetization for consumer apps:

1. Subscription (recurring)
   + Predictable revenue
   + High LTV potential
   - Higher churn
   - Needs constant value add

2. One-time purchase
   + Simple, user-friendly
   + No ongoing commitment
   - Revenue plateau
   - Less user loyalty

3. Freemium + IAP
   + Large user base
   + Flexible pricing
   - Complex to balance
   - Can feel exploitative

4. Ads
   + Free for users
   + Easy to implement
   - Poor UX
   - Low revenue per user

For MindDump:
Recommendation: Subscription with meaningful free tier
Reason: Aligns with continuous improvement model""",
        days_ago=48,
        priority=2,
        concept_ids=[CONCEPT_IDS["startup_ideas"], CONCEPT_IDS["finance"]],
        purpose_ids=[PURPOSE_IDEAS_ID, PURPOSE_WORK_ID],
    ),
    create_note(
        title="AI Feature Exploration",
        content="""Exploring AI features for notes app:

1. Smart Tagging
   - Analyze content, suggest tags
   - Learn from user corrections
   - Tech: NLP classification

2. Related Notes
   - Find semantically similar notes
   - Surface connections user missed
   - Tech: Embedding + vector search

3. Summary Generation
   - TL;DR for long notes
   - Key points extraction
   - Tech: Summarization model

4. Writing Assistance
   - Grammar and style suggestions
   - Tone adjustment
   - Tech: LLM integration

5. Voice Enhancement
   - Better transcription
   - Speaker identification
   - Tech: Whisper or similar

Implementation priority based on user value:
1. Smart Tagging (high impact, low complexity)
2. Summary Generation
3. Related Notes
4. Writing Assistance
5. Voice Enhancement""",
        days_ago=10,
        priority=3,
        concept_ids=[CONCEPT_IDS["ai_ml"], CONCEPT_IDS["startup_ideas"]],
        purpose_ids=[PURPOSE_IDEAS_ID],
        processed_data={
            "summary": "AI features exploration for notes app - smart tagging highest priority",
            "key_points": ["Smart tagging priority", "Related notes via embeddings", "LLM writing assistance"],
            "sentiment": "positive",
        },
    ),
])

# Learning Notes (10)
notes.extend([
    create_note(
        title="Course Notes: Machine Learning Fundamentals",
        content="""Week 3: Supervised Learning

Key concepts:
- Linear regression
- Logistic regression
- Decision trees
- Random forests

Linear Regression:
y = mx + b
- m = slope (weight)
- b = intercept (bias)
- Loss function: Mean Squared Error

Logistic Regression:
- For classification problems
- Sigmoid function for probability
- Loss: Binary Cross-Entropy

Homework:
- Implement linear regression from scratch
- Compare with sklearn
- Visualize decision boundary

Questions for next session:
- When to use regularization?
- How to handle multicollinearity?""",
        days_ago=4,
        priority=2,
        concept_ids=[CONCEPT_IDS["ai_ml"]],
        purpose_ids=[PURPOSE_LEARNING_ID],
    ),
    create_note(
        title="Book Summary: Deep Work by Cal Newport",
        content="""Deep Work: Rules for Focused Success in a Distracted World

Core thesis:
Deep work = professional activities performed in distraction-free concentration that push cognitive capabilities to their limit.

Key rules:

1. Work Deeply
   - Schedule deep work blocks
   - Create rituals and routines
   - Use grand gestures when needed

2. Embrace Boredom
   - Train focus like a muscle
   - Don't use internet as reward
   - Productive meditation

3. Quit Social Media
   - Apply craftsman approach
   - 30-day social media fast test

4. Drain the Shallows
   - Schedule every minute
   - Quantify depth of activities
   - Fixed-schedule productivity

My takeaways:
- Block 2 hours each morning for deep work
- Turn off notifications during blocks
- Track deep work hours weekly""",
        days_ago=60,
        priority=1,
        concept_ids=[CONCEPT_IDS["productivity"], CONCEPT_IDS["personal_growth"]],
        purpose_ids=[PURPOSE_LEARNING_ID],
        processed_data={
            "summary": "Deep Work book - focus on distraction-free work and boredom training",
            "key_points": ["Schedule deep work blocks", "Embrace boredom", "Fixed-schedule productivity"],
            "sentiment": "positive",
        },
    ),
    create_note(
        title="SwiftUI Advanced: Custom Layouts",
        content="""Learning custom Layout protocol in SwiftUI.

Layout protocol requirements:
- sizeThatFits(proposal:subviews:cache:)
- placeSubviews(in:proposal:subviews:cache:)

Example: Custom flow layout

struct FlowLayout: Layout {
    var spacing: CGFloat = 8

    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        // Calculate total size needed
    }

    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        // Position each subview
    }
}

Use cases:
- Tag clouds
- Photo grids
- Flexible button groups

Key learnings:
- Cache for performance
- Handle different size proposals
- Respect subview priorities""",
        days_ago=14,
        priority=2,
        concept_ids=[CONCEPT_IDS["mobile_apps"], CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_LEARNING_ID],
    ),
    create_note(
        title="Tutorial: Setting Up CI/CD for iOS",
        content="""Complete CI/CD pipeline with GitHub Actions.

Step 1: Create workflow file
.github/workflows/ios.yml

Step 2: Define triggers
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

Step 3: Set up build job
- Checkout code
- Select Xcode version
- Install dependencies (SPM)
- Build project
- Run tests
- Upload artifacts

Step 4: Add deployment job
- Build for release
- Sign with certificates (match)
- Upload to TestFlight

Secrets needed:
- MATCH_PASSWORD
- APP_STORE_CONNECT_API_KEY
- CERTIFICATE_P12

Gotchas:
- macOS runner required
- Xcode version selection matters
- Caching SPM for speed""",
        days_ago=22,
        priority=1,
        concept_ids=[CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_LEARNING_ID],
    ),
    create_note(
        title="Podcast Notes: Indie Hackers",
        content="""Episode: Building to $10K MRR

Guest journey:
- Started as side project
- Launched on Product Hunt
- Grew through content marketing
- Hit $10K MRR in 18 months

Key takeaways:

1. Start with a small niche
   - "Riches in niches"
   - Easier to dominate small market

2. Build in public
   - Transparency builds trust
   - Free marketing through content

3. Focus on retention
   - Churn kills SaaS
   - Invest in onboarding

4. Pricing power
   - Don't race to bottom
   - Value-based pricing

Applicable to my projects:
- Share more building progress
- Focus on specific user segment
- Improve onboarding flow""",
        days_ago=30,
        priority=0,
        concept_ids=[CONCEPT_IDS["startup_ideas"]],
        purpose_ids=[PURPOSE_LEARNING_ID],
    ),
    create_note(
        title="Notas del curso: Swift Concurrency",
        content="""Módulo 4: Actores y Aislamiento

Conceptos clave:
- Actor = referencia tipo con aislamiento automático
- @MainActor para código UI
- Task y Task groups
- async let para concurrencia estructurada

Ejemplo de Actor:

actor BankAccount {
    var balance: Decimal

    func deposit(amount: Decimal) {
        balance += amount
    }

    func withdraw(amount: Decimal) throws {
        guard balance >= amount else {
            throw BankError.insufficientFunds
        }
        balance -= amount
    }
}

Importante:
- No usar locks/semaphores en Swift moderno
- Preferir actors sobre clases con locks
- @MainActor en ViewModels para seguridad

Tarea: Refactorizar servicio de red para usar actors.""",
        days_ago=9,
        priority=2,
        language="es",
        concept_ids=[CONCEPT_IDS["software_development"], CONCEPT_IDS["mobile_apps"]],
        purpose_ids=[PURPOSE_LEARNING_ID],
    ),
    create_note(
        title="Research: Vector Databases",
        content="""Comparing vector databases for AI applications.

Options evaluated:

1. Pinecone
   + Fully managed
   + Fast similarity search
   - Expensive at scale
   - Vendor lock-in

2. Weaviate
   + Open source option
   + GraphQL API
   + Multi-modal support
   - Steeper learning curve

3. Qdrant
   + Open source
   + Rust performance
   + Good filtering
   - Smaller ecosystem

4. pgvector (PostgreSQL)
   + Use existing Postgres
   + Simple setup
   - Limited features
   - Performance ceiling

Use case: Semantic search for notes
Recommendation: Start with pgvector for simplicity,
migrate to Qdrant if scaling needed.

Next steps: Prototype with pgvector extension.""",
        days_ago=17,
        priority=2,
        concept_ids=[CONCEPT_IDS["ai_ml"], CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_LEARNING_ID],
        processed_data={
            "summary": "Vector database comparison - pgvector recommended for starting",
            "key_points": ["Pinecone fully managed", "pgvector for simplicity", "Qdrant for scaling"],
            "sentiment": "neutral",
        },
    ),
    create_note(
        title="Workshop Notes: API Design Best Practices",
        content="""Internal workshop on API design.

REST Principles:
- Resources as nouns (not verbs)
- HTTP methods for actions
- Stateless requests
- Consistent naming

Naming conventions:
- Plural nouns: /users, /notes
- Lowercase, hyphenated: /user-settings
- Nested for relationships: /users/{id}/notes

Pagination:
- Offset: simple, jumping pages
- Cursor: scalable, consistent
- Recommendation: cursor for large datasets

Versioning:
- URL prefix: /api/v1/
- Header: X-API-Version
- Recommendation: URL prefix for clarity

Error responses:
- Consistent structure
- Machine-readable codes
- Human-readable messages
- Include correlation IDs

Security:
- Always HTTPS
- JWT for auth
- Rate limiting
- Input validation""",
        days_ago=35,
        priority=1,
        concept_ids=[CONCEPT_IDS["software_development"], CONCEPT_IDS["web_development"]],
        purpose_ids=[PURPOSE_LEARNING_ID],
    ),
    create_note(
        title="Study: SwiftData vs Core Data",
        content="""Comparing SwiftData with Core Data for iOS persistence.

SwiftData advantages:
- @Model macro simplicity
- Swift-native (no Obj-C)
- Seamless SwiftUI integration
- @Query for reactive fetching
- Less boilerplate code

Core Data advantages:
- Mature and battle-tested
- iOS 11+ support
- More migration options
- Larger community resources
- CloudKit integration stable

Migration considerations:
- Not automatic from Core Data
- Need to redefine models
- Data migration manual

Performance:
- Similar for most use cases
- Core Data slightly faster for complex queries
- SwiftData easier to optimize correctly

Recommendation for new projects:
- iOS 17+ only: SwiftData
- Broader support needed: Core Data

For MindDump: SwiftData (iOS 17 min)""",
        days_ago=45,
        priority=1,
        concept_ids=[CONCEPT_IDS["mobile_apps"], CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_LEARNING_ID],
    ),
    create_note(
        title="Video Course: System Design Interview",
        content="""Module 5: Designing a URL Shortener

Requirements:
- Shorten URLs
- Redirect to original
- Custom aliases (optional)
- Analytics (clicks, geography)

Capacity estimation:
- 100M URLs per month
- 10:1 read/write ratio
- 7 characters = 3.5 trillion combinations

Architecture:

1. API Layer
   - POST /shorten
   - GET /{shortCode} -> 301 redirect

2. Application Layer
   - URL validation
   - Short code generation
   - Cache for hot URLs

3. Data Layer
   - SQL for metadata
   - Redis for caching
   - S3 for analytics data

Key decisions:
- Base62 encoding for short codes
- Consistent hashing for partitioning
- Pre-generate IDs to avoid collisions

Trade-offs:
- Short codes vs collision risk
- Consistency vs availability
- Cost vs performance""",
        days_ago=27,
        priority=2,
        concept_ids=[CONCEPT_IDS["software_development"]],
        purpose_ids=[PURPOSE_LEARNING_ID],
    ),
])

# Tasks/Reminders Notes (5+)
notes.extend([
    create_note(
        title="Weekly Tasks - Dec 30",
        content="""Monday:
- [ ] Team standup at 10am
- [ ] Review PRs from weekend
- [ ] Update project board

Tuesday:
- [ ] Finish authentication refactor
- [ ] Write unit tests
- [ ] Code review with Alex

Wednesday:
- [ ] Sprint planning meeting
- [ ] Update documentation
- [ ] Deploy to staging

Thursday:
- [ ] Bug fixing session
- [ ] 1:1 with manager
- [ ] Prepare demo

Friday:
- [ ] Sprint demo
- [ ] Retrospective
- [ ] Clean up tech debt""",
        days_ago=1,
        priority=3,
        concept_ids=[CONCEPT_IDS["productivity"], CONCEPT_IDS["project_management"]],
        purpose_ids=[PURPOSE_TASKS_ID, PURPOSE_WORK_ID],
    ),
    create_note(
        title="Shopping List & Errands",
        content="""Groceries:
- Milk
- Eggs
- Bread
- Vegetables (broccoli, carrots)
- Chicken
- Rice
- Coffee beans

Errands:
- [ ] Dry cleaning pickup
- [ ] Return Amazon package
- [ ] Book dentist appointment
- [ ] Pay utility bills
- [ ] Renew gym membership

Hardware store:
- Light bulbs
- Batteries
- Picture hooks""",
        days_ago=2,
        priority=1,
        concept_ids=[],
        purpose_ids=[PURPOSE_TASKS_ID],
    ),
    create_note(
        title="Home Office Setup Tasks",
        content="""Equipment to buy:
- [ ] Standing desk converter ($200-300)
- [ ] Monitor arm ($50)
- [ ] Keyboard wrist rest
- [ ] Better desk lamp

Organization:
- [ ] Cable management system
- [ ] Shelf for books
- [ ] Plant for desk
- [ ] Whiteboard for brainstorming

Setup tasks:
- [ ] Clean and organize desk
- [ ] Mount new monitor
- [ ] Set up proper lighting
- [ ] Configure ergonomic position

Budget: $500 total
Target completion: End of January""",
        days_ago=10,
        priority=2,
        concept_ids=[CONCEPT_IDS["productivity"]],
        purpose_ids=[PURPOSE_TASKS_ID, PURPOSE_PERSONAL_ID],
    ),
    create_note(
        title="App Release Checklist",
        content="""Pre-release:
- [x] All features implemented
- [x] QA testing complete
- [x] Performance benchmarks pass
- [ ] Update App Store description
- [ ] Create new screenshots
- [ ] Prepare release notes

Submission:
- [ ] Archive build
- [ ] Upload to App Store Connect
- [ ] Fill out app information
- [ ] Submit for review

Post-release:
- [ ] Monitor crash reports
- [ ] Respond to reviews
- [ ] Announce on social media
- [ ] Update documentation
- [ ] Celebrate! 🎉""",
        days_ago=1,
        priority=4,
        concept_ids=[CONCEPT_IDS["mobile_apps"], CONCEPT_IDS["project_management"]],
        purpose_ids=[PURPOSE_TASKS_ID, PURPOSE_WORK_ID],
    ),
    create_note(
        title="Reading List 2025",
        content="""Technical:
- [ ] "Clean Architecture" by Robert Martin
- [ ] "Designing Data-Intensive Applications" by Martin Kleppmann
- [ ] "Staff Engineer" by Will Larson
- [x] "iOS Programming" by Big Nerd Ranch

Non-fiction:
- [ ] "Thinking, Fast and Slow" by Daniel Kahneman
- [ ] "The Mom Test" by Rob Fitzpatrick
- [ ] "Zero to One" by Peter Thiel
- [x] "Atomic Habits" by James Clear

Fiction:
- [ ] "Project Hail Mary" by Andy Weir
- [ ] "The Three-Body Problem" by Liu Cixin

Goal: 24 books (2 per month)
Progress: 2/24 complete""",
        days_ago=5,
        priority=0,
        concept_ids=[CONCEPT_IDS["personal_growth"]],
        purpose_ids=[PURPOSE_TASKS_ID, PURPOSE_LEARNING_ID],
    ),
    create_note(
        title="Recordatorios importantes",
        content="""Esta semana:
- [ ] Llamar a mamá (cumpleaños viernes)
- [ ] Renovar pasaporte
- [ ] Cita con doctor - jueves 3pm
- [ ] Pagar seguro del auto

Este mes:
- [ ] Impuestos trimestrales
- [ ] Revisión anual del trabajo
- [ ] Planear vacaciones de verano

Próximo mes:
- [ ] Conferencia de desarrolladores
- [ ] Renovar suscripciones
- [ ] Limpieza dental""",
        days_ago=0,
        priority=2,
        language="es",
        concept_ids=[],
        purpose_ids=[PURPOSE_TASKS_ID],
    ),
])

# Add a few more archived notes
notes.extend([
    create_note(
        title="Old Project: Weather App",
        content="""Archived project from earlier this year.

Features built:
- Current weather display
- 7-day forecast
- Location-based updates
- Favorite locations

Lessons learned:
- Weather APIs can be unreliable
- Caching is essential
- Users love widgets

Why archived: Decided to focus on MindDump instead.
Code available at: github.com/user/weather-app""",
        days_ago=90,
        priority=0,
        status_id=STATUS_ARCHIVED_ID,
        concept_ids=[CONCEPT_IDS["mobile_apps"]],
        purpose_ids=[PURPOSE_WORK_ID],
    ),
    create_note(
        title="Meeting Notes - Q3 Review (Archived)",
        content="""Q3 performance review meeting.

Achievements:
- App downloads exceeded target by 25%
- User retention improved to 45%
- Bug count reduced by 60%

Areas discussed for improvement:
- Onboarding flow needs work
- Analytics implementation incomplete
- Documentation lagging

Action items from Q3 (now complete):
- Hired new developer
- Implemented new analytics
- Updated onboarding

Archiving as Q4 is now complete.""",
        days_ago=95,
        priority=0,
        status_id=STATUS_ARCHIVED_ID,
        concept_ids=[CONCEPT_IDS["project_management"]],
        purpose_ids=[PURPOSE_WORK_ID],
    ),
])

# ============================================================================
# User Settings
# ============================================================================

user_settings = {
    "id": generate_uuid(),
    "user_id": USER_ID,
    "language": "en",
    "auto_structure_note": True,
    "creation_date": iso_date(180),
    "last_update": iso_date(30),
}

# ============================================================================
# Helper Functions for Data Access
# ============================================================================

def get_note_by_id(note_id: str) -> dict | None:
    """Find a note by ID."""
    return next((n for n in notes if n["id"] == note_id), None)

def get_folder_by_id(folder_id: str) -> dict | None:
    """Find a folder by ID."""
    return next((f for f in folders if f["id"] == folder_id), None)

def get_concept_by_id(concept_id: str) -> dict | None:
    """Find a concept by ID."""
    return next((c for c in concepts if c["id"] == concept_id), None)

def get_status_by_id(status_id: str) -> dict | None:
    """Find a status by ID."""
    return next((s for s in statuses if s["id"] == status_id), None)

def get_purpose_by_id(purpose_id: str) -> dict | None:
    """Find a purpose by ID."""
    return next((p for p in purposes if p["id"] == purpose_id), None)
