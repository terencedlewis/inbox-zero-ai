# Inbox Zero AI

Inbox Zero AI is a Streamlit app that helps users process inbound messages faster by turning raw text into clear summaries, action items, deadlines, and a priority rating.

## Product Description

Inbox Zero AI is designed as a lightweight productivity assistant for people who handle high volumes of email or chat messages. The app accepts pasted message content, sends it to an OpenAI model, and returns structured output that supports quick triage and follow-up.

Primary goals:

- Reduce time spent reading long messages
- Improve consistency in identifying next steps
- Surface deadlines and urgency early
- Provide a simple UI for demos and rapid iteration

## Epic

Build a lightweight AI assistant that helps users reach inbox zero faster by converting unstructured inbound messages into structured, actionable outputs in one step.

## Features

- Summarizes emails into bullet points
- Extracts action items
- Detects deadlines
- Assigns priority

## User Stories

- As a busy professional, I want to paste a long email and get a concise summary so I can understand it quickly.
- As a team lead, I want action items extracted clearly so I can delegate follow-ups without missing tasks.
- As a project manager, I want deadlines highlighted so I can track time-sensitive work.
- As an operations user, I want a simple priority signal so I can triage what to handle first.

## Demo

UI screen capture path:

## UI Demo Screenshot
<img width="598" height="453" alt="Screenshot 2026-04-06 at 9 59 03 PM" src="https://github.com/user-attachments/assets/f983582a-5164-4db6-a841-bc996463e871" />

- [docs/assets/ui-demo.png](docs/assets/ui-demo.png)

Additional demo notes:

- [docs/assets/README.md](docs/assets/README.md)

## Product Documentation

- PRD: [docs/PRD.md](docs/PRD.md)

## Repository Layout

This repository currently contains two separate Streamlit apps in separate folders:

- inbox_zero_ai/: Inbox Zero AI
- ai_workout_generator/: AI Workout Generator

Each folder has its own app entrypoint and requirements file.

## Run Apps

- Inbox Zero AI: run from inbox_zero_ai/
- AI Workout Generator: run from ai_workout_generator/
