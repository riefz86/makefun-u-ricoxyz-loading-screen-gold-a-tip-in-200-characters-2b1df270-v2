# Loading Screen Gold v2 — design notes

## The entry

One loading-screen tip, 161 characters, one line, written by `main.py`
to `/output/entry.txt`:

> Tip: if your agent says 'almost done' for the third time, it has
> quietly started a second project inside the first one. Neither of
> them is the one you asked for.

## Why this tip, and why it is not v1

The v1 entry scored 47.09% (round 2 rank 714 of 2,908). Its premise —
an agent refactoring code while fetching a drink — leaned on a
familiar image (the agent wandering off for refreshment) and its
punchline landed softly: the joke was mostly "the agent is
distracted", which is the first idea anyone has about agents.

This v2 starts from a different, more specific observation. Anyone
who has driven an AI coding agent has lived this exact moment: the
agent reports "almost done", then "almost done" again, and the
suspicion grows that the work has quietly multiplied. The tip names
that suspicion out loud — the agent has started a second project
inside the first one — and then turns it once more: neither project
is the one you asked for. That second turn is the punchline; the
first sentence sets a trap the second sentence springs.

## How it maps to the judge's brief

The brief weighs five things, most important first:

1. **A tip for stressed developers and AI coding agents.** The line
   opens with "Tip:" and is addressed to the person watching the
   loading screen while their agent works. It is not a slogan, a
   status message, or a joke about something else.
2. **A real laugh through a turn, not a groan pun.** There is no pun
   at all. The laugh comes from recognition ("almost done" for the
   third time) followed by escalation (a project inside a project)
   followed by the rug-pull (neither is yours).
3. **Lands in a glance, every word working.** 161 characters, one
   sentence of setup and one short sentence of payoff. "Quietly"
   does work: it is the word that makes the second project feel
   sneaky rather than merely large. "Third time" does work: it is
   the count at which patience turns into suspicion.
4. **Speaks to the developer and the agent at once.** The developer
   hears their own frustration with runaway agents; the agent, if
   it could read, would recognise its own habit of scope creep.
   The joke is about both of them, from either side of the screen.
5. **Fresh, not a rerun.** No coffee, no deadline, no compile
   joke. The subject is the agent's own project management — the
   way an agent invents work for itself — which is a newer, more
   specific vein than the usual loading-screen gags.

## Candidates considered and rejected

- "Your agent isn't stuck — it's reading the same error for the
  fourth time, hoping the error changed its mind." Funny, but the
  second half ("It hasn't. Ship it anyway.") drifts toward advice
  rather than a punchline, and "stuck on an error" is closer to the
  usual compile-error territory the brief warns against.
- "Your agent just rewrote your function, then rewrote the
  rewrite." A good image, but the payoff ("still reading the first
  error message") is a single beat, and again it leans on errors
  rather than on the agent's behaviour as a worker.
- The chosen tip won because its premise (nested projects) is the
  most specific, its turn is the sharpest, and it needs no
  knowledge of any particular error or tool to land.

## The program

`main.py` holds the tip as one fixed string and validates it before
writing: non-empty, at most 200 characters, a single line. It writes
`/output/entry.txt` with no trailing newline, so the file holds
exactly the 161 characters of the tip, then chmods it 0644 so the
grader can collect it as another user. A run with an output
directory argument is supported for local testing; with no argument
it writes `/output`, as the grader expects. After writing, it reads
the file back and checks the bytes match the tip, so a silent
partial write cannot pass unnoticed. The program is deterministic:
the same fixed string goes out on every run.
