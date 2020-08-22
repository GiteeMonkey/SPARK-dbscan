
dev-setup
============

<p align="center">
  <img src="https://raw.githubusercontent.com/donnemartin/dev-setup-resources/master/res/repo-header.gif">
</p>

## Motivation

Setting up a new developer machine can be an **ad-hoc, manual, and time-consuming** process.  `dev-setup` aims to **simplify** the process with **easy-to-understand instructions** and **dotfiles/scripts** to **automate the setup** of the following:

* **OS X updates and Xcode Command Line Tools**
* **OS X defaults** geared towards developers
* **Developer tools**: Vim, bash, tab completion, curl, git, GNU core utils, Python, Ruby, etc
* **Developer apps**: iTerm2, Sublime Text, Atom, VirtualBox, Vagrant, Docker, Chrome, etc
* **Python data analysis**: IPython Notebook, NumPy, Pandas, Scikit-Learn, Matplotlib, etc
* **Big Data platforms**: Spark (with IPython Notebook integration) and MapReduce
* **Cloud services**: Amazon Web Services (Boto, AWS CLI, S3cmd, etc) and Heroku
* **Common data stores**: MySQL, PostgreSQL, MongoDB, Redis, and Elasticsearch
* **Javascript web development**: Node.js, JSHint, and Less
* **Android development**: Java, Android SDK, Android Studio, IntelliJ IDEA

### But...I Don't Need All These Tools!

**`dev-setup` is geared to be more of an organized *reference* of various developer tools.**

**You're *not* meant to install everything.**

If you're interested in automation, `dev-setup` provides a customizable [setup script](#single-setup-script).  There's really no one-size-fits-all solution for developers so you're encouraged to make tweaks to suit your needs.

[Credits](#credits): This repo builds on the awesome work from [Mathias Bynens](https://github.com/mathiasbynens) and [Nicolas Hery](https://github.com/nicolashery).

### For Automation, What About Vagrant, Docker, or Boxen?

[Vagrant](#vagrant) and [Docker](#docker) are great tools and are set up by this repo. I've found that Vagrant works well to ensure dev matches up with test and production tiers. I've only started playing around with Docker for side projects and it looks very promising. However, for Mac users, Docker and Vagrant both rely on **virtual machines**, which have their own considerations/pros/cons.

[Boxen](https://boxen.github.com/) is a cool solution, although some might find it better geared towards "more mature companies or devops teams". I've seen some discussions of [difficulties as it is using Puppet under the hood](https://github.com/boxen/our-boxen/issues/742).

This repo takes a more **light-weight** approach to automation using a combination of **Homebrew, Homebrew Cask, and shell scripts** to do basic system setup.  It also provides **easy-to understand instructions** for installation, configuration, and usage for each developer app or tool.

<p align="center">
  <img src="https://raw.githubusercontent.com/donnemartin/dev-setup-resources/master/res/iterm2.png">
</p>

### Sections Summary
* Section 1 contains the dotfiles/scripts and instructions to set up your system.
* Sections 2 through 7 detail more information about installation, configuration, and usage for topics in Section 1.

## Section 1: Installation

**Scripts tested on OS X 10.10 Yosemite and 10.11 El Capitan.**
