# Setup
Clone your lab repository into your ~/ops435/lab1 directory using SSH:
```bash
git clone git@github.com:ops435/lab1-yourgithubusername.git ~/ops435/lab1/
```

Clone your lab repository using HTTPS:
```bash
git clone https://github.com/ops435/lab1-yourgithubusername.git ~/ops435/lab1/ # (login required)
```

# Submission
Run the checking script:
```bash
cd ~/ops435/lab2/
pwd #confirm that you are in the right directory
python3 ./CheckLab2.py -f -v
```
Before moving on to the next step, make sure you identify any and all errors in your scripts.

Commit and push (upload) your Python scripts:
```bash
git add lab*
git commit -m "Individual message or note."
git push
```

You can make changes to your scripts and reupload as many times as you like. Make sure you commit+push to do so.

**Note:** Your lab is automatically submitted at the due date and time using the last published code. Any changes you publish after the due date won't be marked or seen.
