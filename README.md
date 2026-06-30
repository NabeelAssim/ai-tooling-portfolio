\# AI Tooling Portfolio Setup



This repository documents my process setting up an AI-assisted development environment as a non-technical candidate, completed as part of a portfolio task.



\## Tools Installed



\- \*\*Cursor IDE\*\* — downloaded and installed from cursor.com

\- \*\*Node.js (v24.18.0)\*\* — required for npm, which wasn't initially installed on my system

\- \*\*Claude Code\*\* — installed via npm (`npm install -g @anthropic-ai/claude-code`)

\- \*\*Codex\*\* — installed via npm (`npm install -g @openai/codex`), signed in successfully, sandbox configured in non-admin mode

\- \*\*Git (v2.54.0)\*\* — installed to enable cloning and pushing to GitHub



\## Steps Completed



1\. Installed Cursor IDE

2\. Attempted to install Claude Code as a Cursor extension/plugin — discovered it is not available through Cursor's Plugins or Extensions marketplace, and is instead a standalone tool

3\. Installed Node.js after discovering npm was not available on my system

4\. Installed Claude Code via npm in Cursor's integrated terminal

5\. Installed Codex via npm and successfully signed in

6\. Created a public GitHub repository

7\. Installed Git after discovering it wasn't available on my system

8\. Cloned the repository into Cursor



\## Issues Encountered and Resolutions



\- \*\*npm not recognized\*\*: Node.js was not installed on my system. Installed Node.js, restarted Cursor, and confirmed via `node -v`.

\- \*\*PowerShell script execution blocked\*\*: Running npm install triggered a security policy error. Resolved by running `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`.

\- \*\*Claude Code login required a paid subscription\*\*: Installation succeeded, but full authentication required a Claude Pro/Max/Team subscription or API billing. I completed the installation but did not proceed with payment, as it was outside the scope of this task.

\- \*\*Git not recognized\*\*: Git was not installed on my system. Installed Git, restarted Cursor, and confirmed via `git --version`.

\- \*\*Claude Code not found in Cursor's Plugins/Extensions marketplace\*\*: Discovered that Claude Code is a separate CLI tool, not a Cursor extension, and installed it accordingly via the integrated terminal.



\## Reflection



Going into this, I wasn't sure what to expect since I don't have a coding background. The instructions assumed a level of familiarity I didn't have, which meant almost every step surfaced something unexpected.



I used Claude to help me work through each error as it came up — interpreting what the error messages actually meant, figuring out why npm and Git weren't recognized, and understanding why Claude Code wasn't showing up where I expected it to in Cursor. What stood out to me was that the errors weren't really about the tools themselves being broken — they were missing dependencies or terminology that had changed between versions, and each one needed to be diagnosed before it could be fixed.



I think that's closer to what this task was actually testing. I didn't know how to do this going in, but I knew how to ask the right questions, read an error message instead of panicking at it, and keep working through the problem until it resolved. That's the same approach I'd take with any unfamiliar tool on the job — figure out what's actually broken, find the right resource to help, and stay with it until it works.

