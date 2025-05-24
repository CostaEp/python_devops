from git import Repo

repo = Repo.init("git_python_lab")
repo.index.commit("initial commit")
print("Repo initialized and initial commit made at :", repo.working_dir)
