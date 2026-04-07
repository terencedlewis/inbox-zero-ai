# Inbox Zero AI

This folder is a standalone Streamlit app for message triage.

## Run Locally

1. Create and activate a virtual environment in this folder.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:

   ```bash
   streamlit run app.py
   ```

## Notes

- The app reads OPENAI_API_KEY from `.env` in this folder or the repository root.
- Keep dependencies for this app in `inbox_zero_ai/requirements.txt`.
