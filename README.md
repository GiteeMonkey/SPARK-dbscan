
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

* [Single Setup Script](#single-setup-script)
* [bootstrap.sh script](#bootstrapsh-script)
    * Syncs dev-setup to your local home directory `~`
* [osxprep.sh script](#osxprepsh-script)
    * Updates OS X and installs Xcode command line tools
* [brew.sh script](#brewsh-script)
    * Installs common Homebrew formulae and apps
* [osx.sh script](#osxsh-script)
    * Sets up OS X defaults geared towards developers
* [pydata.sh script](#pydatash-script)
    * Sets up python for data analysis
* [aws.sh script](#awssh-script)
    * Sets up Spark, Hadoop MapReduce, and Amazon Web Services
* [datastores.sh script](#datastoressh-script)
    * Sets up common data stores
* [web.sh script](#websh-script)
    * Sets up JavaScript web development
* [android.sh script](#androidsh-script)
    * Sets up Android development

## Section 2: General Apps and Tools

* [Sublime Text](#sublime-text)
* [Atom](#atom)
* [Terminal Customization](#terminal-customization)
* [iTerm2](#iterm2)
* [Vim](#vim)
* [Git](#git)
* [VirtualBox](#virtualbox)
* [Vagrant](#vagrant)
* [Docker](#docker)
* [Homebrew](#homebrew)
* [Ruby and rbenv](#ruby-and-rbenv)
* [Python](#python)
* [Pip](#pip)
* [Virtualenv](#virtualenv)
* [Virtualenvwrapper](#virtualenvwrapper)

## Section 3: Python Data Analysis

* [Anaconda](#anaconda)
* [IPython Notebook](#ipython-notebook)
* [NumPy](#numpy)
* [Pandas](#pandas)
* [Matplotlib](#matplotlib)
* [Seaborn](#seaborn)
* [Scikit-learn](#scikit-learn)
* [SciPy](#scipy)
* [Flask](#flask)
* [Bokeh](#bokeh)

## Section 4: Big Data, AWS, and Heroku

* [Spark](#spark)
* [MapReduce](#mapreduce)
* [Awesome AWS](#awesome-aws-)
* [AWS Account](#aws-account)
* [AWS CLI](#aws-cli)
* [SAWS](#saws)
* [Boto](#boto)
* [S3cmd](#s3cmd)
* [S3DistCp](#s3distcp)
* [S3-parallel-put](#s3-parallel-put)
* [Redshift](#redshift)
* [Kinesis](#kinesis)
* [Lambda](#lambda)
* [AWS Machine Learning](#aws-machine-learning)
* [Heroku](#heroku)

## Section 5: Data Stores

* [MySQL](#mysql)
* [MySQL Workbench](#mysql-workbench)
* [MongoDB](#mongodb)
* [Redis](#redis)
* [Elasticsearch](#elasticsearch)

## Section 6: JavaScript Web Development

* [Node.js](#nodejs)
* [JSHint](#jshint)
* [Less](#less)

## Section 7: Android Development

* [Java](#java)
* [Android SDK](#android-sdk)
* [Android Studio](#android-studio)
* [IntelliJ IDEA](#intellij-idea)

## Section 8: Misc

* [Contributions](#contributions)
* [Credits](#credits)
* [Contact Info](#contact-info)
* [License](#license)

## Section 1: Installation

### Single Setup Script

#### Running with Git

##### Clone the Repo

    $ git clone https://github.com/donnemartin/dev-setup.git && cd dev-setup

##### Run the .dots Script with Command Line Arguments

**Since you probably don't want to install every section**, the `.dots` script supports command line arguments to run only specified sections.  Simply pass in the [scripts](#scripts) that you want to install.  Below are some examples.

**For more customization, you can [clone](#clone-the-repo) or [fork](https://github.com/donnemartin/dev-setup/fork) the repo and tweak the `.dots` script and its associated components to suit your needs.**

Run all:

    $ ./.dots all

Run `bootstrap.sh`, `osxprep.sh`, `brew.sh`, and `osx.sh`:
