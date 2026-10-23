# Security Policy

## Scope

This repository is a **portfolio and learning project**: a Selenium + Pytest UI automation framework that runs against the public Sauce Labs demo store ([saucedemo.com](https://www.saucedemo.com)).

This policy covers the code in this repository, such as the framework, its configuration, and its dependencies. It does **not** cover saucedemo.com or any Sauce Labs product. To report an issue with those, contact Sauce Labs through their official channels.

## Supported versions

Only the latest version on the `main` branch is maintained.

| Version | Supported |
|---|---|
| `main` (latest) | Yes |
| Older commits | No |

## Reporting a vulnerability

If you find a security issue in this repository (for example an unsafe dependency, a leaked credential, or insecure CI configuration), please report it **privately** and not in a public issue.

1. Use GitHub's **Report a vulnerability** option under the repo's **Security** tab (private vulnerability reporting), or
2. Email **ajitavhad333@gmail.com** with the subject line `Security: web-ui-selenium-framework`.

Please include:
- A description of the issue and where it is (file, line, or workflow)
- Steps to reproduce, if applicable
- The possible impact

I aim to acknowledge reports within 7 days and to fix valid issues as soon as I reasonably can. This is a personal project, so response times may vary.

## What this repository does not contain

- No real user data, company data, or client data
- No private API keys, tokens, or passwords
- The only credentials in the code (`standard_user` / `secret_sauce`, etc.) are the **publicly documented demo logins** for saucedemo.com

If you find anything in the repository that looks like a real secret, please report it using the steps above.

## Responsible use

- The tests in this repository are intended **only** for the public demo site listed above, which exists for test automation practice.
- Do not point these scripts at websites or systems you do not own or do not have written permission to test.
- Do not use this project for load testing, scraping, or attacking any service.

## Security practices used in this project

- Secrets are never committed. If a future version needs credentials, they will be stored in GitHub Actions **Secrets** or environment variables.
- Dependencies are listed in `requirements.txt` and can be monitored with GitHub Dependabot.
- CI runs in GitHub-hosted runners with no access to personal systems.
- Sensitive local files and folders (`venv/`, reports, screenshots) are excluded through `.gitignore`.

## Disclosure

Once an issue is fixed, I'm happy to credit the reporter in the commit or release notes if they wish.
