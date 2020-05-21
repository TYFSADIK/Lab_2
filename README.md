# Setup
This will download Lab 2 locally, allowing you to work on your scripts and upload (push) them back up to GitHub.

1. Clone your lab repository into your ~/ops435/lab2 directory using SSH:
```bash
git clone git@github.com:ops435/lab2-yourgithubusername.git ~/ops435/lab2/
```
# Submission
1. Run the checking script:
```bash
cd ~/ops435/lab2/
pwd #confirm that you are in the right directory
python3 ./CheckLab2.py -f -v
```
Before moving on to the next step, make sure you identify any and all errors in your scripts.

2. Commit and push (upload) your Python scripts:
```bash
git add *
git commit -m "Individual message or note."
git push
```

You can make changes to your scripts and reupload as many times as you like. Make sure you commit+push to do so.

**Note:** Your lab is automatically submitted at the due date and time using the last published code. Any changes you publish after the due date won't be marked or seen by your professor.
