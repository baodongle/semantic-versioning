# Semantic Versioning

[Software versioning](https://en.wikipedia.org/wiki/Software_versioning) is the process of assigning unique version numbers to unique states of computer software. These numbers are generally assigned in increasing order and correspond to new developments in the software.

Modern computer software is often tracked using two different software versioning schemes—internal version number that may be incremented many times in a single day, such as a revision control number, and a released version that typically changes far less often, such as [semantic versioning](https://semver.org/) or a project code name.

Semantic versioning is a simple set of rules and requirements that dictate how version numbers are assigned and incremented. These rules are based on but not necessarily limited to pre-existing widespread common practices in use in both closed and open-source software.

Version numbers are denoted using a standard tuple of integers: `major.minor.patch`.

![Semantic Versioning Component Numbers](semver.png)

- A `major` version identifies the product stage of the project. The basic intent is that `major` versions are incompatible, large-scale upgrades of the software component. This enables a check of a client application against the latest version of the software component to ensure compatibility. If there is a discrepancy between the two, the client application MUST be updated accordingly.

- A `minor` version is incremented when substantial new functionality or improvement are introduced; the `major` version number doesn't change. A `minor` version retains backward compatibility with older minor versions. It is NOT forward compatible as a previous `minor` version doesn't include new functionality or improvement that has been introduced in this newer `minor` version.

- A `patch` version is incremented when bugs were fixed or implementation details were refactored. The `major` and `minor` version don't change. A `patch` version is backward and forward compatible with older and newer patches of the same major and minor version.

## Waypoint 1: Convert a Semantic Versioning Component Number String to a Tuple

Write a Python function `convert_string_to_version_component_numbers` that takes an argument `s`, a string representation of a semantic versioning 3-component number (at least 1), and that returns a tuple composed of 3 integers `(major, minor, patch)`.

If only 1-component number is given, the function returns `minor` and `patch` equal to `0`.

For example:

```python
>>> convert_string_to_version_component_numbers("4.7.6")
(4, 7, 6)
>>> convert_string_to_version_component_numbers("4.7")
(4, 7, 0)
>>> convert_string_to_version_component_numbers("4")
(4, 0, 0)
```

## Waypoint 2: Compare Versions

Write a Python function `compare_versions` that takes two argument `this` and `other`, both tuples composed of 3 integers `(major, minor, patch)` each, and returns:

- `1` if `this` is above `other`;
- `0` if `this` equals `other`;
- `-1` if `this` is below `other`.

For instance:

```python
>>> compare_versions((1, 0, 1), (1, 0, 0))
1
>>> compare_versions((3, 1, 5), (3, 1, 5))
0
>>> compare_versions((2, 0, 1), (4, 7, 0))
-1
```

## Waypoint 3: Write a Class `Version`

Write a [Python class](https://docs.python.org/3/tutorial/classes.html) `Version` which [class construction, also known as _initialization method_](https://docs.python.org/3/reference/datamodel.html#object.__init__), accepts:

- a string representation of a semantic versioning 3-component number (at least 1);
- from 1 to 3 integers representing, in that particular order, `major`, `minor`, and `patch`;
- a tuple from 1 to 3 integers representing, in that particular order, `major`, `minor`, and `patch`: `(major[, minor[, patch]])`.

If `minor` and `patch` are not specified, their default value is `0`.

For example:

```python
>>> Version("1")
>>> Version("1.2")
>>> Version("1.2.8")
>>> Version(1)
>>> Version(1, 2)
>>> Version(1, 2, 8)
>>> Version((1,))
>>> Version((1, 2))
>>> Version((1, 2, 8))
```

The class `Version` has 3 [instances variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables), also known as _attributes_ or _members_, named `major`, `minor`, and `patch`.

```python
>>> version = Version("2")
>>> (version.major, version.minor, version.patch)
(2, 0, 0)
>>> version = Version(1, 4)
>>> (version.major, version.minor, version.patch)
(1, 4, 0)
>>> version = Version((10, 3, 284))
>>> (version.major, version.minor, version.patch)
(10, 3, 284)
```

## Waypoint 4: Compute "Official" String Representations

Write the instance method [`__repr__`](https://docs.python.org/3/reference/datamodel.html#object.__repr__) to compute the “official” string representation of a `Version` object. It returns a string that yields an object with the same value as when we pass it to the [Python built-in eval](https://docs.python.org/3/library/functions.html#eval), i.e., a string representation of a valid Python expression that could be used to recreate an object with the same value.

For example:

```python
>>> Version("1.2.8")
Version(1, 2, 8)
>>> eval(repr(Version("1.2.8")))
Version(1, 2, 8)
```

## Waypoint 5: Compute "Informal" String Representation

Write the instance method [`__str__`](https://docs.python.org/3/reference/datamodel.html#object.__str__) to compute the "informal" or nicely printable string representation of a `Version` object.

For example:

```python
>>> print(Version(1, 7, 0))
1.7.0
```

## Waypoint 6: Compare `Version` Instances

Write the ["rich comparison" instance methods](https://docs.python.org/3.7/reference/datamodel.html#object.__lt__) to allow comparing two `Version` instances.

For example:

```python
>>> Version("1.2.8") > Version("2.4.5")
False
>>> Version("2.4.5") > Version("1.2.8")
True
>>> Version("1.2.8") < Version("2.4.5")
True
>>> Version("2.4.5") < Version("1.2.8")
False
>>> Version("2.4.5") == Version("1.2.8")
False
>>> Version("2.4.5") == Version("2.4.5")
True
>>> Version("2.4.5") != Version("2.4.5")
False
>>> Version("2.4.5") != Version("1.2.8")
True
>>> Version("2.4.5") >= Version("2.4.5")
True
>>> Version("2.4.5") >= Version("1.2.8")
True
>>> Version("2.4.5") <= Version("2.4.5")
True
>>> Version("2.4.5") <= Version("1.2.8")
False
```

# Git Hooks

[Git hooks](https://githooks.com) are scripts that Git executes before or after events such as: `commit`, `push`, and `receive`. [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) are a built-in feature - no need to download anything. Git hooks are run locally.

## Waypoint 7: Increment Version on Git Commit

Write a Python [command-line interface (CLI)](https://en.wikipedia.org/wiki/Command-line_interface) script `post_commit.py` that is intended to be used as a Git hook on [`post-commit`](https://github.com/git/git/blob/master/Documentation/githooks.txt#L142).

When [changes are committed](https://git-scm.com/docs/git-commit) to the Git repository, the script automatically increments the patch number of a semantic versioning 3-component number (at least 1) stored in a file `VERSION` located at the root folder of a Git repository.

If this file `VERSION` doesn't initially exist, the script creates it and stores the version `1.0.1` (the script assumes that the initial version before the commit is `1.0.0`).

You can install your script file, with the proper name, into the hooks folder of your Git repository to check whether it works successfully.

For example:

```bash
$ ls -la
.
..
.git
README.md
```

```bash
$ touch TODO
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	TODO

nothing added to commit but untracked files present (use "git add" to track)
$ git add TODO
$ git commit -m "Initial import"
[master f118110] Initial import
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 TODO
$ ls -la
.
..
.git
README.md
TODO
VERSION
$ cat VERSION
1.0.1
```

```bash
$ rm TODO
$ git status
On branch master
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	deleted:    TODO

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	VERSION

no changes added to commit (use "git add" and/or "git commit -a")
$ git add TODO
$ git commit -m "Remove useless file TODO"
[master 4c68419] Remove useless file TODO
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 TODO
$ cat VERSION
1.0.2
```