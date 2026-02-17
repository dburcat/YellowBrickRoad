
# My FirstRepo

## How to Download

### Part 1 - Forking the Project

* navigate to `https://github.com/ZipCodeCore/FirstRepo`
* To _fork_ the project, click the `Fork` button located at the top right of the project.
* this makes a copy of the code IN YOUR Github ACCOUNT


### Part 2 - Navigating to _forked_ Repository
* Navigate to **your github account** to find the _newly forked repository_.
* This is your copy of the code, not the original copy of ZipCode's
* Copy the URL of the project to the clipboard.

### Part 3 - Cloning _forked_ repository
* Clone the repository from **your account** into the `~/Projects` directory.
    * if you do not have a `~/Projects` directory, make one by executing the following command in terminal when you are in your home directory:
      * `cd`
      * `mkdir ~/Projects`
    * navigate to the `~/Projects` directory by executing the following command:
      * `cd ~/Projects`
    * clone the project by executing the following command:
      * `git clone https://github.com/ZipCodeCore/FirstRepo`
    * navigate to the `FirstRepo` directory by executing the following command:
      * `cd ~/Projects`

_Please note, __Projects__, is just a suggestion. Over the years, some have made it __Code__, __Source__, __src__ or even just __p__. _kristofer did that for decades._
Generally, though, you should keep all your source code together in a _folder/directory_. _

## Make Changes
* edit the `my-name` file inside the _FirstRepo_ directory, by adding your name to the file.


## How to Submit

This is what we refer to as **The 'holy' Triad**, `git add`, `git commit`, `git push`


### Part 1 -  _Pushing_ local changes to remote repository
* from a _terminal_ navigate to the root directory of the _cloned_ project.
* from the root directory of the project, execute the following commands:
    * add all changes
        * `git add .`
    * commit changes to be pushed
        * `git commit -m 'I have added changes'`
    * push changes to your repository
        * `git push`
* now, check that the code has been copied UP to the Github site.
   * navigate to your fork of the repo, the one in your account.
   * make sure the commit message is correct and up to date.
   * look in the _my-name_ file up on the github site to make sure your name is there.

### Part 2 - Submitting assignment
* from the browser, navigate to the _forked_ project from **your** github account.
* make PULL REQUEST to the upstream lab.

You can do it, we know you can. Ask around if confused, you're not the only one confused.
