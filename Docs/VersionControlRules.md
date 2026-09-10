# Florgropuli Version Control Standards

## 1. Never Commit Directly to `main`
- All changes must go through a branch and pull request (PR).
- `main` should always be in a reasonalbly "working" state.
- **NO DIRECT PUSHES TO `main` EVER**

```bash
# Get up to date with `main`
git checkout main
git pull origin main

# Make your branch
git checkout -b new-branch-name

# Do your thing... ... ...

# Check your status create your commit
git status .
git add .
git commit -m"commit-name"

# Create a PR
git push -u origin HEAD && gh pr create --base main --title "Your PR Title" --body "Your PR Description"
```

## 2. Use Feature Branches
ex:
```
feature/login-page
feature/database-api
feature/webpage-bug
feature/setup-guide
...
etc
```
A branch should represent **one logical task**.

## 3. Pull / Rebase before opening or merging a PR
In order to reduce merge confilicts and keep our history clean:
```bash
git fetch origin
git rebase origin/main
```
before every PR.

## 4. CI must pass before merging
At minimum:
- Build must succeed
- Tests must pass
- Linter/formatter must pass
- No obvious security checks fail

## 5. Don't merge your own PR
Have a peer check your work and merge to `main` for you.

## 6. Keep commit messages clear

Good:
```
Add user authentication
Fix password validation
Add authentication tests
```

Bad:
```
fixed stuff
updates
final final FINAL. ACUALLY FINAL
```

## 7. Use `.gitignore`

Do not commit your secrets / machine code. I.e:
```
#/.gitignore
.env
[API Keys]
[Passwords]
.venv/
*.log
build/
dist/ 
etc...
```

## 8. Don't rewrite shared history

Avoid:
```bash
git push --force
```
on shared branches if at all possible.
