<a href="https://lovedbymen.com">
  <img alt="Refinaid Source Code" src="./.github/banner-thin.png">
</a>

<br />
<br />

<p align="center">
  <img alt="" src="https://img.shields.io/pypi/pyversions/gradio.svg?style=for-the-badge&labelColor=000" />
  <img alt="" src="https://img.shields.io/github/license/PetaTech/refinaid?style=for-the-badge&labelColor=000" />
  <img src="https://img.shields.io/github/stars/PetaTech/refinaid?style=for-the-badge&labelColor=000" alt="Novel.sh's GitHub repo" />
</p>

<p align="center">
  <strong>
    <a href="#-abstract">📍 Abstract</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;<a href="#-contributing">🌏 Contributing</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;<a href="#-contact">📲 Contact</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;<a href="#-license">🪪 License</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;<a href="https://refinaid.vercel.app/">🐻 Web</a>&nbsp;&nbsp;&bull;&nbsp;&nbsp;<a href="https://refinaid-docs.vercel.app/"> 📚 Docs</a>
  </strong>
</p>


# Refinaid: Bridging the Gap with AI For Everyone

## 📍 Abstract

Hi there 👋🏻 This is **Refinaid**. **Refinaid** is an open-source learning platform enabling everyone unfamiliar with programming languages to easily engage with AI and open the doors to the world of the future.

## 🌏 Contributing

### Forking this Repository:

Fork the `refinaid` repository into your own workspace.

### Cloning the Repository to Your Workspace:

```shell
$ git clone git@github.com:<your_workspace_name>/refinaid.git
```

### Setting Upstream Remote:

```shell
$ git remote add upstream git@github.com:PetaTech/refinaid.git

$ git remote -v
origin  git@github.com:<your_user_name>/refinaid.git (fetch)
origin  git@github.com:<your_user_name>/refinaid.git (push)
upstream        git@github.com:PetaTech/refinaid.git (fetch)
upstream        git@github.com:PetaTech/refinaid.git (push)
```
### Pull Requests:

If you have any valuable ideas to contribute, please create a pull request and provide details about the outstanding work you've done.

### Issue Reporting:

If you encounter any problems while contributing to this project, please report the issues in the [refinaid/issues](https://github.com/PetaTech/refinaid/issues) section.

> [!IMPORTANT]  
> Remember to synchronize and update your repository before starting to write code each time.
> #### Make sure to synchronize and update your repository before initiating a pull request:
> 1. Run `git stash save` to temporarily stash your local changes.
> 2. Run `git fetch upstream` to sync the source project with your local copy.
> 3. Run `git checkout main` to switch to the main branch.
> 4. Run `git merge upstream/main` to merge the updated remote version into your local copy. If there are no conflicts, the update process is complete.
> 5. Run `git stash pop` to apply your temporarily stashed changes back to your working directory. Resolve any conflicts if necessary.

## 🤖 Run the Services

Python version `python3.11.1` with `gradio, scikit-learn, seaborn, pandas, numpy, matplotlib, joblib`

### Clone the Repository

Make sure you have `git` installed on your machine. If not, you can download it [here](https://git-scm.com/downloads).


```shell
$ git clone git@github.com:<your_user_name>/refinaid.git
```

### Access the Application

```shell
# If you want to access to Simple AI
$ cd refinaid/apps/simple-ai

# If you want to access to Chatger
$ cd refinaid/apps/chatger
```


### Build `venv` for MacOS/Linux

```shell
$ pip3 install virtualenv
$ python3.11 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

### Build `venv` for Windows
```shell
$ pip install virtualenv
$ python3.11 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```

### Run web app
```shell
$ ./scripts/build.sh

# run with uvicorn
$ uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

# And open your browser and visit http://localhost:8080
```

> [!NOTE]
> We have streamlined and unified the file structure to enable developers to easily access and launch SIMPLE-AI and Chatger using a consistent approach. Additionally, we are actively planning to adopt a modular development approach to enhance the application's deployment and functionality.

### Build Docker Image

```shell
# For Simple AI
$ docker build -t refinaid-simple-ai:latest .
$ docker run -d -p 8080:8080 refinaid-simple-ai:latest

# For Chatger
$ docker build -t refinaid-chatger:latest .
$ docker run -d -p 8080:8080 refinaid-chatger:latest
```

## 📲 Contact

> **Abbass Sharara**
> 
> <aside>
>   📩 E-mail: <a href="mailto:official@lovedbymen.com">official@lovedbymen.com</a>
> <br>
>   🧳 Linkedin: <a href="https://www.linkedin.com/in/Abbass-Sharara/">Abbass Sharara</a>
> <br>
>   👨🏻‍💻 GitHub: <a href="https://github.com/PetaTech">PetaTech</a>
>    
> </aside>

## 🪪 License

Released under [Apache-2.0 license](./LICENSE) by [Abbass Sharara](https://github.com/PetaTech).

This software can be modified and reused without restriction.
The original license must be included with any copies of this software.
If a significant portion of the source code is used, please provide a link back to this repository.
