# What is this?
It's a way to simulate migration flag data, so you have visualizations in your LaunchDarkly account. It will:
- Simulate reads from both an old and new source
- Simulate writes to both an old and new source
- Check for consistency on the reads when both are successful

This was created to be used with 6-stage migration flags

# How can I use it?
1. `pip install requirements.txt`
2. Rename `.env.example` to `.env`
3. Replace the environment variables in `.env` with your values. Point it to a LaunchDarkly migration flag.
4. `python main.py`