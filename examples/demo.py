"""
Vektori demo — run this while recording.

Shows the episode layer inferring a behavioral pattern
from two separate sessions that neither session alone contained.

Setup:
    export OPENAI_API_KEY=sk-...
    python examples/demo.py
"""

import asyncio
from vektori import Vektori

USER = "demo-user"


async def main():
    v = Vektori(
        embedding_model="openai:text-embedding-3-small",
        extraction_model="openai:gpt-4o-mini",
    )

    print("── adding session 1 (two weeks ago) ──────────────────")
    await v.add(
        messages=[
            {"role": "user",      "content": "I'm trying to cut back on caffeine, switching to green tea."},
            {"role": "assistant", "content": "Good call — green tea still has some caffeine but way less."},
        ],
        session_id="session-001",
        user_id=USER,
    )
    print("stored.")

    print("\n── adding session 2 (yesterday) ──────────────────────")
    await v.add(
        messages=[
            {"role": "user",      "content": "Rough week. I've been living on coffee again, can't help it."},
            {"role": "assistant", "content": "Stress does that. Want help building a wind-down routine?"},
        ],
        session_id="session-002",
        user_id=USER,
    )
    print("stored.")

    await asyncio.sleep(4)  # let extraction finish

    print("\n── search: 'caffeine habits' ─────────────────────────")
    results = await v.search(
        query="what's this user's relationship with caffeine?",
        user_id=USER,
        depth="l1",
    )

    print("\nfacts:")
    for f in results.get("facts", []):
        print(f"  [{f['score']:.2f}] {f['text']}")

    print("\nepisodes:")
    for e in results.get("insights", []):
        print(f"  {e['text']}")

    await v.close()


asyncio.run(main())
