import llm
import subprocess


def bazelisk(args: list[str]) -> tuple[int, str]:
    """
    Runs bazelisk on the input args and returns the exit code and combined stdout and stderr.
    """
    result = subprocess.run(["bazelisk"] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return result.returncode, result.stdout

def bash(args: list[str]) -> tuple[int, str]:
    """
    Runs bash on the input args and returns the exit code and combined stdout and stderr.
    """
    result = subprocess.run(["bash"] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return result.returncode, result.stdout

def bash(args: list[str]) -> tuple[int, str]:
    """
    Runs aider on the input args and returns the exit code and combined stdout and stderr.
    """
    result = subprocess.run(["aider"] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return result.returncode, result.stdout

@llm.hookimpl
def register_tools(register):
    register(bazelisk)
    register(bash)
    register(aider)
