# Lesson 2: Saving your work with Git

## Why this matters
Right now, if you break `exercise_01.py`, the working version is gone.
Git fixes that. It takes **snapshots** of your project, called **commits**, and you can go back to any of them.

- **Git** runs on your laptop. Nothing leaves your computer.
- **GitHub** is a website that stores a copy of your Git project online. That's your portfolio. We do GitHub in Part B.

At work, every quant team uses Git. Code that isn't in Git doesn't really exist.

## The idea: three places
| Place | What it is | Command that moves it on |
|---|---|---|
| Working folder | Your files as you edit them | `git add` |
| Staging area | Changes you've picked for the next snapshot | `git commit` |
| History | Saved snapshots | |

Think of staging as packing a box before you seal it. You choose what goes in, then `commit` seals it with a label.

---

## Part A: Your first commit (today)

Do every step in the VS Code terminal, inside `quant_dev`. Run `Get-Location` first to check.

### Step 1: Check who Git thinks you are
```
git config --global user.name
git config --global user.email
```
Every commit records this name and email **permanently**. If you put the project on a public GitHub page, anyone can see that email.

**Stop here** if the email is a personal one you don't want public. Tell Claude, and we'll set up GitHub's private "noreply" email first.

### Step 2: Use `main` as the branch name
Do this **before** `git init`:
```
git config --global init.defaultBranch main
```
Without this, Git names your first branch `master`. GitHub and most teams now use `main`. You only do this once on this laptop.

If you already ran `git init` and have no commits yet, rename the branch instead:
```
git branch -m main
```

### Step 3: Turn the folder into a Git project
```
git init
```
This creates a hidden `.git` folder, where Git keeps your history. Don't edit or delete it.

### Step 3b: Use your GitHub noreply email for this project
Run this inside the project, **without** `--global`, so your other Git projects keep their own email:
```
git config user.email "ID+USERNAME@users.noreply.github.com"
git config user.email
```
The second command should print the noreply address. Do this **before your first commit**, because commits keep the email they were made with.

### Step 4: Look before you act
```
git status
```
Your files show as **untracked**: Git sees them but isn't saving them yet.
Run `git status` constantly. It's the Git version of checking your folder before running code.

### Step 5: Tell Git what to ignore
Create a file named exactly `.gitignore` (starting with a dot) and type in:
```
__pycache__/
.venv/
```
These are files Python and tools create automatically. They don't belong in your history.
A `.gitignore` is also how you keep things out of a public project, such as files with passwords or private notes.

### Step 6: Stage your files
Stage one file, then check:
```
git add lesson_01.py
git status
```
Now stage the rest, naming each one:
```
git add .gitignore exercise_01.py lesson_02_git.md ROADMAP.md
git status
```
Leave `memory.md` and `JOURNAL.md` unstaged for now. Decide later whether they should be public.

Naming files is slower than `git add .` (which adds everything), but you always know what you're saving.

### Step 7: Commit
```
git commit -m "Add Lesson 1 and Exercise 1"
```
The text after `-m` is the commit message. A good message says **what changed**, in a few words, starting with a verb:
- Good: `Fix average return calculation`
- Bad: `stuff`, `update`, `asdf`

### Step 8: See your history
```
git log --oneline
```
You'll see one line: a short ID and your message. That's your first snapshot.

---

## Practice: undo a mistake
1. Open `exercise_01.py` and break it on purpose. For example, delete the `print` for the average.
2. Run `git status`. Git shows the file as **modified**.
3. Run `git diff`. Lines starting with `-` were removed, `+` were added.
4. Undo it:
   ```
   git restore exercise_01.py
   ```
5. Run the file. It's back to your last commit.

**Warning:** `git restore` throws away changes you haven't committed. Use it only when you're sure you don't want them. Commit often, so you always have a recent snapshot.

## Practice: a second commit
1. Add a comment at the top of `exercise_01.py`, for example: `# Exercise 1: daily, average and highest returns`
2. `git status`, then `git diff`
3. `git add exercise_01.py`
4. `git commit -m "Add description to Exercise 1"`
5. `git log --oneline`. You should see two commits.

## Your daily routine from now on
1. `git status`
2. Edit and test your code
3. `git diff` to read what changed
4. `git add <file>`
5. `git commit -m "Verb what changed"`

## Cheat sheet
| Command | What it does |
|---|---|
| `git status` | Shows what's changed, staged or untracked |
| `git add <file>` | Stages a file for the next commit |
| `git commit -m "..."` | Saves a snapshot of staged changes |
| `git log --oneline` | Lists your commits |
| `git diff` | Shows unstaged changes line by line |
| `git restore <file>` | Discards uncommitted changes to a file |

---

## Part B: Putting your project on GitHub

So far your history lives only on your laptop. A **remote** is a copy of your project stored somewhere else.
**Pushing** sends your commits to it. This gives you a backup, and a public page people can look at.

| Word | Meaning |
|---|---|
| Repository (repo) | A project tracked by Git, including its history |
| Remote | A copy of the repo somewhere else. `origin` is the usual name for the main one. |
| Push | Send your commits to the remote |
| README | The file GitHub shows on your project's front page |

**Pushing to a public repo publishes your work.** Treat every push as permanent: people and tools can copy it the moment it's up, even if you delete it later.

### Step 1: Commit your `.gitignore` change
Run `git status`, then:
```
git add .gitignore
git commit -m "Ignore private notes and journal"
```

### Step 2: Write your README
Create `README.md` in `quant_dev`. Write it in your own words. It should answer:
- Who are you, and what are you working towards?
- What's in this project?
- **Who wrote what?** Say that the lessons were written by Claude, an AI tutor, and that the exercises are your own.
- Make clear that the prices are made up and that nothing here is investment advice.

Don't include your phone number, personal email, grades or scholarship plans.

### Step 3: Commit the README and your other files
```
git add README.md ROADMAP.md lesson_02_git.md
git status
git commit -m "Add README, roadmap and Git lesson"
```

### Step 4: Check what will go public
```
git ls-files
git log --format="%h %ae %s"
```
- `git ls-files` lists every file that will be published. Read it. `memory.md`, `JOURNAL.md`, `goals/` and `posts/` should **not** be there.
- The second command shows the email on each commit. Every line should show your noreply address.

### Step 5: Create the empty repo on GitHub
1. On github.com, click **+** in the upper-right corner, then **New repository**.
2. Name it, for example `quant-dev-journey`. Add a one-line description.
3. Choose **Public** or **Private**. Public is what makes it a portfolio. Private lets you practise first.
4. **Don't add a README, .gitignore or license.** Your project already has its own history, and GitHub warns these can cause a merge conflict.
5. Click **Create repository**, then copy the HTTPS URL. It ends in `.git`.

### Step 6: Connect your project to GitHub
```
git remote add origin PASTE-YOUR-URL-HERE
git remote -v
```
`git remote -v` should show your URL twice: once for fetch, once for push.

### Step 7: Push
```
git push -u origin main
```
- Your browser may open and ask you to sign in to GitHub and authorise Git. That comes from Git Credential Manager, which is installed with Git for Windows. Sign in on github.com itself, and only you should type your password.
- `-u` links your `main` to GitHub's `main`, so next time you can just type `git push`.

### Step 8: Look at your page
Open your repo on GitHub. Check that your README shows, click a commit, and confirm the files match what you expected.

## Your routine now
1. `git status`
2. Edit and test your code
3. `git diff`
4. `git add <file>`
5. `git commit -m "Verb what changed"`
6. `git push`

## Sources
- First-time setup: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
- `git init` and default branch: https://git-scm.com/docs/git-init
- Commit email privacy: https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address
- Pushing existing code to GitHub: https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
- Creating a repository: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- Signing in with Git Credential Manager: https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git
- READMEs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
