#!/usr/bin/env bash
container run \
    --interactive \
    --tty \
    --rm \
    --env OPENROUTER_API_KEY="$OPENROUTER_API_KEY" \
    --env OPENROUTER_KEY="$OPENROUTER_KEY" \
    --volume="$(pwd)/workspace":/workspace \
    --workdir /workspace/go-jsonnet  \
    dan-buildbox:$(git rev-parse --short HEAD) \
    llm prompt \
        --tool bazel \
        --tool rg \
        --tool sed \
        --tool read_file \
        --tool write_file \
        --tool replace_in_file \
        --tools-debug \
        --chain-limit 0 \
        --model openrouter/openai/gpt-5-codex \
        "Can you see any missing unit tests in this repo (go-jsonnet)?"
