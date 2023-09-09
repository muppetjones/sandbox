# Github Actions

## Pattern

* <https://waylonwalker.com/hatch-version/>

## Workflows

1. Continuous Integration
    * On every PR, run tests for all packages changed between head and base
2. Continuous Deploy
    * On `release/*` and `hotfix/*` branches after CI
    * On push to develop (with relevant changes)

### Continuous Integration (CI)

```mermaid
stateDiagram-v2
    Python: Python Version
    
    classDef artifact font-style:italic,font-weight:bold,fill:white,color:black
    class wheel artifact
    class report artifact

    state if_event <<choice>>
    state if_branch <<choice>>

    state Event {
        direction LR
        [*] --> event
        event --> if_event
        if_event --> branch: push
        if_event --> branch: pull_request
        branch --> if_branch
        if_branch --> True: main
        if_branch --> True: develop
        if_branch --> False
        if_event --> False
        False --> [*]
        True --> [*]
    }

    state Project {
        direction LR
        [*] --> Python

        state Python {
            direction LR
            setup1: setup
            setup1 --> lint
            lint --> test
            test --> report
        }

        Python --> build
        build --> wheel
        wheel -->[*]
    }

    [*] --> Event
    Event --> change_matrix
    change_matrix --> Project
    Project --> [*]
```

### Format

```mermaid
stateDiagram-v2
    python: python, ipython
    
    classDef artifact font-style:italic,font-weight:bold,fill:white,color:black
    classDef commit font-style:italic,font-weight:bold,fill:gray,color:black
    commit_py: commit
    commit_md: commit
    class commit_py,commit_md commit

    class wheel artifact
    class report artifact

    state if_event <<choice>>
    state if_branch_push <<choice>>
    state if_branch_pr <<choice>>
    branch_pr: branch
    branch_push: branch

    state Event {
        direction LR
        [*] --> event
        event --> if_event
        if_event --> branch_push: push
        branch_push --> if_branch_push
        if_branch_push --> True: develop
        if_branch_push --> False
        if_event --> branch_pr: pull_request
        branch_pr --> if_branch_pr
        if_branch_pr --> True: main
        if_branch_pr --> True: develop
        if_branch_pr --> False
        if_event --> False
        False --> [*]
        True --> [*]
    }

    state FileType {
        state python {
            direction LR
            isort --> black
            black --> commit_py
        }
        --
        state markdown {
            direction LR
            markdownlint --> commit_md
        }

    }
    [*] --> Event
    Event --> change_matrix
    change_matrix --> FileType
    FileType --> [*]

```
