# Web Scraping using Python, Airflow, Docker and Selenium

## Context
Sometimes when creating web bot applications, we face issues related to the environment machine configuration or even the browser itself - Firefox, Chrome, etc. So having a solution that is resilient is fairly important nowadays. Additionally, depending on the situation, it might be necessary, for any reason, to run these bots inside a Linux machine, and it is known that accessing the browser through them might not seem as simple as it could.

The current project will aim to address this issue.

## Solution's Core
I am aware that for a robust solution it would be very useful to create the Grid from the Hub and Nodes Docker images. However, I will be using a standalone Firefox image for this project.
That said, The idea of the project is to have a preconfigured container that includes Selenium WebDriver and a standalone Firefox browser, allowing run automated browser tests using Selenium. Simultaneously, It will be running the Airflow application in another container, which will make it possible to execute web scraping Python scripts on the standalone Firefox browser. The scripts will be scheduled and orchestrated to run according to the requirements.

## Deploy

## Architecture

## Some useful commands

## Observations

## Next steps

## Technologies

<a href="https://www.selenium.dev/" title="Selenium">
    <img align="middle" src="https://github.com/devicons/devicon/blob/master/icons/selenium/selenium-original.svg" alt="selenium" height="30" width="40" style="max-width: 100%;">
</a>

<a href="https://airflow.apache.org/" title="Airflow">
    <img align="middle" src="https://github.com/devicons/devicon/blob/master/icons/apacheairflow/apacheairflow-original.svg" alt="airflow" height="30" width="40" style="max-width: 100%;">
</a>

<a href="https://www.python.org/" title="Python">
    <img align="middle" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" height="30" width="40" style="max-width: 100%;">
</a>

<a href="https://git-scm.com/" title="Git">
    <img align="middle" src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" height="30" width="40" style="max-width: 100%;">
</a>

<a href="https://www.docker.com/" title="Docker">
    <img align="middle" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" height="30" width="40" style="max-width: 100%;">
</a>

<a href="https://www.linux.org/" title="Linux">
    <img align="middle" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" height="30" width="40" style="max-width: 100%;">
</a>

<a href="https://github.com/" title="GitHub">
    <img align="middle" src="https://github.com/devicons/devicon/blob/master/icons/github/github-original.svg" alt="github" height="30" width="40" style="max-width: 100%;">
</a>

## Release history

1.0.0 - May 07, 2024
- First Version - josue.lui - May 07, 2024