# Product Requirements Document (PRD)

## Product

Inbox Zero AI

## Problem Statement

Users spend too much time reading long inbound messages and manually identifying what matters. Important actions and deadlines are often missed or delayed.

## Goal

Provide a simple AI-powered interface that converts unstructured messages into concise, actionable outputs:

- Summary
- Action items
- Deadlines
- Priority level

## Success Metrics

- Time-to-triage reduction compared to manual review
- Percentage of messages with correctly identified action items
- Percentage of messages with correctly identified deadlines
- User-rated usefulness of priority assignment

## Target Users

- Founders and operators
- Customer support and success teams
- Project managers
- Individual contributors managing high message volume

## Scope

### In Scope (Current)

- Streamlit text input UI
- OpenAI-powered analysis
- Structured markdown output with sections
- Environment-based API key management

### Out of Scope (Current)

- Native Gmail inbox sync
- Slack event ingestion
- Auto-send email replies
- Persistent user accounts and history

## Epics

## Epic 1: Core Message Analysis

Deliver reliable extraction of summary, action items, deadlines, and priority from pasted message text.

## Epic 2: User Experience and Demo Readiness

Provide a clean, fast Streamlit interface suitable for internal demos and early user testing.

## Epic 3: Integrations and Workflow Automation

Expand from manual paste-based workflow to connected inbox/chat sources and downstream task systems.

## Features

### Feature 1: Message Input and Analyze Action

Users can paste message text and trigger analysis via one button.

### Feature 2: Structured AI Response

System returns output with clear headings for Summary, Action Items, Deadlines, and Priority.

### Feature 3: Priority Classification

System assigns Low, Medium, or High priority based on urgency and required action.

### Feature 4: API Key Configuration

System reads OPENAI_API_KEY from environment variables using python-dotenv.

### Feature 5: Demo Screenshot Section

Documentation includes a dedicated location for a UI screenshot used in presentations and demos.

## User Stories

### Story 1: Fast Inbox Triage

As a busy user, I want to paste an email and get a concise summary so I can decide quickly what to do next.

Acceptance Criteria:

- User can paste text in the app input area
- Clicking Analyze returns a Summary section
- Summary content is in readable bullet format

### Story 2: Action Extraction

As a user, I want action items extracted so I can execute tasks without rereading the full message.

Acceptance Criteria:

- Output includes an Action Items section
- Action steps are explicit and actionable

### Story 3: Deadline Visibility

As a user, I want deadlines called out so I do not miss time-sensitive commitments.

Acceptance Criteria:

- Output includes a Deadlines section
- If no deadline exists, output states none found

### Story 4: Priority Signal

As a user, I want a priority label so I know whether to act now or later.

Acceptance Criteria:

- Output includes a Priority section
- Priority value is one of: Low, Medium, High

### Story 5: Demo Artifacts

As a presenter, I want a dedicated screenshot section so I can quickly include product visuals in demos.

Acceptance Criteria:

- Repo contains a defined screenshot path in documentation
- README links to screenshot instructions

## UI Screenshot Section (For Demo)

Place demo screenshot file at:

- docs/assets/ui-demo.png

Reference guidance:

- Screenshot instructions: [docs/assets/README.md](docs/assets/README.md)
