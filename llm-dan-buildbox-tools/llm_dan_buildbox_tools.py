import pathlib
import subprocess

import llm


def bazel(args: list[str]) -> tuple[int, str]:
    """
    Runs bazel on the input args and returns the exit code and combined stdout and stderr.

                                                               [bazel release 8.4.2]
Usage: bazel <command> <options> ...

Available commands:
  analyze-profile     Analyzes build profile data.
  aquery              Analyzes the given targets and queries the action graph.
  build               Builds the specified targets.
  canonicalize-flags  Canonicalizes a list of bazel options.
  clean               Removes output files and optionally stops the server.
  coverage            Generates code coverage report for specified test targets.
  cquery              Loads, analyzes, and queries the specified targets w/ configurations.
  dump                Dumps the internal state of the bazel server process.
  fetch               Fetches external repositories that are prerequisites to the targets.
  help                Prints help for commands, or the index.
  info                Displays runtime info about the bazel server.
  license             Prints the license of this software.
  mobile-install      Installs targets to mobile devices.
  mod                 Queries the Bzlmod external dependency graph
  print_action        Prints the command line args for compiling a file.
  query               Executes a dependency graph query.
  run                 Runs the specified target.
  shutdown            Stops the bazel server.
  sync                Syncs all repositories specified in the workspace file
  test                Builds and runs the specified test targets.
  vendor              Fetches external repositories into a folder specified by the flag --vendor_dir.
  version             Prints version information for bazel.

Getting more help:
  bazel help <command>
                   Prints help and options for <command>.
  bazel help startup_options
                   Options for the JVM hosting bazel.
  bazel help target-syntax
                   Explains the syntax for specifying targets.
  bazel help info-keys
                   Displays a list of keys used by the info command.
    """
    result = subprocess.run(["bazelisk"] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return result.returncode, result.stdout

def rg(args: list[str]) -> tuple[int, str]:
    """
    Runs rg with the input args and returns the exit code and combined stdout and stderr.
    """
    result = subprocess.run(["rg"] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return result.returncode, result.stdout

def sed(args: list[str]) -> tuple[int, str]:
    """
    Runs sed with the input args and returns the exit code and combined stdout and stderr.
    """
    result = subprocess.run(["rg"] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return result.returncode, result.stdout

def read_file(path: str) -> str:
    """
    Read the entire contents of the file at `path` and return it as an utf-8 string.
    """
    return pathlib.Path(path).read_text(encoding="utf-8")

def write_file(path: str, content: str):
    """
    Overwrite the file at `path` with the given `content` (assumed to be a utf-8 string).
    """
    pathlib.Path(path).write_text(content, encoding="utf-8")

def replace_in_file(path: str, old: str, new: str):
    """
    Replace the given `old` text with the given `new` text in the file at the given `path`.
    Assumes there will be exactly one match for the `old` text in the file.
    Assumes `old` and `new` are utf-8 strings.
    """
    text = pathlib.Path(path).read_text(encoding="utf-8")
    parts = text.split(old)
    if len(parts) != 2:
        raise ValueError(f"Expected exactly one match, found {len(parts)-1}")
    pathlib.Path(path).write_text(new.join(parts), encoding="utf-8")

@llm.hookimpl
def register_tools(register):
    register(bazel)
    register(rg)
    register(read_file)
    register(write_file)
    register(replace_in_file)
