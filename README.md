🧠 Personal Notes (Dev Log)

Day 1:
- Project structure created and pushed to GitHub
- Git remote connection error fixed with --allow-unrelated-histories
- NASA APOD and Launch Library 2 APIs explored
  - APOD response is flat — simple key/value pairs at top level
  - Launch Library is nested — sub-objects like rocket, mission, pad, agency
  - Nested data will need to be unpacked before PostgreSQL storage
- Accidentally exposed API key in chat — regenerated immediately (good lesson)
- Virtual environment issue fixed by creating venv locally
- 403 error on new API key — resolved with DEMO_KEY while real key activates
- First successful API call — Status 200 ✅

Mistakes & Corrections:
- Exposed real API key publicly — regenerated immediately. Never hardcode or paste API keys anywhere public
- VS Code was using a different Python than where requests was installed — fixed by creating a virtual environment with python -m venv venv and reinstalling dependencies inside it
- New NASA API key returned 403 — keys take up to 1 hour to activate after generation, used DEMO_KEY as temporary fix