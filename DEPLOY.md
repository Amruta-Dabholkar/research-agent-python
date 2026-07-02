# Deploying the UI

## 1. Run it locally first

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# edit .env: add ANTHROPIC_API_KEY (or OPENAI_API_KEY) and SERPAPI_API_KEY

streamlit run streamlit_app.py
```

This opens the app at `http://localhost:8501`.

## 2. Push to GitHub

```bash
git init
git add .
git commit -m "Add Streamlit UI"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

`.gitignore` already excludes `.env` and `.streamlit/secrets.toml`, so your keys won't be committed.

## 3. Deploy on Streamlit Community Cloud (free)

1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **New app**, pick your repo/branch, and set the main file path to `streamlit_app.py`.
3. Before (or after) deploying, open **Settings -> Secrets** and paste in the contents of `.streamlit/secrets.toml.example` with real values filled in, e.g.:

   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   SERPAPI_API_KEY = "..."
   ```

4. Deploy. You'll get a shareable `https://<your-app>.streamlit.app` URL.

## Notes

- Each visitor's runs share the app's API keys (yours) and billing — there's no per-user auth here. For a public link, keep `max_iterations` capped in the sidebar and watch your SerpAPI/LLM usage.
- If you want to swap providers, `LLM_PROVIDER` can be `anthropic` or `openai` — set it in secrets or pick it in the sidebar at runtime.
- `scrape_page` will occasionally fail or get blocked on sites with bot protection — this is expected per the README's "Known Limitations"; the agent is prompted to move on rather than retry.
